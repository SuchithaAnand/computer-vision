import cv2
import numpy as np


image_path ="C:\\Users\\DELL\\Downloads\\img.jpg"
image = cv2.imread(image_path)


text = "Hello, World!!!"
position = (50, 100)  


font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 1
font_color = (240, 248, 255)  
thickness = 2

text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]


text_x = (image.shape[1] - text_size[0]) // 2
text_y = position[1]


cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness)


cv2.imshow("Image with Text", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
