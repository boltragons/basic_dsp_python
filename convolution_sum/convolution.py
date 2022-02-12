# File: convolution.py
# 
# Author: Pedro M. Botelho.
# Supervisor: André R. Braga.
# Institution: Federal University of Ceará.
# Registration: 471047.
# Subject: Signals and Systems.
#
# Description: This code implements several
# functions that plot discrete-time signals
# and perfom convolutions between two signals.
# 
# We will consider the first input signal as
# x[n], our usual input, and the second input
# signal as h[n], the impulse response.
#  
# Date: Friday, February 11th, 2022.

# The libraries used in this code.
import numpy as np
from pylab import *

# Inferior limit to k, in the convolution
# sum. Adjust it if your signal is abnormal.
INFERIOR_LIMIT = -100

# Superior limit to k, in the convolution
# sum. Adjust it if your signal is abnormal.
SUPERIOR_LIMIT = 100

# Returns a unit impulse, that is, a signal
# with value '1' in n = 0, and 0 in the rest
# of the domain.
def unitImpulse(n):
    return np.where(n == 0, 1, 0)

# Returns a unit step, that is, a signal
# with value '1' for n greater or equal than 0,
# and 0 in the rest of the domain.
def unitStep(n):
    return np.where(n >= 0, 1, 0)
# 
# The convolution, roughly speaking, is the sum of the
# responses scaled by the signal, in an interval. The
# range has been set to [-100, 100] but can be modified
# by changing the constants. 
def convolve(x, h, n):
    y = 0
    for k in range(INFERIOR_LIMIT, SUPERIOR_LIMIT):
        y += x(k)*h(n - k) 
    return y

# Plot the given signal, in the given domain, with the
# given title.
def plotSignal(domain, signal, title):
    fig = figure()
    fig.set_size_inches(16, 10)

    signalPlot = fig.add_subplot()
    signalPlot.set_title(title)
    signalPlot.set_xlabel("$n$ (Domain)")
    signalPlot.stem(domain, signal)
    show()

# Plot the given signal, in the given domain, with the
# given title and saves it in the given file path.
def plotSignalAndSave(domain, signal, title, fileName):
    fig = figure()
    fig.set_size_inches(16, 10)

    signalPlot = fig.add_subplot()
    signalPlot.set_title(title)
    signalPlot.set_xlabel("$n$ (Domain)")
    signalPlot.stem(domain, signal)
    fig.savefig(fileName, dpi=fig.dpi)
    show()