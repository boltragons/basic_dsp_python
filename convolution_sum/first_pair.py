# File: first_pair.py
# 
# Author: Pedro M. Botelho.
# Supervisor: André R. Braga.
# Institution: Federal University of Ceará.
# Registration: 471047.
# Subject: Signals and Systems.
#
# Description: This code implements the two signals
# of question 03 of the first test of the discipline,
# and obtains the resulting signal. 
# 
# At the end, it shows the three graphics on the
# screen and saves them in the images folder.
#  
# Date: Friday, February 11th, 2022.

# The libraries used in this code.
import numpy as np
from convolution import *

# The first input signal, given in the test. We'll
# take it for x[n]. This signal is 1 for n = -1 and 
# for n = 1 and is 2 for n = 0.
def inputSignal(n):
    return 1*unitImpulse(n + 1) + 2*unitImpulse(n) + 1*unitImpulse(n - 1) 

# The second input signal, given in the test. We'll
# take it for h[n]. This signal has a value of 1 from
# n = -3 to n = 3, except at n = 0, where the signal
# has a value of 2.
def responseSignal(n):
    return 1*unitImpulse(n + 3) + 1*unitImpulse(n + 2) + 1*unitImpulse(n + 1) + 2*unitImpulse(n) + 1*unitImpulse(n - 1) + 1*unitImpulse(n - 2) + 1*unitImpulse(n - 3)

# The domain of the signal.
n = np.arange(-10, 10)

# The output signal, resultant of the convolution
# between x and h in a n domain.
y = convolve(inputSignal, responseSignal, n)

# The input signal, applied to the values of the
# domain. 
x = inputSignal(n)

# The impulse response, applied to the values of
# the domain.
h = responseSignal(n)

# The signals will be plotted and saved in the
# informed files.
plotSignalAndSave(n, x, "$x[n]$ (Input Signal)", "images/first_pair_input.png")
plotSignalAndSave(n, h, "$h[n]$ (Response Signal)", "images/first_pair_response.png")
plotSignalAndSave(n, y, "$y[n]$ (Output Signal)", "images/first_pair_output.png")