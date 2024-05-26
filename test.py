import cv2
import numpy as np

# Đọc ảnh mẫu biển cấm rẽ trái
forbidden_left_turn = cv2.imread('forbidden_left_turn.jpg', 0)

# Khởi tạo SIFT detector
sift = cv2.SIFT_create()

# Tìm keypoints và descriptors trong ảnh mẫu
kp1, des1 = sift.detectAndCompute(forbidden_left_turn, None)

# Khởi tạo FLANN matcher
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Hàm để nhận diện biển báo và hiển thị văn bản
def detect_and_display_text(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    kp2, des2 = sift.detectAndCompute(gray, None)

    # Tìm các matches giữa ảnh mẫu và ảnh camera
    matches = flann.knnMatch(des1, des2, k=2)

    # Áp dụng tỷ lệ Lowe's để lọc các matches tốt
    good_matches = []
    for m, n in matches:
        if m.distance < 0.7 * n.distance:
            good_matches.append(m)

    # Nếu số lượng matches tốt đủ nhiều, hiển thị văn bản
    if len(good_matches) > 10:
        cv2.putText(frame, 'Cấm rẽ trái', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    return frame

# Khởi động camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Gọi hàm nhận diện và hiển thị văn bản
    frame = detect_and_display_text(frame)

    # Hiển thị khung hình
    cv2.imshow('Frame', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
