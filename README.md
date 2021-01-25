# Hand-detection  

Convex hull hand detection code.  

# How it works

1. set upper color and lower color. This may be your skin color.  
2. Read camera frame.
3. Turn frame into binary array - Area that is in your color range will be 1(White), else will be 0(black)  
4. Calculate contour of white area.  
5. Draw convex hull at RGB frame.  

# Example

![Example](https://user-images.githubusercontent.com/56443524/105649199-8caa4e00-5ef2-11eb-83a4-c44b15a4240f.PNG)



# Require

Cv2  
Numpy
