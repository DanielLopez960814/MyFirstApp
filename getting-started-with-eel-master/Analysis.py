import cv2
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import os
import sys
import csv


#f = open(path, 'r')
#f1 = f.readlines()
#for x in f1:
#    path_i = x
def morning_analysis(image):
        #Basic Process
        im2 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        im2 = 255 - im2
        im2 = (abs(im2 - im2.mean()))
        
        #Statistical Analysis
        [fil, col] = im2.shape
        a = []
        for i in range(fil):
            for j in range(col):
                if im2[i,j] > 0:
                    a.append(im2[i,j])
        Q1 = np.quantile(a, .25)
        Q3 = np.quantile(a, .75)
        Range = Q3 - Q1
        outlier = Q1 + 1.5 * Range
        
        #Outlier extraction
        
        #Lookup table
        func = []
        for i in range(256):
            if (i > outlier):
                func.append(i) 
            else:
                func.append(0)
        
        #Image outlier extraction
        for i in range(fil):
            for j in range(col):
                value = int(im2[i,j])
                value = func[value]
                im2[i,j] = value
        #im2[0:350,:] = 0
        #im2[350:420,0:200] = 0
        #im2[im2 > 0] = 255
        return im2

def imageAnalysis():

    #Read coordinates
    coordinatesPath =  'coordinatesCropping.txt'
    file = open(coordinatesPath, 'r')
    coordinatesStr = file.read()

    ## Turn string [(x, y), (w,z)] into numb [x,y,w,z]
    coordinatesStr = coordinatesStr.strip('][').strip('()')
    coordinatesStr = coordinatesStr.split(',')
    coordinatesStr[1] = coordinatesStr[1].strip(')')
    coordinatesStr[2] = coordinatesStr[2].strip(' (')
    coordinatesStr = [int(i) for i in coordinatesStr]

    #Images files path
    path = 'Ruta.txt' 
    tendency = [] # array of [sum(:), frame]
    values = [] # array of sum(:) for plotting
    f = open(path, "r") 
    l = 1
    #print(f)
    #Itetarions over the each images
    for x in f:
        x = x.replace("\n", "") #dealing with \n
        im = cv2.imread(str(x))
        im = cv2.resize(im, (800, 600)) #standard
        im = im[coordinatesStr[1]:coordinatesStr[3], coordinatesStr[0]:coordinatesStr[2]]
        #cv2.imshow('ImageWindow', im)
        #cv2.waitKey(0)
        print('Wait, analyzing' + x)
        #sys.stdout.flush()
        im2 = morning_analysis(im)
        #cv2.imshow('ImageWindow', im2)
        #cv2.waitKey(0)
        #/home/daniel/Descargas/segmentos/
        cv2.imwrite('/home/daniel/Descargas/segmentos/'+str(l)+'.jpg', im2) #sobra
        valor = im2.sum()
        values.append(valor)
        tendency.append(['frame'+str(l),valor])
        l = l + 1


        
    values = values - np.mean(values)    #substracting the mean. Hyp: most of the images are background, not foreground
    values[values < 0] = 0

    with open('tendency.cvs', 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(tendency)

    #Plot
    arrange = np.arange(len(values))
    plt.bar(arrange, values, align='center', alpha=0.5)
    plt.savefig('plot.png')

#print('The csv file was generated')
#sys.stdout.flush()
# im = cv2.imread('/home/daniel/Descargas/frames/frame531.jpg')
# im2 = morning_analysis(im)
# valor = im2.sum()
# print(valor)
# cv2.imshow('Window',im2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#imageAnalysis()