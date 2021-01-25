import cv2
import numpy as np

lower = np.array([0,20,70], dtype=np.uint8)
upper = np.array([20,255,255], dtype=np.uint8)

cap = cv2.VideoCapture(0)

kernel = np.zeros((3,3),np.uint8)

while (True) :
    _, frame = cap.read()
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    mask = cv2.inRange(hsv, lower, upper)
    mask = cv2.dilate(mask, kernel,iterations = 4)
    mask = cv2.GaussianBlur(mask, (5,5), 100)

    _, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    if len(contours) < 1 or len(contours) == 0:
        continue
    else:
        pass

    contours = max(contours, key = lambda x: cv2.contourArea(x))

    epsilon = 0.0005*cv2.arcLength(contours,True)
    appctr = cv2.approxPolyDP(contours,epsilon,True)

    hull = cv2.convexHull(contours)

    hull = cv2.convexHull(appctr, returnPoints=False)
    defects = cv2.convexityDefects(appctr, hull)

    for i in range(defects.shape[0]):
        s, e, _, _ = defects[i,0]
        start = tuple(appctr[s][0])
        end = tuple(appctr[e][0])

        cv2.line(frame,start, end, [20,255,255], 2)

    cv2.imshow('mask',mask)
    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()
cap.release()    