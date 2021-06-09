import cv2
import numpy as np

#criar variáveis globais
ponto1 = (0,0)
ponto2 = (0,0)

primeiro_clique = False
segundo_clique = False


def desenhaRetangulo(event,x,y,flags,param):
    global ponto1,ponto2,primeiro_clique,segundo_clique

    if event == cv2.EVENT_LBUTTONDOWN:

        if primeiro_clique == True and segundo_clique == True:
            ponto1 = (0,0)
            ponto2 = (0,0)
            primeiro_clique = False
            segundo_clique = False

        if primeiro_clique == False:
            primeiro_clique = True
            ponto1 = (x,y)

        elif segundo_clique == False:
            segundo_clique = True
            ponto2 = (x,y)    


cv2.namedWindow(winname='frame')

cap = cv2.VideoCapture(0)


cv2.setMouseCallback('frame',desenhaRetangulo)

while True:

    ret, frame = cap.read()

    if primeiro_clique == True:
        cv2.circle(frame,ponto1,5,(255,255,255),-1)
    
    if primeiro_clique == True and segundo_clique == True:
        cv2.rectangle(frame,ponto1,ponto2,(255,255,255),2)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
