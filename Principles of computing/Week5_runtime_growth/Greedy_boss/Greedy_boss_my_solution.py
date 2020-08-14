
"""
Simulator for greedy boss scenario

"""

#import simpleplot
import math
#import codeskulptor
#codeskulptor.set_timeout(20)

STANDARD = True
LOGLOG = False

# constants for simulation
INITIAL_SALARY = 100
SALARY_INCREMENT = 100
INITIAL_BRIBE_COST = 1000

def greedy_boss(days_in_simulation, bribe_cost_increment,plot_type = STANDARD):
    """
    Simulation of greedy boss
    """

    # initialize necessary local variables
    salary = INITIAL_SALARY
    bribe_cost = INITIAL_BRIBE_COST
    earnings = 0
    current_day = 0
    accum_bribes = 0

    # define  list consisting of days vs. total salary earned for analysis
    days_vs_earnings = [(0,0)]

    # Each iteration of this while loop simulates one bribe (OR at least it should...check teacher solution)
    while current_day <= days_in_simulation:
        money_in_pocket = earnings - accum_bribes
        if money_in_pocket >= bribe_cost:
            if plot_type == STANDARD:
                days_vs_earnings.append((current_day, earnings))
            else:
                days_vs_earnings.append([math.log(current_day), math.log(earnings)])
            accum_bribes += bribe_cost
            bribe_cost += bribe_cost_increment
            salary += SALARY_INCREMENT
        else:
            current_day += 1
            earnings += salary
    return days_vs_earnings

def f(n):
    return math.exp(0.095*n)

def g(function, n):
    return([n,float(function(n)/(greedy_boss(100,0)[n])[1])])

def h(m):
    lst=[]
    for indx in range(1,m):
        lst.append(g(f,indx))
    return lst

print h(10)


def run_simulations():
    simpleplot.plot_lines('KRMS', 500,500, 'days', 'fraction',[h(50)])

# pops up a line plot

#run_simulations()

print greedy_boss(35, 100)
# should print [(0, 0), (10, 1000), (16, 2200), (20, 3400), (23, 4600), (26, 6100), (29, 7900), (31, 9300), (33, 10900), (35, 12700)]
#print ""
#print greedy_boss(35, 0)
# should print [(0, 0), (10, 1000), (15, 2000), (19, 3200), (21, 4000), (23, 5000), (25, 6200), (27, 7600), (28, 8400), (29, 9300), (30, 10300), (31, 11400), (32, 12600), (33, 13900), (34, 15300), (34, 15300), (35, 16900)]
#print ""
#print greedy_boss(50, 1000)
