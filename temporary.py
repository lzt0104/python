# -*- coding: utf-8 -*-
"""
Spyder Editor

@author 
"""
import cv2 
#import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (30,10),linewidth=30)
ax=760
ay=400
bx=860
by=400
axwid=50
aywid=500
bxwid=50
bywid=500
N=0
a= []
b =[]
n= []
cap = cv2.VideoCapture('/Users/rafael/Desktop/cut_video.mp4')
 
label =255    
 
while cap.isOpened():
       
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.rectangle(frame,(ax-axwid,ay-aywid),(ax+axwid,ay+aywid),(0,255,0),3)
    cv2.rectangle(frame,(bx-bxwid,by-bywid),(bx+bxwid,by+bywid),(255,0,0),3)
    cv2.rectangle(frame,(10,10),(150,150),(0,0,label),3)
    
    N+=1
    cv2.namedWindow("frame",cv2.WINDOW_NORMAL)
    #cv2.imshow('frame', frame)
    
    atatol=btatol=ctatol=d=e=f=0
    
    if 1200>=N>=300:
        label=0
        for aax in range(ax-axwid+3,ax+axwid-3,1):
            for aay in range(ay-aywid+3,ay+aywid-3,1):
                d=frame[aay,aax][0]
                atatol+=d
        a.append(atatol)
        for bbx in range(bx-bxwid+3,bx+bxwid-3,1):
           for bby in range(by-bywid+3,by+bywid-3,1):
               e=frame[bby,bbx][0]
               btatol+=e
        b.append(btatol) 
       
        n.append(N)
 
    if cv2.waitKey(1) & 0xff==ord('q') or N==3001:
        break
 
cap.release()
cv2.destroyAllWindows()
 
plt.plot(n,a,color="g",label='Left',linewidth=2)
plt.plot(n,b,color="b",label='Right',linewidth=2)
plt.title("candle Xcm",x=0.5,y=1)
plt.xlabel("frame")
plt.ylabel("blue light intensity")
plt.grid(True,linestyle = "--",color = 'gray',linewidth = '0.5',axis='both')
plt.show()
