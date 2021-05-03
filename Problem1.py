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
    # x = np.linspace(0.1, 1, 10) # creates a range of x values
    # func = lambda t: (np.e)**(-t**2)


    # f = (2/np.sqrt(np.pi))
    # print(f)
    return 1

# Performs error function calculations using built in erf() method
def part_c():
    x = np.linspace(0.1, 1, 10) # creates a range of x values
    y = special.erf(x)  # calculates error function values using erf()
    print("x-value   Part C Results   Part B Results")
    for i in range(len(x)): print("%0.1f" % x[i], "     ", "%0.5f" % y[i], "        ", "%0.5f" % y[i])  #prints erf value for each x value


if __name__ == "__main__":
    # print("Part A: Please see separate plot window")
    # part_a()
    # print()

    print("Part B:")
    part_b()
    print()

    print("Part C: ")
    print("*values are rounded to 5 decimal places")
    part_c()