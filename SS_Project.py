# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 19:24:17 2019

@author: anshu
"""
""" This code is presented to Prof. Dr. Hilmi Dajani for partial fulfillment of the requirements for the course ELG7172/EACJ [W]– Topics in Signal Processing I. """

import numpy as np
import matplotlib.pyplot as plt
from math import pi
from scipy import random

plt.close('all')

"""Generating a Small subthreshold signal (Sine Wave)""" 

A=2                                    # amplitude
f=50                                   # frequency
T=1/f                                  #time period
fs=100*f                               #sampling freq
Ts=1/fs   
cycles=5

t=np.arange(0,cycles*T,Ts)                    #defining t
signal = A*np.sin(2*pi*f*t)                   #defining the signal

plt.subplot(2,1,1)
plt.plot(signal)                              #plotting the signal
plt.title('Sine wave / Subthreshold signal')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
plt.grid(True)
plt.show()

signal_power = signal**2
signal_power_db = 10*np.log10(signal_power)


""" Generating a system with a threshold """

detected_signal = np.zeros(500,np.int16)
detected_signal_amp = np.zeros(500,np.int16)
for i in range(500):
    if (signal[i] >  2.5):
        detected_signal[i]=1;
        detected_signal_amp[i]=output[i]-2.5
plt.subplot(2,1,1)
plt.plot(detected_signal, 'red')
plt.title('System output')
plt.xlabel('Input signal')
plt.ylabel('Output')
plt.grid(True)
plt.show()


"""Generating random White Gaussian Noise, adding with the noise and then using it as an input to our system"""   

"""1st noise level"""

noise_power = 1.5
mean=0
noise = np.random.normal(mean, np.sqrt(noise_power), len(signal_power)) 
plt.plot(noise)
plt.title('White Gaussian Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
plt.grid(True)
plt.show()


output = signal + noise
plt.subplot(2,1,1)
plt.plot(output, 'orange')
plt.title('Output Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
ax = plt.gca()
ax.set_yticks(np.arange(-5, 5.1, 2.5))
plt.grid(True)
plt.show()

output_power = output**2
output_power_db= 10* np.log10(output_power)

detected_signal = np.zeros(500,np.int16)
detected_signal_amp = np.zeros(500,np.int16)
for i in range(500):
    if (output[i] >  2.5):
        detected_signal[i]=1;
        detected_signal_amp[i]=output[i]-2.5
plt.subplot(2,1,1)
plt.plot(detected_signal, 'red')
plt.title('System output')
plt.xlabel('Input signal')
plt.ylabel('Output')
plt.grid(True)
plt.show()



"""2nd noise level"""

noise_power = 2
mean=0
noise = np.random.normal(mean, np.sqrt(noise_power), len(signal_power)) 
plt.plot(noise)
plt.title('White Gaussian Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
plt.grid(True)
plt.show()

output = signal + noise
plt.subplot(2,1,1)
plt.plot(output, 'orange')
plt.title('Output Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
ax = plt.gca()
ax.set_yticks(np.arange(-5, 5.1, 2.5))
plt.grid(True)
plt.show()

output_power = output**2
output_power_db= 10* np.log10(output_power)

detected_signal = np.zeros(500,np.int16)
detected_signal_amp = np.zeros(500,np.int16)
for i in range(500):
    if (output[i] >  2.5):
        detected_signal[i]=1;
        detected_signal_amp[i]=output[i]-2.5
plt.subplot(2,1,1)
plt.plot(detected_signal, 'red')
plt.title('System output')
plt.xlabel('Input signal')
plt.ylabel('Output')
plt.grid(True)
plt.show()


"""3rd noise level"""

noise_power = 3
mean=0
noise = np.random.normal(mean, np.sqrt(noise_power), len(signal_power)) 
plt.plot(noise)
plt.title('White Gaussian Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
plt.grid(True)
plt.show()

output = signal + noise
plt.subplot(2,1,1)
plt.plot(output, 'orange')
plt.title('Output Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
ax = plt.gca()
ax.set_yticks(np.arange(-5, 5.1, 2.5))
plt.grid(True)
plt.show()

output_power = output**2
output_power_db= 10* np.log10(output_power)

detected_signal = np.zeros(500,np.int16)
detected_signal_amp = np.zeros(500,np.int16)
for i in range(500):
    if (output[i] >  2.5):
        detected_signal[i]=1;
        detected_signal_amp[i]=output[i]-2.5
plt.subplot(2,1,1)
plt.plot(detected_signal, 'red')
plt.title('System output')
plt.xlabel('Input signal')
plt.ylabel('Output')
plt.grid(True)
plt.show()


"""4th noise level"""

noise_power = 4
mean=0
noise = np.random.normal(mean, np.sqrt(noise_power), len(signal_power)) 
plt.plot(noise)
plt.title('White Gaussian Noise')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
plt.grid(True)
plt.show()

output = signal + noise
plt.subplot(2,1,1)
plt.plot(output, 'orange')
plt.title('Output Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amp (v)')
ax = plt.gca()
ax.set_yticks(np.arange(-5, 5.1, 2.5))
plt.grid(True)
plt.show()

output_power = output**2
output_power_db= 10* np.log10(output_power)

detected_signal = np.zeros(500,np.int16)
detected_signal_amp = np.zeros(500,np.int16)
for i in range(500):
    if (output[i] >  2.5):
        detected_signal[i]=1;
        detected_signal_amp[i]=output[i]-2.5
plt.subplot(2,1,1)
plt.plot(detected_signal, 'red')
plt.title('System output')
plt.xlabel('Input signal')
plt.ylabel('Output')
plt.grid(True)
plt.show()



""" Generating 200 noise levels and adding to subthreshold signal to use as an input to our system and then find relevant plot of SNR """


noise_power = 1
snr_array=np.zeros(200)
noise_power_array=np.zeros(200)
for j in range (200):
    noise_power_array[j]=noise_power;
    mean=0
    noise = np.random.normal(mean, np.sqrt(noise_power), len(signal_power)) 
    
    output = signal + noise
    output_power = output**2
    output_power_db= 10* np.log10(output_power)
    
    detected_signal = np.zeros(500,np.int16)
    detected_signal_amp = np.zeros(500,np.int16)
    for i in range(500):
        if (output[i] >  2.5):
            detected_signal[i]=1;
            detected_signal_amp[i]=output[i]-2.5

    detected_signal_power=detected_signal**2;    
    avg_noise_power = np.mean(noise_power)
    avg_detected_signal_power = np.mean(detected_signal_power)
    snr_detected=avg_detected_signal_power / avg_noise_power
    snr_detected_db = 10* np.log10(snr_detected)
    snr_array[j]=snr_detected_db;
    print('SNR for this detected signal =' , snr_detected_db)
    noise_power=noise_power+.01;
plt.plot(noise_power_array,snr_array, 'black')
plt.title('SNR vs Noise')
plt.xlabel('Increasing Noise')
plt.ylabel('SNR (db)')
plt.show()

""" End of code """

