import cv2
import numpy as np

def desenhaCirculo(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagem,(x,y),50,(0,0,255),-1)
    
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(imagem,(x,y),50,(0,255,0),-1)

cv2.namedWindow(winname='teste')

cv2.setMouseCallback('teste',desenhaCirculo)

imagem = np.zeros((512,512,3))

while True:

    cv2.imshow('teste',imagem)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
