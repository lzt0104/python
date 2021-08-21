# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 12:17:47 2021

@author: lzt

"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

v=np.array([2,0,2])
p=np.array([2,1,3])
m=0.0006
q=3
dt=0.00001
tend=0.001
data=[[0],[p[0]],[p[1]],[p[2]]]
data_skip=1000

fig = plt.figure()
sub= fig.add_subplot(111, projection='3d')


def B(p,t):#設磁場為時間、空間的函數
    (x,y,z)=(p[0],p[1],p[2])
    B=np.array([0,5,0])
    return B
    
    return B

def E(p,t):
    (x,y,z)=(p[0],p[1],p[2])
    E=np.array([0,5,7*z])#設電場為時間、空間的函數
    return E

def a(p,v,t):
    s=q/m*(np.cross(v,B(p,t))+E(p,t))#帶電粒子的加速度
    return s

for i in range(0,int(tend/dt)):#二階隆格庫塔法
        t=i*dt
        dp1=v*dt
        dv1=a(p,v,t)*dt
        dp2=(v+dv1/2)*dt
        dv2=a(p+dp1/2,v+dv1/2,t+0.5*dt)*dt
        dp3=(v+dv2/2)*dt
        dv3=a(p+dp2/2,v+dv2/2,t+0.5*dt)*dt
        dp4=(v+dv3)*dt
        dv4=a(p+dp3,v+dv3,t+dt)*dt
        dv=(dv1+2*dv2+2*dv3+dv4)/6
        dp=(dp1+2*dp2+2*dp3+dp4)/6
        p1=p+dp
        p=p1
        v1=v+dv
        v=v1
        t+=dt
        data[0].append(t)
        data[1].append(p[0])
        data[2].append(p[1])
        data[3].append(p[2])
t=np.array(data[0])
x=np.array(data[1])
y=np.array(data[2])
z=np.array(data[3])

def init_func():
    sub.clear()
    sub.plot(x,y,z)
    sub.set_xlabel('$x$',fontsize=13)
    sub.set_ylabel('$y$',fontsize=13)
    sub.set_zlabel('$z$',fontsize=13)
    sub.view_init(elev=40,azim=20)
    
def update_plot(i):
    sub.plot(x[i:i+data_skip],y[i:i+data_skip],z[i:i+data_skip])
    
anim=FuncAnimation(fig,sub,frames=np.arange(0,len(t),data_skip),init_func=init_func,interval=50)
