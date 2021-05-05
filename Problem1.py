# Henry Song  |  MA375  |  Spring 2021
# Homework #7: Topic 6 - Differential Equations
# File: Problem1.py
# Dependencies: numpy, scipy, matplotlib
# Description: Performs calculations for homework #7 problem. 
#==========================================================================

import numpy as np
from scipy import integrate
from scipy import special
import matplotlib.pyplot as plt

# Plots function described in part A
def part_a():
    x = np.linspace(-1, 1, 100) # creates a range of x values
    f = lambda x: (2/np.sqrt(np.pi))*(np.e)**(-x**2)

    plt.title("Part A")
    plt.plot(x, f(x), 'ro', label='original')
    plt.show()

# Performs manual calculation of error function

def part_b():
    x = np.linspace(0.1, 1, 10) # creates a range of x values
    integral = lambda t: ((np.e)**(-t**2))  # integral part of the erf function
    f = (2/np.sqrt(np.pi))  #first half (non-integral part) of erf function

    results = []

    # loop first calculates the value of integral using scipy.integrate.quad(), then adds overall result to array after calculation
    for i in x:
        integrated = integrate.quad(integral, 0, i) #calculates integral part of function
        results.append(f*integrated[0])    # multiplies integral part by non-integral part, then adds result to array

    # trapz stuff
    xx = np.array([0,0.1])
    func = lambda t: (2/np.sqrt(np.pi))*((np.e)**(-t**2))
    temp = func(xx)
    trap_results = []
    for i in range(10):
        temp = func(xx)
        trap_results.append(integrate.trapz(temp, xx))
        xx[1] = xx[1]+0.1
    print(trap_results)
    # end trapz stuff

    print("x-value   Integrate Results    trapz Results")
    print("--------------------------------------------")
    for i in range(len(x)): print("%0.1f" % x[i], "     ", "%0.12f" % results[i], "     ", "%0.12f" % trap_results[i])
    return results

# Performs error function calculations using built in erf() method
def part_c(results):
    x = np.linspace(0.1, 1, 10) # creates a range of x values
    y = special.erf(x)  # calculates error function values using erf()
    print("x-value  |  Part C Results  |  Part B Results")
    print("---------------------------------------------")
    for i in range(len(x)): print("%0.1f" % x[i], "     | ", "%0.12f" % y[i], " | ", "%0.12f" % results[i])  #prints erf value for each x value


if __name__ == "__main__":
    print("Part A: Please see separate plot window")
    part_a()
    print()

    print("Part B: Manual erf function calculations")
    print("NOTE: values are rounded to 12 decimal places")
    part_b_results = part_b()
    print()

    print("Part C: SciPy erf function compared with manual calculations")
    print("NOTE: values are rounded to 12 decimal places")
    part_c(part_b_results)