# File: third_pair.py
# 
# Author: Pedro M. Botelho.
# Supervisor: André R. Braga.
# Institution: Federal University of Ceará.
# Registration: 471047.
# Subject: Signals and Systems.
#
# Description: This code implements the two signals
# of example 2.3 of Alan Oppenheim's book, "Signals
# and Systems", 2nd edition, and obtains it's
# resultant output signal.
# 
# At the end, it shows the three graphics on the
# screen and saves them in the images folder.
# 
# Note that the input signal x[n] -> 0 with
# n -> IFNTY, and that the output sinal
# y[n] -> (1)/(1 - ALPHA). With A equals to
# 0.95 we have that y[n] -> 20, as we can
# see in the plot.
#  
# Date: Friday, February 11th, 2022.

# The libraries used in this code.
import numpy as np
from convolution import *

# The constant alpha in the input signal.
ALPHA = 0.95

# The first input signal, x[n]. This signal is
# defined by (APLHA^n)(u[n]). Hence, it's ALPHA^n
# for n greater or equal than n, and 0 otherwhise.
def inputSignal(n):
    return (ALPHA**n)*unitStep(n)

# The second input signal, h[n]. This signal is
# defined by a simple unit step.
def responseSignal(n):
    return 1*unitStep(n)

# The domain of the signal.
n = np.arange(-10, 100)

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
plotSignalAndSave(n, x, "$x[n]$ (Input Signal)", "images/third_pair_input.png")
plotSignalAndSave(n, h, "$h[n]$ (Response Signal)", "images/third_pair_response.png")
plotSignalAndSave(n, y, "$y[n]$ (Output Signal)", "images/third_pair_output.png")