import numpy as np
from matplotlib import pylab as pl
from math import *
#write by Chen Yinan
class pendulum:
    def __init__(self,FD=1.2,theta_init=0.2,w_init=0,omegaD=2/3,dt=0.04,m=1):
        self.theta=[theta_init]
        self.w=[w_init]                           #角速度
        self.omegaD=omegaD
        self.FD=FD
        self.E=[0.5*m*(9.8**2)*(w_init**2+theta_init**2)]         #energy,我们假定m=1kg，考虑相对能量的变化，l=g=9.8,绳子长L=9.8m
        self.dt=dt
        self.t=[0]
    def calculate(self):
        FD=self.FD
        omegaD=self.omegaD
        for i in range(1,3001):
            tmpw=self.w[i-1]-( sin(self.theta[i-1])+0.5*self.w[i-1]+FD*sin(omegaD*self.t[i-1]) )*self.dt
            self.w.append(tmpw)
            tmptheta=self.theta[i-1]+tmpw*self.dt
            if tmptheta>pi :
                tmptheta-=2*pi
            elif tmptheta<-pi:
                tmptheta+=2*pi
            self.theta.append(tmptheta)
            #tmpE=self.E[i-1]+0.5*(9.8**2)*(self.w[i-1]**2+self.theta[i-1]**2)*(self.dt**2) #m=1
            tmpE=0.5*(9.8**2)*(self.w[i]**2)+9.8*9.8*(1-cos(self.theta[i]))
            self.E.append(tmpE)
            self.t.append(self.t[i-1]+self.dt)
    
    def showtheta(self,label1):
        pl.plot(self.t,self.theta,label=label1)                                      
        pl.xlabel('time/s')
        pl.ylabel('theta/radians')
    def showEnergy(self,label1):
        pl.plot(self.t,self.E,label=label1)                                      
        pl.xlabel('time/s')
        pl.ylabel('energy/J')
    def gettheta(self):
        return self.theta
    def gettime(self):
        return self.t
def plotdelta(delta,t,label1):
    pl.plot(t,delta,label=label1)                                      
    pl.xlabel('time/s')
    pl.ylabel('Δtheta/radians')
theta1=[]
theta2=[]
t=[]
delta_theta=[]
pendulum1 = pendulum(0.5,0.2,0)
pendulum1.calculate()
pendulum2 = pendulum(0.5,0.2001,0)
pendulum2.calculate()
theta1=pendulum1.gettheta()
theta2=pendulum2.gettheta()
t=pendulum1.gettime()
for i in range(3001):
    delta_theta.append(abs(theta1[i]-theta2[i]))
plotdelta(delta_theta,t,'ss')
pl.xlim(0,40)
pl.ylim()
pl.legend(loc='lower left') 
pl.show()

