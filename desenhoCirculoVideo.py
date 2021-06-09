import cv2
import numpy as np

#criar variáveis globais
centro = (0,0)
clicado = False

def desenhaCirculo(event,x,y,flags,param):
    global centro, clicado

    if event == cv2.EVENT_LBUTTONDOWN:
        centro = (x,y)
        clicado = False

    elif event == cv2.EVENT_LBUTTONUP:
        clicado = True
        
    
    #if event == cv2.EVENT_RBUTTONDOWN:
    #    cv2.circle(imagem,(x,y),50,(0,255,0),-1)

cv2.namedWindow(winname='frame')

cap = cv2.VideoCapture(0)


cv2.setMouseCallback('frame',desenhaCirculo)

#imagem = np.zeros((512,512,3))

while True:

    ret, frame = cap.read()

    if clicado == True:
        cv2.circle(frame,centro,50,(255,255,255),2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
