import cv2

import sys

cap = cv2.VideoCapture("data/movie/Cosmos.mp4")

if cap.isOpened() == False:
    sys.exit()

# ret = True or False, readed img.
ret, frame = cap.read()
h, w = frame.shape[:2]
fourcc = cv2.VideoWriter_fourcc(*"XVID")
# 30.0 = fps
dst = cv2.VideoWriter("output/test.avi", fourcc, 30.0, (w, h))

while True:
    ret, frame = cap.read()
    if ret == False:
        break
    cv2.imshow("img", frame)
    dst.write(frame)
    # Push "Esc" key exit.
    if cv2.waitKey(30) == 27:
        break

cv2.destroyAllWindows()
cap.release()