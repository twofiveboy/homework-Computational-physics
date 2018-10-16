import numpy as np
from matplotlib import pylab as pl
from math import *
#write by Chen Yinan
class baseball :         
    def __init__(self,theta_init=31,omega=0.4*pi,v_init=30.6,alpha=20,y_init=1,dt=0.01):  #alpha is the  ,theta is the inital orientations of the stitches
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
            elif self.y[i]<0 :
                j=i
                break
 
        
    def showResults_f(self,style='g',label1='??'):
        pl.plot(self.theta_t,self.f,style,label=label1)                                      
        pl.xlabel('theta/degree')
        pl.ylabel('force/weight')
        
    def showResults(self,label1='??',style=''):       #style=风格，label=图例
        pl.plot(self.x,self.z,style,label=label1)                                      
        pl.xlabel('x/m')
        pl.ylabel('z/m')
     




a=baseball(90,0,40.25,20)
a.calculate_WithDrag()
a.showResults()
pl.show()
vInit =20
#for i in range(5):
#    label="vInit="
#    vstr='{:.2f}'.format(vInit)
#    label+=vstr+"m/s"
#    a=baseball(31,0.2*pi,vInit)
#    a.calculate_WithDrag()
#    a.showResults(label)
#    vInit+=1

#pl.legend(loc='upper left')  


#omega =0.4*pi;

#for i in range(5):
#    label="omega="
#    omegastr='{:.2f}'.format(omega)
#    label+=omegastr+"r/s"
#    a=baseball(31,omega)
#    a.calculate_WithDrag()
#    a.showResults(label)
#    omega+=0.02*pi

#pl.legend(loc='upper left')  
#pl.show()


