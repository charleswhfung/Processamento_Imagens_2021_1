import numpy as np
import cv2

cap = cv2.VideoCapture(0)

mascara = cv2.imread('centrouninter.png')

angulo = 0

aux = 0
aux2 = 0

while(True):
    ret, frame = cap.read() 

    #Processamentos
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #imagemClara = cv2.add(cinza,40)

    #Escala
    #imagemEscala = cv2.resize(frame,None,fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
    
    #Rotação
    
    #Linhas, Colunas, x = frame.shape

    #matrizRotacao = cv2.getRotationMatrix2D((Colunas/2,Linhas/2),angulo,1)

    #imagemRotacionada = cv2.warpAffine(frame,matrizRotacao,(Colunas,Linhas))

    #angulo = angulo +10

    #Translação

    #Linhas, Colunas, x = frame.shape

    #matrizTranslacao = np.float32([[1, 0, aux],[0, 1, aux2]])

    #imagemTranslacao = cv2.warpAffine(frame,matrizTranslacao,(Colunas,Linhas))

    #aux = aux + 1
    #aux2 = aux2 + 1

    #Corte
    
    #y_inicial = 31
    #x_inicial = 100

    #linhas = 109 - 31
    #colunas = 432 - 100

    #imagem_cortada = frame[y_inicial:y_inicial+linhas, x_inicial:x_inicial+colunas]

    #Colocar logo
    
    linhas,colunas,canais = mascara.shape

    roi = frame[0:linhas,0:colunas]
    
    cinza = cv2.cvtColor(mascara,cv2.COLOR_BGR2GRAY)

    ret,mask = cv2.threshold(cinza,120,255,cv2.THRESH_BINARY)

    mask_inv = cv2.bitwise_not(mask)
    
    imagem1_and = cv2.bitwise_and(roi,roi,mask = mask)

    imagem2_and = cv2.bitwise_and(roi,roi,mask = mask_inv)

    ref_imagem = cv2.bitwise_and(mascara,mascara,mask=mask)

    res1 = cv2.add(imagem1_and,ref_imagem)

    res2 = cv2.add(imagem2_and,ref_imagem)

    frame1 = frame

    frame[0:linhas,0:colunas] = res2


    #frame1[0:linhas,0:colunas] = res1
    

    

    

    #Visualização
    cv2.imshow('frame1',frame)
    #cv2.imshow('frame1_1',frame1)
    #cv2.imshow('frame2',cinza)
    #cv2.imshow('frame3',imagem1_and)
    #cv2.imshow('frame3_1',imagem2_and)
    #cv2.imshow('frame4',roi)
    #cv2.imshow('frame5',res1)
    #cv2.imshow('frame6',res2)

    #cv2.imshow('frame3',imagem_cortada)
    #cv2.imshow('frame3',imagemTranslacao)
    #cv2.imshow('frame3',imagemRotacionada)
    #cv2.imshow('frame3',imagemEscala)
    #cv2.imshow('frame3',imagemClara)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

