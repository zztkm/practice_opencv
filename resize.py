import cv2

img = cv2.imread("data/src/grapes.jpg")

print(img.shape)
# x = 300, y = 200
size = (300, 200)
img_resize = cv2.resize(img, size)

img_area = cv2.resize(img, size, interpolation = cv2.INTER_AREA)
img_linear = cv2.resize(img, size, interpolation = cv2.INTER_LINEAR)

cv2.imshow("default_img", img)
cv2.imshow("x=300, y=200", img_resize)
cv2.imshow("area", img_area)
cv2.imshow("linear", img_linear)

cv2.waitKey(0)
cv2.destroyAllWindows()