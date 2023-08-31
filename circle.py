import numpy as np
import cv2
img = np.zeros((400, 400, 3), dtype = "uint8")
cv2.circle(img, (200, 200), 80, (255, 0, 0), 3)
cv2.imshow('dark', img)
cv2.waitKey(0)
cv2.destroyAllWindows()