# coding:utf-8
# simple one
import numpy as np
from matplotlib import pyplot as plt

split=100.0

def amp(mental, emotion):
    #ampritude of output of emotion on face and so on
    k_m=1
    k_e=1
    print("amp:",k_m*mental+k_e*emotion)
    return k_m*mental+k_e*emotion

def x_a(mental):
    #time to reach ampritude max
    k_a=0.2
    print("x_a:",k_a*np.float_power(mental,-1))
    return k_a*np.float_power(mental,-1)

def x_s(mental):
    k_s=0.1
    print("x_s:",k_s*mental+x_a(mental))
    return k_s*mental+x_a(mental)

def delta_d(mental):
    k_d=-10
    print("delta_d:",k_d*np.float_power(mental,-1))
    return k_d*np.float_power(mental,-1)

def section(x,array,x_st,x_en):
    x_type = (x>=x_st)&(x<=x_en)
    y=array*(x_type.astype(np.int))
    return y

def attack(x,mental,emotion):
    y=amp(mental,emotion)/x_a(mental)*x
    return section(x,y,0,x_a(mental))

def sustain(x,mental,emotion):
    y=amp(mental,emotion)*np.ones_like(x)
    return section(x,y,x_a(mental),x_s(mental))

def decay(x,mental,emotion):
    y = delta_d(mental)*x+amp(mental,emotion)-delta_d(mental)*x_s(mental)
    return section(x,y,x_s(mental),1)


if __name__ == '__main__':
    mental = 4
    emotion = 10

    x=np.linspace(0,1,split)

    y_a=attack(x,mental,emotion)
    y_s=sustain(x,mental,emotion)
    y_d=decay(x,mental,emotion)

    plt.plot(x,(y_a+y_s+y_d)/20.0)
    plt.show()

