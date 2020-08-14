"""
THE RNA SECONDARY STRUCTURE PROBLEM
My own recursice and dynamic programming implementation of "RNA pairing" (i.g. get the maximal number og pairings and the parings-positoins
of a given RNA string)

RNA string consists og U, C, G, A, eg. "UCGAAACCCAA"
Rules for pairing:
1. No cross-pairings!
2. If (i, j) is a pair, then i< j-4
3. A can pair with U, G can pair with C.
4. No element appears in more than one pair

"""

def pairings_of_last(string, i, j):
    """
    Takes a string and indexes i, j.
    Returns lists of all t's in [i, ... j-5], where string[i], string[j] is a legal pair
    """
    possible_t = []

    last = string[j]
    focus = range(i, j - 4)

    if last == "A":
        for index in focus:
            if string[index] == "U":
                possible_t.append(index)

    if last == "U":
        for index in focus:
            if string[index] == "A":
                possible_t.append(index)

    if last == "C":
        for index in focus:
            if string[index] == "G":
                possible_t.append(index)

    if last == "G":
        for index in focus:
            if string[index] == "C":
                possible_t.append(index)
    return possible_t


def opt(i,j, original_string):
    """
    First call(0, len(original_string), original_string)
    Recursive solution.
    Returns maximal number of pairings in RNA string, between position i and position j in the string.
    Has not been seriously tested.
    THIS VERSION RETURNS POSITION OF PAIRS
    """

    if j - i < 5:
        return []

    # if last letter is NOT part of a solution-pair:
    ans_if_last_is_not_part_of_solution = opt(i, j - 1, original_string)

    # if last letter IS part of a solution-pair:
    possible_t = pairings_of_last(original_string, i, j-1)

    if len(possible_t) > 0:
        most_pairs = []

        for t in possible_t:
            first_part = opt(i, t, original_string)
            second_part = opt(t + 1, j - 1, original_string)
            new_pairs = first_part + second_part + [(t, j-1)]
            if len(new_pairs) > len(most_pairs):
                most_pairs = new_pairs

        ans_if_last_is_part_of_solution = most_pairs

    else:
        ans_if_last_is_part_of_solution = []

    if len(ans_if_last_is_not_part_of_solution) > len(ans_if_last_is_part_of_solution):
        return ans_if_last_is_not_part_of_solution
    else:
        return ans_if_last_is_part_of_solution

def opt_recursive_with_dict(i,j, original_string, dictionary):
    """
    First call(0, len(original_string), original_string)
    Recursive solution.
    Returns maximal number of pairings in RNA string, between position i and position j in the string.
    Has not been seriously tested.
    THIS VERSION RETURNS POSITION OF PAIRS
    """

    if (i,j) in dictionary:
        return dictionary[(i,j)]

    if j - i < 5:
        dictionary[(i,j)] = []
        return []

    # if last letter is NOT part of a solution-pair:
    ans_if_last_is_not_part_of_solution = opt_recursive_with_dict(i, j - 1, original_string, dictionary)

    # if last letter IS part of a solution-pair:
    possible_t = pairings_of_last(original_string, i, j-1)

    if len(possible_t) > 0:
        most_pairs = []

        for t in possible_t:
            first_part = opt_recursive_with_dict(i, t, original_string, dictionary)
            second_part = opt_recursive_with_dict(t + 1, j - 1, original_string, dictionary)
            new_pairs = first_part + second_part + [(t, j-1)]
            if len(new_pairs) > len(most_pairs):
                most_pairs = new_pairs

        ans_if_last_is_part_of_solution = most_pairs

    else:
        ans_if_last_is_part_of_solution = []

    if len(ans_if_last_is_not_part_of_solution) > len(ans_if_last_is_part_of_solution):
        dictionary[(i,j)] = ans_if_last_is_not_part_of_solution
        return ans_if_last_is_not_part_of_solution
    else:
        dictionary[(i,j)] = ans_if_last_is_part_of_solution
        return ans_if_last_is_part_of_solution

#string = "AAAAAUUUUAAAUUUUUUUUUUUUUUUU"
#print opt_recursive_with_dict(0, len(string), string, {})

def dyn_opt(original_string):
    """
    MATRIX LIBRARY
    Dynamic programmning solution.
    FirstInput = i, j, original_string
    First call should be: (0, len(string), original_string, empty_dictionary)
    """

    n = len(original_string)

    opt_lib = [[[] for col in range(n)] for row in range(n)]

    ans_if_last_is_part_of_solution = []
    ans_if_last_is_not_part_of_solution = []

    for k in range(4, n-1):
        for i in range(n-k-1):
            j = i + k+1
            #print i,j
            # if last letter is NOT part of a solution-pair:
            ans_if_last_is_not_part_of_solution = opt_lib[i][j - 1]

            # if last letter IS part of a solution-pair:
            possible_t = pairings_of_last(original_string, i, j)
            if len(possible_t) > 0:
                most_pairs = []

                for t in possible_t:
                    #print t
                    first_part = opt_lib[i][t-1]
                    #print "opt_libt[{}][{}]={}".format(i,t-1, first_part)
                    second_part = opt_lib[t + 1][j - 1]
                    #print "opt_lib[{}][{}]={}".format(t+1,j-1, second_part)
                    new_pairs = first_part + second_part + [(t, j)]
                    if len(new_pairs)>len(most_pairs):
                    #len(new_pairs) > len(most_pairs):
                        most_pairs = new_pairs

                ans_if_last_is_part_of_solution = most_pairs

            else:
                ans_if_last_is_part_of_solution = []

            if len(ans_if_last_is_not_part_of_solution) > len(ans_if_last_is_part_of_solution):
                opt_lib[i][j] = ans_if_last_is_not_part_of_solution
            else:
                opt_lib[i][j] = ans_if_last_is_part_of_solution
            #print i,j, possible_t
            #for t in possible_t:
            #    print original_string[t], original_string[j]#opt_lib[i][j]


    #for row in range(n-1,-1,-1):
    #    print opt_lib[row]

    return opt_lib[0][n-1]

def run():
    string = "CCAAAAAUUAAAAAAAUUUUUCCCCCGGGG"

    print "RNA string of length ", len(string),":\n", string

    print "Number of pairs in secondary RNA structure:", len(dyn_opt(string))
    #print len(opt_recursive_with_dict(0, len(string), string, {}))
    #print len(opt(0, len(string), string))
#run()




def plot_running_times():
    """
    Use gen_random_clusters and your favorite Python timing code to compute the running times of the
    functions slow_closest_pair and fast_closest_pair for lists of clusters of size 2 to 200.
    """
    import matplotlib.pyplot as plt
    import time
    x_vals = []
    y_1_vals = []
    y_2_vals = []
    y_3_vals = []
    add_string = "AUCGGGA"
    string = ""

    for num in range(80):
        string += add_string
        x_vals.append(len(string))

        t0 = time.clock()
        dyn_opt(string)
        y_1_vals.append(time.clock() - t0)

        # t0 = time.clock()
        # opt(0, len(string), string)
        # y_2_vals.append(time.clock() - t0)

        t0 = time.clock()
        opt_recursive_with_dict(0, len(string), string, {})
        y_3_vals.append(time.clock() - t0)


    plt.plot(x_vals, y_1_vals, label = "Dynamic buttom-up solution")
    #plt.plot(x_vals, y_2_vals, label = "Recursive solution")
    plt.plot(x_vals, y_3_vals, label = "Dynamic/recursive top-down solution")

    plt.xlabel("Input size (length of RNA string)")
    plt.ylabel('CPU running time (sec.)')

    #tegner
    plt.legend()

    plt.title("Comparison of running times (desktop Python)")

    #goer det hele synligt
    plt.show()

plot_running_times()
