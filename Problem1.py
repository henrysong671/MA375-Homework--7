import numpy as np
from scipy import integrate
from scipy import special
import matplotlib.pyplot as plt

def part_a():
    x = np.linspace(-1, 1, 100)
    f = lambda x: (2/np.sqrt(np.pi))*(np.e)**(-x**2)

    plt.title("Part A")
    plt.plot(x, f(x), 'ro', label='original')
    plt.show()

def part_b():
    # x = np.linspace(0.1, 1, 10)
    # func = lambda t: (np.e)**(-t**2)


    # f = (2/np.sqrt(np.pi))
    # print(f)

def part_c():
    x = np.linspace(0.1, 1, 10)
    y = special.erf(x)
    for i in range(len(x)):
        print("%0.1f" % x[i], ":", "%0.5f" % y[i])


if __name__ == "__main__":
    # print("Part A: Please see separate plot window")
    # part_a()
    # print()

    print("Part B:")
    part_b()
    print()

    print("Part C: ")
    part_c()