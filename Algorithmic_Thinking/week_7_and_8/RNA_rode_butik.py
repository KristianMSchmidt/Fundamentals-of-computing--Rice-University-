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

# string = "CCAAAAGUGGAACAAAAU"
# print len(string)
# i = 5
# j= len(string)-1
# print string[j]
# print pairings_of_last(string, 5, j)

# def pairings_of_last(string):
#     possible_t = []
#
#     if string[-1] == "A":
#         for index in range(len(string) - 5):
#             if string[index] == "U":
#                 possible_t.append(index)
#
#     if string[-1] == "U":
#         for index in range(len(string) - 5):
#             if string[index] == "A":
#                 possible_t.append(index)
#
#     if string[-1] == "C":
#         for index in range(len(string) - 5):
#             if string[index] == "G":
#                 possible_t.append(index)
#
#     if string[-1] == "G":
#         for index in range(len(string) - 5):
#             if string[index] == "C":
#                 possible_t.append(index)
#     return possible_t

#print pairings_of_last("GAUUGGGGGGC")



def opt(string):
    """
    Recursive solution.
    Returns maximal number of pairings in RNA string, between position i and position j in the string.
    Has not been seriously tested.
    THSI VERSION DOES NOT RETURN POSITION OF PAIRS
    """

    if len(string) < 6:
        return 0

    # if last letter is NOT part of a solution-pair:
    ans_if_last_is_not_part_of_solution = opt(string[:-1])

    # if last letter IS part of a pair solution-pair:
    possible_t = pairings_of_last(string)

    if len(possible_t) > 0:
        list_to_max = [1 +
                       opt(string[:t]) +
                       opt(string[t + 1 :-1])
                       for t in possible_t]
        ans_if_last_is_part_of_solution = max(list_to_max)

    else:
        ans_if_last_is_part_of_solution = 0

    return max(ans_if_last_is_not_part_of_solution, ans_if_last_is_part_of_solution)

#AU og GC
#print "FINAL ANSWER:", opt("AGGAAAACCUUUUUUUUUUUUUUUUUUUGGGGGGGGGGGGGGGGCCCCCCCCCCCC")

#print opt("GAGAAAAAAAAAUUCC", [])


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

#AU og GC
original_string = "ACCCCUCCC"
print original_string, len(original_string)
#print "FINAL ANSWER:",
solution = opt(0, len(original_string), original_string)
solution.sort()
print solution



def opt(i,j, original_string, pairs):
    """
    First call(0, len(original_string), original_string, [])
    Recursive solution.
    Returns maximal number of pairings in RNA string, between position i and position j in the string.
    Has not been seriously tested.
    THIS VERSION RETURNS POSITION OF PAIRS
    """

    if j - i < 5:
        return (len(pairs), pairs)

    # if last letter is NOT part of a solution-pair:
    ans_if_last_is_not_part_of_solution = opt(i, j - 1, original_string, pairs)

    # if last letter IS part of a pair solution-pair:
    possible_t = pairings_of_last(original_string[i : j])

    if len(possible_t) > 0:
        list_to_max = []
        for t in possible_t:
            first_part = opt(i, t, original_string, [(t, j-1)])
            second_part = opt(t + 1, j-1, original_string, [(t, j-1)])
            new_pair_number = 1 + first_part[0] + second_part[0] + len(pairs)
            new_pairs = first_part[1] + second_part[1] + [(t, j - 1)]
            list_to_max.append((new_pair_number, new_pairs))
        #print list_to_max
        ans_if_last_is_part_of_solution = max(list_to_max)
    else:
        ans_if_last_is_part_of_solution = (0, pairs)

    print ans_if_last_is_not_part_of_solution
    print ""
    print ans_if_last_is_part_of_solution

    return max(ans_if_last_is_not_part_of_solution, ans_if_last_is_part_of_solution)

#AU og GC
original_string = "GGAAAACC"
#print "FINAL ANSWER:",
#opt(0, len(original_string), original_string, [])


    # for k in range(5, n - 1):
    #     for i in range(1, n - k)
    #         j = i + k
    #         ans_if_max(opt(string, i, j - 1), max_t(1 + opt(i, t-1)+ opt(t+1,j-1)))
    #
