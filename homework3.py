import numpy as np
from matplotlib import pylab as pl
from math import *
#write by Chen Yinan
class baseball :         
    def __init__(self,alpha=35,v_init=25,y_init=0,theta_init=24,omega=0.4*pi,dt=0.01):  #alpha is the  ,theta is the inital orientations of the stitches
        self.dt=dt                                                                  #alpha,theta shoule be degrees(角度) rather than randians（弧度）                            
        self.v_inti=v_init
        self.alpha_r=radians(alpha)                                   #translate degree into randian
        self.theta = radians(theta_init)
        self.omega=omega
        self.vx=v_init*cos(self.alpha_r)
        self.vy=v_init*sin(self.alpha_r)
        self.vz=0
        self.B_m=0.0039                                                 #B_m=B2/M                  
        self.x=[0]
        self.y=[y_init]
        self.z=[0]
        self.t=[0]
        self.theta_t=[radians(theta_init)]
    def calculate_WithDrag(self):                 
        vx=self.vx
        vy=self.vy
        vz=self.vz
        theta=[self.theta]
        self.f=[0]
        for i in range(100000000):
            
            tmpx=self.x[i]+vx*self.dt
            tmpy=self.y[i]+vy*self.dt
            tmpz=self.z[i]+vz*self.dt
            self.x.append(tmpx)
            self.y.append(tmpy)
            self.z.append(tmpz)

            v=sqrt(vx**2+vy**2)
            B_m=0.0039+0.0058/(1+exp((v-35)/5))                                    
            f=B_m*sqrt(vx**2+vy**2)
            f2=0.5*(sin(4*theta[i])-0.25*sin(8*theta[i])+0.08*sin(12*theta[i])-0.025*sin(16*theta[i]))
            vz=vz+f2*9.8*self.dt
            vx-=f*vx*self.dt
            vy=vy-(9.8*self.dt)-f*vy*self.dt
            
            theta.append(theta[i]+self.omega*self.dt)
            self.theta_t.append(degrees(theta[i+1]))
            self.f.append(f2)
            self.t.append(self.t[i-1]+self.dt)
            if self.x[i]>60:                              #本垒
               break
            #if self.y[i]<0 :
            #    j=i
            #    break
        #b=-self.y[j]/self.y[j-1]
        #self.x[j]=(self.x[j]+b*self.x[j-1])/(1+b)
        #self.y[j]=0
        #self.theta_t=theta
        print("done")
    def showResults_f(self,style='g',label1='??'):
        pl.plot(self.theta_t,self.f,style,label=label1)                                      
        pl.xlabel('theta/degree')
        pl.ylabel('force/weight')
        
    def showResults(self,style='',label1='??'):       #style=风格，label=图例
        pl.plot(self.x,self.z,style,label=label1)                                      
        pl.xlabel('x/m')
        pl.ylabel('z/m')
        #pl.ylim(-0.5,0.2)
        #pl.xlim(0,51000)
        #pl.ylim(0,20000) 

a=baseball()
a.calculate_WithDrag()
a.showResults()
pl.show()


