#!/usr/bin/env python
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
class Vehicle():
    def __init__(self):
 
        #Throttle to engine torque
        self.a_0 = 400
        self.a_1 = 0.1
        self.a_2 = -0.0002
        
        # Gear ratio, effective radius, mass + inertia
        self.GR = 0.35
        self.r_e = 0.3
        self.J_e = 10
        self.m = 2000
        self.g = 9.81
        
        # Aerodynamic and friction coefficients
        self.c_a = 1.36
        self.c_r1 = 0.01
        
        # Tire force 
        self.c = 10000
        self.F_max = 10000
        
        # State variables
        self.x = 0
        self.v = 5
        self.a = 0
        self.w_e = 100
        self.w_e_dot = 0
        
        self.sample_time = 0.01
        
    def reset(self):
        # reset state variables
        self.x = 0
        self.v = 5
        self.a = 0
        self.w_e = 100
        self.w_e_dot = 0

    def step(self, throttle, alpha):
        # self.w_e = 
        # self.v = self.v + self.a*0.01
        # self.x = self.x + self.v*0.01
        self.w_e = self.w_e + self.w_e_dot*0.01
        self.v = self.v + self.a*0.01
        self.x = self.x + self.v*0.01
        F_a = self.c_a*pow(self.v,2)
        F_g = self.m*self.g*(alpha) #no sin
        R_x = self.c_r1*self.v
        F_load = F_a + F_g + R_x
       
        T_e = throttle*(self.a_0 + self.a_1*self.w_e + self.a_2*math.pow(self.w_e,2))
        self.w_e_dot = (T_e - self.GR*self.r_e*F_load)/self.J_e
       
        w_w = self.GR*self.w_e
        s = (w_w*self.r_e - self.v)/self.v
       
        if (abs(s)<1):
            F_x = self.c*s
        else:
            F_x = self.F_max
       
        self.a = (F_x - F_load)/self.m
        

        pass

if __name__ == "__main__":
    sample_time = 0.01
    time_end = 20
    model = Vehicle()

    t_data = np.arange(0,time_end,sample_time)
    v_data = np.zeros_like(t_data)
    x_data = np.zeros_like(t_data)
    throttle_data = np.zeros_like(t_data)
    al_data = np.zeros_like(t_data)
    # throttle percentage between 0 and 1
    throttle = 0.2
    # x_d
    # incline angle (in radians)
    alpha = 0
    throttle_data[0]= 0.2
    x_data[0] = 0
    al_data[0]=math.atan(0.05)
    for i in range(2000):

        if (i>0 and i<=500):

            throttle_data[i] = (i*0.06*0.01) + 0.2
            alpha = math.atan(0.05)
            al_data[i] = alpha
            v_data[i] = model.v
            x_data[i] = (model.v * 0.01) + x_data[i-1]
            model.step(throttle_data[i], al_data[i])
        elif (i>500 and i<=1500):
            throttle = throttle_data[i] = 0.5
            alpha = math.atan(0.05)
            if (i >= 676):
                alpha = math.atan(0.1)
            al_data[i] = alpha
            v_data[i] = model.v
            x_data[i] = (model.v * 0.01) + x_data[i-1]
            model.step(throttle, alpha)
        elif (i>=1500 and i<=2000):
            alpha = 0.1
            if (i>=1512):
                alpha = 0
            al_data[i] = alpha
            v_data[i] = model.v
            x_data[i] = (model.v * 0.01) + x_data[i-1]
            throttle_data[i] =  (-0.1 * i *0.01) + 2
            model.step(throttle_data[i], al_data[i])
    plt.plot(t_data, v_data)
    plt.show()
    # plt.axis('equal')
    plt.plot(t_data, throttle_data,label='Learner Model')
    plt.legend()
    plt.show()