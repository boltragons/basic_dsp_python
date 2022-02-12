# File: third_signal.py
# 
# Author: Pedro M. Botelho.
# Supervisor: André R. Braga.
# Institution: Federal University of Ceará.
# Registration: 471047.
# Subject: Signals and Systems.
#
# Description: This code implements the signal from
# qestion 1.24c, of Alan Oppenheim's book, "Signals
# and Systems", 2nd edition, and obtains it's
# even and odd signals, making the decomposition
# and the composition. 
# 
# At the end, it shows the three graphics on the
# screen and saves them in the images folder.
#  
# Date: Friday, February 11th, 2022.

# The libraries used in this code.
import numpy as np
from decomposition import *

# The input signal, being -1 for n = -4 and n = 3,
# 1 for n = -1, n = 0 and n = 2, and 2 for n = -3,
# n = -2 and n = 1..
def inputSignal(n):
    return (-1)*unitImpulse(n + 4) + 2*unitImpulse(n + 3) + 2*unitImpulse(n + 2) + 1*unitImpulse(n + 1)  + 1*unitImpulse(n) + 2*unitImpulse(n - 1) + 1*unitImpulse(n - 2) -  1*unitImpulse(n - 3)

# The domain of the signal.
n = np.arange(-5, 9)

# The three output signals, resultant of the
# decomposition and recomposition of the
# input signal.
evenSignal = decomposeEven(inputSignal, n)
oddSignal = decomposeOdd(inputSignal, n)
signalSum = evenSignal + oddSignal

# The signals will be plotted and saved in the
# informed files.
plotSignalAndSave(n, inputSignal(n), "$x[n]$ (Input Signal)", "images/third_signal_input.png")
plotSignalAndSave(n, evenSignal, "$Ev\{y[n]\}$ (Even part of the Input Signal)", "images/third_signal_even.png")
plotSignalAndSave(n, oddSignal, "$Od\{y[n]\}$ (Odd part of the Input Signal)", "images/third_signal_odd.png")
plotSignalAndSave(n, signalSum, "$Ev\{y[n]\} + Od\{y[n]\}$ (Sum of the parts of the Input Signal)", "images/third_signal_sum.png")