# Hand-detection  

Convex hull hand detection code.  

#How it works

1. set upper color and lower color. This may be your skin color.  
2. Read camera frame.
3. Turn frame into binary array - Area that is in your color range will be 1(White), else will be 0(black)  
4. Calculate contour of white area.  
5. Draw convex hull at RGB frame.  

#Require

Cv2  
Numpy
