
import matplotlib.pyplot as plt


def fib(num):
    global counter
    counter += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


def count_info(n):
    global counter
    num_calls = []
    fib_nums = []
    for num in range(n+1):
        counter = 0
        fib_num = fib(num)
        num_calls.append(counter)
        fib_nums.append(fib_num)
    return num_calls, fib_nums

def plot(n):
    x_vals = range(n+1)
    num_calls, fib_nums = count_info(n)
    plt.plot(x_vals, num_calls, label="num VS number of calls")
    plt.plot (x_vals, fib_nums, label = "num VS fib(num)")
    plt.plot(fib_nums, num_calls, label = "fib(num) VS number_of_calls")
    #plt.title("Number vs number of recursive calls to fibonacci")
    plt.legend()

    plt.show()

plot(8)


def memoized_fib(num, memo_dict):
    """
    The number of recursive calls to fib in the previous problem grows quite quickly. The issue is that fib
    fails to "remember" the values computed during previous recursive calls. One technique for avoiding this issue
    is memoization, a technique in which the values computed by calls to fib are stored in an auxiliary dictionary
    for later use.
    The Python function below uses memoization to compute the Fibonacci numbers efficiently
    """
    global counter2
    counter2 += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

calls = []
for num in range(1000):
    counter2 = 0
    fib_dict = {0: 0, 1:1}
    memoized_fib(num,fib_dict)
    calls.append(counter2)

#print calls
