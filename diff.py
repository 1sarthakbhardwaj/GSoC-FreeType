import sys
import cv2

base_img_path = sys.argv[1]
test_img_path = sys.argv[2]

base_img = cv2.imread(base_img_path, 0)
test_img = cv2.imread(test_img_path, 0)

diff_img = cv2.bitwise_xor(base_img, test_img)

cv2.imwrite('diff.png', diff_img)
