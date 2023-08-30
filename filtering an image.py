import cv2
import numpy as np
image_path = "C:\\Users\\DELL\\Downloads\\img.jpg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE) 

# Apply the Sobel filter
sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)  # Sobel filter in the X direction
sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)  # Sobel filter in the Y direction

# Calculate the magnitude and angle of the gradient
gradient_magnitude = np.sqrt(sobel_x*2 + sobel_y*2)
gradient_angle = np.arctan2(sobel_y, sobel_x)

# Normalize the gradient magnitude to 0-255 range
gradient_magnitude = cv2.normalize(gradient_magnitude, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# Display the original and filtered images
cv2.imshow('Original Image', img)
cv2.imshow('Sobel Filtered Image', gradient_magnitude)
cv2.waitKey(0)
cv2.destroyAllWindows()