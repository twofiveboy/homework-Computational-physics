import numpy as np
from matplotlib import pylab as pl
from math import *
#write by Chen Yinan
class cannon :         
    def __init__(self,theta=45,v_init=100,x_init=0,y_init=0,dt=0.01):  #theta shoule be degrees(角度) rather than randians（弧度）
        self.dt=dt
        self.v_inti=v_init
        self.theta=theta
        self.theta_r=radians(theta)                                    #translate degree into randian
        self.vx=v_init*cos(self.theta_r)
        self.vy=v_init*sin(self.theta_r)
        self.B_m=4e-5                                                  #B_m=B2/M                  
        self.x=[x_init]
        self.y=[y_init]
        self.x_init=x_init
        self.y_init=y_init
        self.t=[0]
    def calculate_noDrag(self):                 #无空气阻力的计算模块
        for i in range(1,100000000):
            tmpx=self.x[i-1]+self.vx*self.dt
            tmpy=self.y[i-1]+self.vy*self.dt
            self.x.append(tmpx)
            self.y.append(tmpy)
            self.vy-=(9.8*self.dt)
            self.t.append(self.t[i-1]+self.dt)
            if self.y[i]<0 :
                j=i
                break
        a=-self.y[j]/self.y[j-1]
        self.x[j]=(self.x[j]+a*self.x[j-1])/(1+a)
        self.y[j]=0
        return
    def calculate_WithDrag(self):                 #有空气阻力的计算模块（用于计算落地轨迹）
        vx=self.vx
        vy=self.vy
        B_m=self.B_m
        for i in range(1,100000000):
            tmpx=self.x[i-1]+vx*self.dt
            tmpy=self.y[i-1]+vy*self.dt
            self.x.append(tmpx)
            self.y.append(tmpy)
            c=1-(6.5e-3)*self.y[i]/293
            a=pow(c,2.5)                       # 20℃-> 293K=20+273     
            f=a*B_m*sqrt(vx**2+vy**2)
            vx=vx-f*vx*self.dt
            vy=vy-(9.8*self.dt)-f*vy*self.dt
            self.t.append(self.t[i-1]+self.dt)
            if self.y[i]<0 :
                j=i
                break
        b=-self.y[j]/self.y[j-1]
        self.x[j]=(self.x[j]+b*self.x[j-1])/(1+b)
        self.y[j]=0
    def calculate_WithDrag2(self,targetX,targetY):   #有空气阻力的计算模块2（用于计算炮击，不用手动调用）
        vx=self.vx
        vy=self.vy
        B_m=self.B_m
        for i in range(1,100000000):
            tmpx=self.x[i-1]+vx*self.dt
            tmpy=self.y[i-1]+vy*self.dt
            self.x.append(tmpx)
            self.y.append(tmpy)
            c=1-(6.5e-3)*self.y[i]/293
            a=pow(c,2.5)                       # 20℃-> 293K=20+273     
            f=a*B_m*sqrt(vx**2+vy**2)
            vx=vx-f*vx*self.dt
            vy=vy-(9.8*self.dt)-f*vy*self.dt
            self.t.append(self.t[i-1]+self.dt)
            #if (self.y[i]<self.y_init and self.y[i]<targetY) :
            #    break
            if targetY>self.y_init and (self.x[i]>0.6*targetX and self.y[i]<targetY) :
                break
            elif targetY<=self.y_init and self.y[i]<targetY:
                break
       

        
    def getPosition(self):                   
        return [self.x[-1],self.y[-1]]
    def showResults(self,style='g',label1='??'):       #style=风格，label=图例
        pl.plot(self.x,self.y,style,label=label1)                                      
        pl.xlabel('x/m')
        pl.ylabel('y/m')
        pl.xlim(0,51000)
        pl.ylim(0,20000)                                                                                                                             

def kaipao(targetX,targetY):                    #使用建议：炮击点选择（10000，200），由于程序本身问题，其他炮击点需要自己手动调试，如果有任何问题请联系作者
    theta=45                       
    error=5
    v=360
    for i in range (10000):
        v+=0.1
        a=cannon(theta,v)
        a.calculate_WithDrag2(targetX,targetY)
        b=a.getPosition()
        if (abs(b[0]-targetX)<error) and  (abs(b[1]-targetY)<error):
            break
    vmin=v
    thetamin=theta
    position=b
    error=5
    for i in range(0,200):
        theta-=0.1
        a=cannon(theta,v)
        a.calculate_WithDrag2(targetX,targetY)
        b=a.getPosition()
        if b[0]>targetX+error :      #and b[1]>targetY+error:
            v-=0.1
        elif b[0]<targetX-error :    #and b[1]<targetY-error:
            v+=0.1
        if v<vmin:
           vmin=v
           thetamin=theta
           position=b
           c=a
    c.showResults('--b','')
    print("最小速度：",vmin)
    print("此时的发射角:",thetamin)
    print("落地位置：",position)

#示例1，第一项参数=角度，第二项=速度，可自由调整
a=cannon(30,700)
a.calculate_noDrag()
a.showResults('b','theta=30°')
b=cannon(35,700)
b.calculate_noDrag()
b.showResults('--','theta=35°')
c=cannon(40,700)
c.calculate_noDrag()
c.showResults('-.','theta=40°')
d=cannon(45,700)
d.calculate_noDrag()
d.showResults(':','theta=45°')
e=cannon(50,700)
e.calculate_noDrag()
e.showResults('-y','theta=50°')
f=cannon(55,700)
f.calculate_noDrag()
f.showResults('--r','theta=55°')

pl.legend(loc='upper right')
pl.show()
#有空气阻力情况把 no改为With即可
#炮击示例
kaipao(10000,200)
pl.xlim(0,10000)
pl.ylim(0,4000)
pl.show()










 
