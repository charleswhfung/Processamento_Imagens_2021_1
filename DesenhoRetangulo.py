import cv2
import numpy as np
from numpy.lib.index_tricks import ix_

#definir variáveis globais
desenhando = False
ix = -1
iy = -1

def desenhaRetangulo(event,x,y,flags,param):
    global desenhando, ix, iy
    #detectar o pressionar do botão
    if event == cv2.EVENT_LBUTTONDOWN:
        desenhando = True
        ix = x
        iy = y    

    #detectando o arrastar do mouse
    elif event == cv2.EVENT_MOUSEMOVE:
        if desenhando == True:
            cv2.rectangle(imagem,(ix,iy),(x,y),(255,255,255),-1)

    #detectando o soltar do botão da esquerda do mouse
    elif event == cv2.EVENT_LBUTTONUP:
        desenhando = False
        cv2.rectangle(imagem,(ix,iy),(x,y),(255,0,0),-1)





    
cv2.namedWindow(winname='teste')

cv2.setMouseCallback('teste',desenhaRetangulo)

#imagem = np.zeros((512,512,3))
imagem = cv2.imread('lena_color_512.tif')

while True:

    cv2.imshow('teste',imagem)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
