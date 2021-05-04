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
# 0-0.1, 0-0.2, 0-0.3 ... 0-1
def part_b():
    x = np.linspace(0.1, 1, 10) # creates a range of x values
    integral = lambda t: ((np.e)**(-t**2))  # only the integral part of the erf function
    f = (2/np.sqrt(np.pi))

    results = []
    for i in x:
        integrated = integrate.quad(integral, 0, i) #calculates integral part of function
        results.append(f*integrated[0])    # multiplies integral part by 2/sqrt(pi), then adds result to array
    
    print("x-value   Results")
    for i in range(len(x)): print("%0.1f" % x[i], "     ", "%0.8f" % results[i])
    return results

# Performs error function calculations using built in erf() method
def part_c(results):
    x = np.linspace(0.1, 1, 10) # creates a range of x values
    y = special.erf(x)  # calculates error function values using erf()
    print("x-value   Part C Results   Part B Results")
    for i in range(len(x)): print("%0.1f" % x[i], "     ", "%0.8f" % y[i], "     ", "%0.8f" % results[i])  #prints erf value for each x value


if __name__ == "__main__":
    print("Part A: Please see separate plot window")
    part_a()
    print()

    print("Part B:")
    print("NOTE: values are rounded to 8 decimal places")
    part_b_results = part_b()
    print()

    print("Part C: ")
    print("NOTE: values are rounded to 8 decimal places")
    part_c(part_b_results)