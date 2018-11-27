import numpy as np
from matplotlib import pylab as pl
from math import *
#write by Chen Yinan
class pendulum:
    def __init__(self,FD=1.2,theta_init=0.2,w_init=0,omegaD=2/3,dt=pi/100,m=1):
        self.theta=[theta_init]
        self.w=[w_init]                           #角速度
        self.omegaD=omegaD
        self.FD=FD 
        self.E=[0.5*m*(9.8**2)*(w_init**2+theta_init**2)]         #energy,我们假定m=1kg，考虑相对能量的变化，l=g=9.8,绳子长L=9.8m，q=0.5
        self.dt=dt
        self.t=[0]
        self.theta_chaos=[]
    def calculate(self):
        FD=self.FD
        omegaD=self.omegaD
        while self.t[-1]<=1200*pi:
            tmpw=self.w[-1]-( sin(self.theta[-1])+0.5*self.w[-1]+FD*sin(omegaD*self.t[-1]) )*self.dt
            self.w.append(tmpw)
            tmptheta=self.theta[-1]+tmpw*self.dt
            if tmptheta>pi :
                tmptheta-=2*pi
            elif tmptheta<-pi:
                tmptheta+=2*pi
            if self.t[-1]>=900*pi:
                if self.t[-1]%(3*pi)<=self.dt:
                   self.theta_chaos.append(tmptheta)
            self.t.append(self.t[-1]+self.dt)
    def getTheta(self):
        return self.theta_chaos
      

#th=[]
#FD=[1.35]

#for i in range(100):
#    a=pendulum(FD[-1])
#    a.calculate()
#    points=a.getTheta()
#    for j in points:
#        FD.append(FD[-1])
#        th.append(j)
#    FD.append(FD[-1]+0.0015)

fd1=list(np.linspace(1.35,1.5,100))
fd=[]
th=[]

for i in fd1:
    a=pendulum(i)
    a.calculate()
    points=a.getTheta()
    for j in points:
        fd.append(i)
        th.append(j)
pl.scatter(fd,th,s=10)
pl.grid(True)
pl.xlim(1.35,1.48)
pl.ylim(0,3)
pl.title('Bifurcation diagram')
pl.xlabel('FD')
pl.ylabel('theta(radians)')
pl.show()
