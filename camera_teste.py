import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    
    ret, frame = cap.read()

    
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #resultado = cv2.Canny(gray, 50, 50)

    
    cv2.imshow('frame1',frame)
    #cv2.imshow('frame',gray)
    #cv2.imshow('frame2',resultado)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()