import cv2
import numpy as np

video = cv2.VideoCapture("movimentacao-de-objetos-480.mov")
#video = cv2.VideoCapture(0)

while True:

    ret, frame = video.read()

    cinza = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    ret, imagemBin = cv2.threshold(cinza,180,255,cv2.THRESH_BINARY_INV)

    contornos, __ = cv2.findContours(imagemBin,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    if len(contornos) == 2:

        momentos1 = cv2.moments(contornos[0])

        x1 = int(momentos1["m10"]/momentos1["m00"])
        y1 = int(momentos1["m01"]/momentos1["m00"])

        cv2.circle(frame,(x1,y1),3,(255,0,0),-1)

        momentos2 = cv2.moments(contornos[1])

        x2 = int(momentos2["m10"]/momentos2["m00"])
        y2 = int(momentos2["m01"]/momentos2["m00"])

        cv2.circle(frame,(x2,y2),3,(255,0,0),-1)

        distancia = int(np.sqrt(((x2-x1)**2)+((y2-y1)**2)))
        print(distancia)

        posx = int((x1+x2)/2)
        posy = int((y1+y2)/2)

        fonte = cv2.FONT_HERSHEY_SIMPLEX

        cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)

        cv2.putText(frame,str(distancia),(posx,posy),fonte,0.5,(0,0,0),2,cv2.LINE_AA)


    cv2.imshow('frame',frame)
    cv2.imshow('imagemBin',imagemBin)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()