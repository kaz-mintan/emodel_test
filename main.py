# coding:utf-8
# simple one
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from func_h import *



#[emotion, mental]
load_data=np.loadtxt("emotion_mental_data.csv", delimiter=",")
split_data=np.loadtxt("width_data.csv",delimiter=",")

x=np.linspace(0,1,int(np.sum(split_data.flatten())))

b=np.array([])
for i in range(load_data.shape[0]):
    print("load_data", load_data[i,:])
    b=np.append(b,estimated_s(split_data[i], load_data[i,:]))

fig = plt.figure()
plt.plot(x,b)
plt.savefig("test_output.png")

np.savetxt("test_output.csv",b,delimiter=",")
