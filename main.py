from email.errors import CloseBoundaryNotFoundDefect
import cv2
import numpy as np
from windows_cleaner import delete_little_part

gray=cv2.imread("gray_image.jpg")
cleaned_img=delete_little_part(gray)
if gray.shape[2]>1:
    gray = cv2.cvtColor(gray,cv2.COLOR_BGR2GRAY)
total=cv2.vconcat([gray,cleaned_img])
cv2.imshow("total",total)
cv2.imwrite("cleaned_img.jpg",cleaned_img)
cv2.waitKey(0)
