# File: second_pair.py
# 
# Author: Pedro M. Botelho.
# Supervisor: André R. Braga.
# Institution: Federal University of Ceará.
# Registration: 471047.
# Subject: Signals and Systems.
#
# Description: This code implements the two signals
# of example 2.1 of Alan Oppenheim's book, "Signals
# and Systems", 2nd edition, and obtains it's
# resultant output signal.
# 
# At the end, it shows the three graphics on the
# screen and saves them in the images folder.
#  
# Date: Friday, February 11th, 2022.

# The libraries used in this code.
import numpy as np
from convolution import *

# The first input signal, x[n]. This signal has a
# value of 0.5 for n = 0 and a value of 2 for n = 1.
def inputSignal(n):
    return 0.5*unitImpulse(n) + 2*unitImpulse(n - 1)

# The second input signal, h[n]. This signal has a
# value of 1, from n = 0 to n = 2.
def responseSignal(n):
    return 1*unitImpulse(n) + 1*unitImpulse(n - 1) + 1*unitImpulse(n - 2) 

# The domain of the signal.
n = np.arange(-3, 5)

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
plotSignalAndSave(n, x, "$x[n]$ (Input Signal)", "images/second_pair_input.png")
plotSignalAndSave(n, h, "$h[n]$ (Response Signal)", "images/second_pair_response.png")
plotSignalAndSave(n, y, "$y[n]$ (Output Signal)", "images/second_pair_output.png")