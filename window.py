import cv2

img = cv2.imread("data/src/Lena.jpg")
cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window", 640, 480)
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()