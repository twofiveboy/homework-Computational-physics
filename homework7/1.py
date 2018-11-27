import matplotlib.pyplot as pl
from math import *
import numpy as np
# this function gives trac
class trac():
    def __init__(self,vy=2*pi,beta=2):
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.vy=[vy]
        self.t=[0]
        self.dt=0.02
        self.beta=beta
    def calculate(self):
        beta=self.beta
        while self.t[-1]<20:
            r=sqrt(self.x[-1]**2+self.y[-1]**2)
            vx=-4*pi**2*self.x[-1]/(r**(self.beta+1))
            vy=-4*pi**2*self.y[-1]/(r**(self.beta+1))
            self.vx.append(self.vx[-1]+vx*self.dt)
            self.vy.append(self.vy[-1]+vy*self.dt)
            self.x.append(self.x[-1]+self.vx[-1]*self.dt)
            self.y.append(self.y[-1]+self.vy[-1]*self.dt)
            self.t.append(self.t[-1]+self.dt)
    def plot(self,title):
        fig=pl.figure(figsize=[8,8]) 
        pl.plot(self.x,self.y)
        pl.scatter([0],[0],s=1000,color='yellow')
        pl.xlabel('x(AU)')
        pl.ylabel('y(AU)')
        pl.title('')
        pl.show()

a=trac()
a.calculate()
a.plot('beta=2.1,vy0=2.5pi')
