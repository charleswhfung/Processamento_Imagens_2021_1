import numpy as np
import cv2
import os

def noisy(noise_typ,image):
   if noise_typ == "gauss":
      row,col,ch= image.shape
      mean = 0
      var = 0.5
      sigma = var**0.5
      gauss = np.random.normal(mean,sigma,(row,col,ch))
      gauss = gauss.reshape(row,col,ch)
      noisy = image + image * gauss * var
      return noisy
   elif noise_typ == "s&p":
      row,col,ch = image.shape
      s_vs_p = 0.5
      amount = 0.04
      out = np.copy(image)
      # Salt mode
      num_salt = np.ceil(amount * image.size * s_vs_p)
      coords = [np.random.randint(0, i - 1, int(num_salt))
              for i in image.shape]
      out[coords] = 1

      # Pepper mode
      num_pepper = np.ceil(amount* image.size * (1. - s_vs_p))
      coords = [np.random.randint(0, i - 1, int(num_pepper))
              for i in image.shape]
      out[coords] = 0
      return out
   elif noise_typ == "poisson":
      vals = len(np.unique(image))
      vals = 2 ** np.ceil(np.log2(vals))
      noisy = np.random.poisson(image * vals) / float(vals)
      return noisy
   elif noise_typ =="speckle":
      row,col,ch = image.shape
      gauss = np.random.randn(row,col,ch)
      gauss = gauss.reshape(row,col,ch)        
      noisy = image + image * gauss
      return noisy

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read() 

    #Processamento
    #imagemRuido = noisy("gauss",frame)
    #imagemRuido = np.array(imagemRuido, dtype=np.uint8)
    #imRuido = cv2.cvtColor(imagemRuido, cv2.COLOR_BGR2GRAY)

    #imagemRuido2 = noisy("s&p",frame)
    #imagemRuido2 = np.array(imagemRuido2, dtype=np.uint8)
    #imRuido2 = cv2.cvtColor(imagemRuido2, cv2.COLOR_BGR2GRAY)

    #Pontos Isolados
    #mascara = np.ones((3,3), np.float32)

    #mascara[1,1] = -8

    #res = cv2.filter2D(frame,-1,mascara)

    #mascara_horizontal = np.float32([[-1,-1,-1],[2,2,2],[-1,-1,-1]])
    #mascara_vertical = np.float32([[-1, 2, -1],[-1, 2, -1],[-1, 2, -1]])
    #mascara_diagonal45 = np.float32([[2,-1,-1],[-1,2,-1],[-1,-1,2]])
    #mascara_diagonaln45 = np.float32([[-1,-1,2],[-1,2,-1],[2,-1,-1]])

    #res1 = cv2.filter2D(frame, -1, mascara_horizontal)
    #res2 = cv2.filter2D(frame, -1, mascara_vertical)
    #res3 = cv2.filter2D(frame, -1, mascara_diagonal45)
    #res4 = cv2.filter2D(frame, -1, mascara_diagonaln45)

    #res = cv2.Canny(frame,100,100)

    #res = cv2.blur(frame, (9,9))

    #imagemRuido = noisy("s&p",frame)

    #imagemRuido = cv2.cvtColor(imagemRuido,cv2.COLOR_BGR2GRAY)

    #res1 = cv2.blur(imagemRuido, (9,9))
    #res2 = cv2.GaussianBlur(imagemRuido,(9,9),0)
    #res3 = cv2.medianBlur(imagemRuido, 15)
    #res4 = cv2.bilateralFilter(imagemRuido,9,150,150)

    laplaciano = cv2.Laplacian(frame,cv2.CV_8U)

    res2 = cv2.subtract(frame, laplaciano)


    suviazada = cv2.GaussianBlur(frame,(13,13),3)
    detalhes = 3 * cv2.subtract(frame,suviazada)
    res = cv2.add(frame,detalhes)


    #Visualização
    cv2.imshow('frame1',frame)
    #cv2.imshow('frame2',res)
    #cv2.imshow('frame3',detalhes)
    #cv2.imshow('frame4',suviazada)
    #cv2.imshow('frame5',res2)
    #cv2.imshow('frame3',laplaciano)
    #cv2.imshow('frame2_1',res2)
    #cv2.imshow('frame2_2',res3)
    #cv2.imshow('frame2_3',res4)
    #cv2.imshow('frame3',imagemRuido)
    #cv2.imshow('frame3',res2)
    #cv2.imshow('frame4',res3)
    #cv2.imshow('frame5',res4)
    #cv2.imshow('frame2',imRuido)
    #cv2.imshow('frame3',imRuido2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()