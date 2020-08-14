"""
A simple recursive solver for Nim
http://en.wikipedia.org/wiki/Nim#The_21_game
"""


MAX_REMOVE = 3

# recursive solver with no memoization
counter = 0

def evaluate_position(current_num):
    """
    Recursive solver for Nim
    My solution
    """
    global counter
    counter += 1

    #base case
    if current_num == 0:
        return "lost"
    #if there is a move that leads to your opponent losing, you have won
    for choice in range(1, min(current_num + 1, MAX_REMOVE + 1)):
        if evaluate_position(current_num - choice) == "lost":
            return "won"
    # if there is no such move (i.e. if all of my choices leads to my opponent winning) I have lost
    return "lost"
#
# def evaluate_position(current_num):
#     """
#     Recursive solver for Nim
#     Teacher solution
#     """
#     global counter
#     #counter += 1
#     for removed_num in range(1, min(MAX_REMOVE + 1, current_num + 1)):
#         new_num = current_num - removed_num
#         if evaluate_position(new_num) == "lost":
#             return "won"
#     return "lost"

#

def run_standard(items):
    """
    Encapsulate code to run regular recursive solver
    """
    global counter
    counter = 0
    print
    print "Standard recursive version"
    print "Position with", items, "items is", evaluate_position(items)
    print "Evaluated in", counter, "calls"

#run_standard(21)

    # memoized version with dictionary
def evaluate_memo_position(current_num, memo_dict):
    """
    Memoized version of evaluate_position
    memo_dict is a dictionary that stores previously computed results
    """
    global counter
    counter += 1

    if current_num in memo_dict:
        return memo_dict[current_num]
    else:
        #if there is a move that leads to your opponent losing, you have won
        for choice in range(1, min(current_num + 1, MAX_REMOVE + 1)):
            if evaluate_memo_position(current_num - choice, memo_dict) == "lost":
               memo_dict[current_num - choice] = "lost"
               memo_dict[current_num] = "won"
               return "won"
        # if there is no such move (i.e. if all of my choices leads to my opponent winning) I have lost
        memo_dict[current_num] = "lost"
        return "lost"

def run_memoized(items):
    """
    Run the memoized version of the solver
    """
    global counter
    counter = 0
    print
    print "Memoized version"
    print "Position with", items, "items is", evaluate_memo_position(items, {0 : "lost"})
    print "Evaluated in", counter, "calls"

run_memoized(500)
