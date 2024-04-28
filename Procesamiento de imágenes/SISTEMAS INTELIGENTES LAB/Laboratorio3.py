import numpy as np
import cv2 

img = cv2.imread('D.png',0)
cv2.imwrite('Dgris.png',img)
cv2.imshow('imagen',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
