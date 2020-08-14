
"""
Plot solutions to common recurrences
Note that lambda is a Python way of making functions 'on the fly'
f.eks.
g = lambda x: x**2
print g(8) -> 64

"""

import math
import matplotlib.pyplot as plt


# select index of recurrence for analysis
INDEX = 5


# dictionary of right hand sides for recurrences
LHS_DICT = {0 : lambda n : recur(n - 1) + 1,
            1 : lambda n : recur(n - 1) + n,
            2 : lambda n : 2 * recur(n - 1),
            3 : lambda n : n * recur(n - 1),
            4 : lambda n : recur(n / 2) + 1,
            5 : lambda n : recur(n / 2) + n,
            6 : lambda n : 2 * recur(n / 2),
            7 : lambda n : 2 * recur(n / 2) + 1,
            8 : lambda n : 2 * recur(n / 2) + n}

def recur(num):
    """
    Common recurrences, always make sure that recursive
    calls involve smaller integer values
    """
    if num == 1:
        return 1
    # Lookup righthand side of the recurrence using dictionary
    rhs = LHS_DICT[INDEX]
    return rhs(num)



# Dictionary of solution
# These functions are upper bounds for the recurrence
SOL_DICT = {0 : lambda n : n,
            1 : lambda n : 0.5 * n * (n + 1),
            2 : lambda n : 2 ** (n - 1),
            3 : lambda n : math.factorial(n),
            4 : lambda n : math.log(n, 2) + 1,
            5 : lambda n : 2 * n - 1,
            6 : lambda n : n,
            7 : lambda n : 2 * n - 1,
            8 : lambda n : n * (math.log(n, 2) + 1)}


def plot_example(length):
    """
    Plot computed solutions to recurrences
    """
    x_vals = range(2,length)
    rec_plot_y = []
    sol_plot_y = []

    sol = SOL_DICT[INDEX]
    for num in range(2, length):
        rec_plot_y.append([recur(num)])
        sol_plot_y.append([sol(num)])

    plt.plot(x_vals, rec_plot_y, label = "Recurrence")
    plt.plot(x_vals, sol_plot_y, label = "Solution (upper bound)")
    plt.xlabel('x values')
    plt.ylabel('y values')

    plt.title("Recurrence Vs Solution #"+str(INDEX) )
    plt.legend()
    plt.show()

plot_example(130)
