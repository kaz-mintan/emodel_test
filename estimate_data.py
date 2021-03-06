# coding:utf-8
import numpy as np
from matplotlib import pyplot as plt

class Attack:
    def a_mental(self, mental):
        return mental

    def amp(self, mental, emotion):
        return mental*emotion

    def attack(self, mental, emotion):
      
        x = np.linspace(0,1,100)
        #y = 1/(1+np.exp(-a_mental(mental)*x))
        y = self.amp(mental, emotion)/(1+np.exp((0.5-x)*self.a_mental(mental)))
        return y

class Decay:
    def __init__(self):
        self.st_x=10

    def a_mental(self, mental):
        if mental!=0:
            return 1.0/mental
        else:
            return 1#TODO

    def decay(self, mental, emotion):
        x = np.linspace(0,1,100)
        x_type = x>(self.st_x)/100.0
        y = -self.a_mental(mental)*x*x_type.astype(np.int)
        return y 


def test(a,b,c):
    x=np.linspace(0,1,100)
    x_type = x>c
    notx_type = np.logical_not(x_type)
    y=(-a*x+1+a*c)*(x_type.astype(np.int))+1*(notx_type.astype(np.int))
    return y

if __name__ == '__main__':
    test(4,2,0.3)


    x=np.linspace(0,1,100)
    func_a=Attack()
    y_a=func_a.attack(10,1)

    func_d=Decay()
    y_d=func_d.decay(10,1)

    y=y_a*y_d
    plt.plot(x,y)
    plt.show()
