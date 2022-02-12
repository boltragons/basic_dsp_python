# File: decomposition.py
# 
# Author: Pedro M. Botelho.
# Supervisor: André R. Braga.
# Institution: Federal University of Ceará.
# Registration: 471047.
# Subject: Signals and Systems.
#
# Description: This code implements several
# functions that plot discrete-time signals
# and perfom the decomposition of a signals
# in even and odd signals.
#  
# Date: Friday, February 11th, 2022.

# The libraries used in this code.
import numpy as np
from pylab import *

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

# Decompose the given signal in a even signal,
# using the given domain.
def decomposeEven(signal, n):
    return 0.5*(signal(n) + signal(-n))
     
# Decompose the given signal in a odd signal,
# using the given domain.    
def decomposeOdd(signal, n):
    return 0.5*(signal(n) - signal(-n))

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