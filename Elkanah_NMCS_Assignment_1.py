#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 08:42:56 2020

@author: aimsg
"""
#[s0+v0*t+0.5*a0*t**2+a0*t*(t-t1)]
import numpy as np
import matplotlib.pyplot as plt
rho=1.2e-2;h=8.3;c=1000;a=0.3;S0=1367;epsilon=0.6;sigma=5.67e-8#costants given
'''Exact Solution'''
Eq_T=(((1-a)*S0)/(4*epsilon*sigma))**(1/4)#Equilibrium temperature
constant=(-4*epsilon*sigma*(Eq_T**3))/(rho*c*h)
t=np.arange(0.0,500.0,14)
Temp=[]#Create an empty list T
for i in t:
    Temp.append(10*np.exp(constant*i)+Eq_T) #For every value of t, compute the exact solution of the equation and append it to Temp
    
    
'''APPROXIMATE SOLUTION '''
T=[300.0] #create a list yo
def f(t,y):
    return ((1.0-a)*S0-4.0*epsilon*sigma*(y**4.0))/(4.0*h*rho*c)
for j in t[:-1]: 
    K1=f(j,T[-1]) #calculate the value of K1 as solved in the assignment
    K2=f(j+0.75*14,T[-1]+0.75*14*K1)#calculates the value of k2
    #print(K1,K2)
    T.append(T[-1]+(1/3)*14*(K1+2*K2)) #using the initial temp, it calucaltes fot T_n+1 for each value of t
    
plt.plot(t,Temp,label="Exact") #plots the exact soluton  
plt.plot(t,T,label="Approx")  #Plots the approximate solution
plt.ylabel("Temperature")
plt.xlabel("time")
plt.title("Exact and Approximate solutions for the conservation of energy\n")
plt.legend()
plt.grid()
plt.savefig('graph.png')
