import numpy as np
import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

#Cor/Limite inferior/Limite superior

#Amarelo/10,100,100/50,255,255

#Azul/100,100,100/140,255,255

#Verde/40,100,100/80,255,255

#Vermelho/160,100,100/200,255,255


while(True):

    ret, frame = cap.read()

    limiar_inferior = np.array([100,100,100])

    limiar_superior = np.array([140,255,255])

    frameHSI = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    ImagemSegmentada = cv2.inRange(frameHSI,limiar_inferior,limiar_superior)


    limiar_inferior2 = np.array([10,100,100])

    limiar_superior2 = np.array([50,255,255])

    frameHSI2 = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    ImagemSegmentada2 = cv2.inRange(frameHSI2,limiar_inferior2,limiar_superior2)

    contornos, __ = cv2.findContours(ImagemSegmentada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contornos = sorted(contornos, key=lambda x:cv2.contourArea(x), reverse=True)

    #print(contornos)
    m=0
    for c in contornos:
        m=m+1
        x,y,w,h = cv2.boundingRect(c)

        cv2.rectangle(frame, (x,y),(x+w,y+h),(0,0,255),2)

        media_x = (x + (x+w))/2
        media_y = (y + (y+h))/2

        media_x = int(media_x)
        media_y = int(media_y)

        #(100,200)
        STR = "("+str(media_x)+","+str(media_y)+")"

        cv2.putText(frame,STR,(media_x,media_y),font,0.5,(0,0,255),2,cv2.LINE_AA)

        centro=(media_x,media_y)
        raio = 5
        cv2.circle(frame,centro,raio,(0,255,0),-1)

        if m==2:
            break

    contornos2, __ = cv2.findContours(ImagemSegmentada2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contornos2 = sorted(contornos2, key=lambda x:cv2.contourArea(x), reverse=True)

    objeto = contornos2[0]

    x,y,w,h = cv2.boundingRect(objeto)

    cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,255),2)



    cv2.imshow('frame',frame)

    cv2.imshow('Segmentada',ImagemSegmentada)
    cv2.imshow('Segmentada2',ImagemSegmentada2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.realease()
cv2.destroyAllWindows()