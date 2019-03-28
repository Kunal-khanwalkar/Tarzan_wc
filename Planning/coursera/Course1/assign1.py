#!/usr/bin/env python

# from notebook_grader import BicycleSolution, grade_bicycle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math

class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

        
        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        
        self.sample_time = 0.01
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

    def step(self,v,w):
        
        self.delta = self.delta + (w*0.01)
        # self.beta =  math.atan((self.lr*math.tan(self.delta))/self.L)
        # print (self.beta)
        self.theta = self.theta + (v*0.01*math.cos(self.beta)*math.tan(self.delta))/self.L
        self.yc = self.yc + v*0.01*math.sin(self.theta + self.beta)
        self.xc = self.xc + v*0.01*math.cos(self.theta + self.beta)
def sqrrt(x , y):
    z = math.pow(x,2) + math.pow(y,2)
    return math.pow(z,0.5)

if __name__ == "__main__":
    sample_time = 0.01
    time_end = 30
    model = Bicycle()
    model.delta = np.arctan(0.25)
    print (model.delta)
    t_data = np.arange(0,time_end,sample_time)
    x_data = np.zeros_like(t_data)
    y_data = np.zeros_like(t_data)
    v_data = np.zeros_like(t_data)
    w_data = np.zeros_like(t_data)
    j = 0
    for i in range(1666):
 
        x_data[i] = model.xc
        x = model.xc
        y_data[i] = model.yc
        y = model.yc
        v_data[i] = sqrrt(x, y)
        if(i==0):
            w_data[i] = 0
        else:
            w_data[i] = model.delta/i
        # model.beta = 0.0
        model.step(6*np.pi/5,0)
        # j = i
    
    # model.reset()
    model.delta = np.arctan(-0.25)
    print (model.delta)
    for i in range(1666,len(t_data)):
        x_data[i] = model.xc
        y_data[i] = model.yc
        v_data[i] = sqrrt(x, y)
        if(i==0):
            w_data[i] = 0
        else:
            w_data[i] = model.delta/i
        model.step(6*np.pi/5,0)
        
    plt.axis('equal')
    plt.plot(x_data, y_data,label='Learner Model')
    plt.legend()
    plt.show()
