import matplotlib.pyplot as pl
from math import *
import numpy as np
# this function gives trac
class hyperion():
    def __init__(self,thetainit):
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.vy=[5]               #vy=5 HU
        self.theta=[thetainit]
        self.t=[0]
        self.dt=0.0001
        self.avelo=[0]           #角速度
    def calculate(self):
        while self.t[-1]<10:
            r=sqrt(self.x[-1]**2+self.y[-1]**2)
            vx=-4*pi**2*self.x[-1]/(r**3)
            vy=-4*pi**2*self.y[-1]/(r**3)
            avelo_new=(-12*(pi**2)*(self.x[-1]*sin(self.theta[-1])-self.y[-1]*cos(self.theta[-1]))*(self.x[-1]*cos(self.theta[-1])+self.y[-1]*sin(self.theta[-1])))/r**5
            self.vx.append(self.vx[-1]+vx*self.dt)
            self.vy.append(self.vy[-1]+vy*self.dt)
            self.avelo.append(self.avelo[-1]+avelo_new*self.dt)
            theta_new=self.theta[-1]+self.avelo[-1]*self.dt
            if theta_new>pi:
                theta_new-=2*pi
            elif theta_new<-pi:
                theta_new+=2*pi
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.theta.append(theta_new)
            self.t.append(self.t[-1]+self.dt)
    def plottheta(self,title='Hyperion'):
        pl.plot(self.t,self.theta)
        pl.xlabel('time(yr)')
        pl.ylabel('θ(radians)')
        pl.title(title)
        pl.show()
    def plotOmega(self,title='Hyperion'):
        pl.plot(self.t,self.avelo)
        pl.xlabel('time(yr)')
        pl.ylabel('ω(radians/yr)')
        pl.title(title)
        pl.show()
def dthe(theta1,theta2):
    dtheta=[]
    for i in range(len(theta1)):
        dtheta.append(abs(theta2[i]-theta1[i]))
    return dtheta

a=hyperion(0)
a.calculate()
b=hyperion(0.01)
b.calculate()

dtheta=dthe(a.theta,b.theta)
pl.plot(a.t,dtheta)
pl.semilogy(a.t,dtheta)
pl.xlabel('time(yr)')
pl.ylabel('Δθ(radians))')
pl.title('1')
pl.show()

#第二题：请参考ttps://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/Ex13/Exercise13.md