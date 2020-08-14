"""
Global and local sequence alignment problems
Krms
25/12/2017
"""

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    Takes as input a set of characters alphabet and three scores diag_score, off_diag_score, and dash_score.
    The function returns a dictionary of dictionaries whose entries are indexed by pairs of characters in alphabet plus '-'.
    The score for any entry indexed by one or more dashes is dash_score. The score for the remaining diagonal entries is
     diag_score. Finally, the score for the remaining off-diagonal entries is off_diag_score.
    One final note for build_scoring_matrix is that, although an alignment with two matching dashes is not allowed,
    the scoring matrix should still include an entry for two dashes (which will never be used).
    """
    scoring_matrix = {}

    alphabet = list(alphabet) + ["-"]

    for letter1 in alphabet:
        scoring_matrix[letter1] = {}
        for letter2 in alphabet:
            if letter1 == "-" or letter2 == "-":
                scoring_matrix[letter1][letter2] = dash_score
            elif letter1 == letter2:
                scoring_matrix[letter1][letter2] = diag_score
            else:
                scoring_matrix[letter1][letter2] = off_diag_score

    #for key,val in scoring_matrix.items():
    #    print key,val

    return scoring_matrix



def test():
    """
    test function
    """

    result1 = build_scoring_matrix(set(["a","b"]),10,4,-6)
    expected1 = {"a":{"a":10, "b":4, "-":-6}, "b":{"a":4, "b":10, "-":-6}, "-": {"a":-6, "b":-6, "-":  -6}}
    print (result1 == expected1)

    result2 = build_scoring_matrix(set(["a"]),10,4,-6)
    expected2 = {"a":{"a":10, "-":-6}, "-": {"a":-6, "-":  -6}}
    print (result2 == expected2)
#test()


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring matrix
    scoring_matrix. The function computes and returns the alignment matrix for seq_x and seq_y as described in the Homework.
    If global_flag is True, each entry of the alignment matrix is computed using the method described in Question 8
    of the Homework. If global_flag is False, each entry is computed using the method described in Question 12 of
    the Homework.
    """
    len_x = len(seq_x)
    len_y = len(seq_y)

    alignment_matrix = [[0 for col in range(len_y + 1)] for row in range(len_x + 1)]

    for row in range(1, len_x + 1):
        possible_score = alignment_matrix[row-1][0] + scoring_matrix["-"][seq_x[row-1]]
        if global_flag:
            alignment_matrix[row][0] = possible_score
        else:
            alignment_matrix[row][0] = max(0, possible_score)

    for col in range(1, len_y+1):
        possible_score = alignment_matrix[0][col-1] + scoring_matrix["-"][seq_y[col-1]]
        if global_flag:
            alignment_matrix[0][col] = possible_score
        else:
            alignment_matrix[0][col] = max(0, possible_score)

    for row in range(1, len_x+1):
        for col in range(1, len_y+1):
            route1 = alignment_matrix[row-1][col-1] + scoring_matrix[seq_x[row-1]][seq_y[col-1]]
            route2 = alignment_matrix[row-1][col] + scoring_matrix[seq_x[row -1]]["-"]
            route3 = alignment_matrix[row][col-1] + scoring_matrix["-"][seq_y[col-1]]
            possible_score = max(route1, route2, route3)
            if global_flag:
                alignment_matrix[row][col] = possible_score
            else:
                alignment_matrix[row][col] = max(0, possible_score)

    #for row in alignment_matrix:
     #  print row

    return alignment_matrix

def test2():
    """
    test function
    """

    scoring_matrix = build_scoring_matrix(set(["a", "b"]), 10, 4, -6)
    result = compute_alignment_matrix("aa", "abb", scoring_matrix, True)
    for row in result:
        print (row)
    expected = [[0,0,0],
                [0,10,4]]
    print (result == expected)
    #
    # scoring_matrix = build_scoring_matrix(set(["a", "b","c"]), 10, 4, -6)
    # result = compute_alignment_matrix("a", "abc", scoring_matrix, True)
    # expected = [[0,-6,-12,-18],
    #             [-6,10,4, -2]]
    # print result == expected
    #
    # scoring_matrix = build_scoring_matrix(set(["a", "b","c"]), 10, 4, -6)
    # result = compute_alignment_matrix("ab", "abc", scoring_matrix, True)
    # expected = [[0,-6,-12,-18],
    #             [-6,10, 4, -2],
    #             [-12, 4,20,14]]
    #
    # print result == expected
    #
    # scoring_matrix = build_scoring_matrix(set(["a", "b","c"]), 10, 4, -6)
    # result = compute_alignment_matrix("abc", "bc", scoring_matrix, True)
    # expected = [[0,-6,-12],
    #             [-6,4, -2],
    #             [-12, 4,8],
    #             [-18,-2,14]]
    # print result == expected

#test2()


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    The first function will implement the method ComputeAlignment discussed in Question 9 of the Homework.
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring
    matrix scoring_matrix. This function computes a global alignment of seq_x and seq_y using the global alignment matrix
    alignment_matrix.The function returns a tuple of the form (score, align_x, align_y) where score is the score of the
     global alignment align_x and align_y. Note that align_x and align_y should have the same length and may include the
     padding character '-'.
    """

    align_x = ""
    align_y = ""

    len_x = len(seq_x)
    len_y = len(seq_y)

    score = alignment_matrix[len_x][len_y]

    while len_x > 0 and len_y > 0:
        if alignment_matrix[len_x][len_y] == alignment_matrix[len_x -1][len_y - 1] + scoring_matrix[seq_x[len_x-1]][seq_y[len_y-1]]:
            align_x = seq_x[len_x-1] + align_x
            align_y = seq_y[len_y-1] + align_y
            len_x -= 1
            len_y -= 1
        elif alignment_matrix[len_x][len_y] == alignment_matrix[len_x -1][len_y] + scoring_matrix[seq_x[len_x-1]]["-"]:
            align_x = seq_x[len_x-1] + align_x
            align_y = "-" + align_y
            len_x -= 1
        else:
            align_x = "-" + align_x
            align_y = seq_y[len_y-1] + align_y
            len_y -= 1

    while len_x > 0:
        align_x = seq_x[len_x-1] + align_x
        align_y = "-" + align_y
        len_x -= 1

    while len_y > 0:
        align_x = "-" + align_x
        align_y = seq_y[len_y-1] + align_y
        len_y -= 1

    return (score, align_x, align_y)

def test3():
    """
    test function
    """

    scoring_matrix = build_scoring_matrix(set(["a", "b","c"]), 10, 4, -6)
    alignment_matrix = compute_alignment_matrix("abbc", "abc", scoring_matrix, True)
    computed = compute_global_alignment("abbc", "abc", scoring_matrix, alignment_matrix)
    print (computed)
    expected = ("a-", "ab", 4)
    print (computed == expected)

#test3()


import random
def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    This second function will compute an optimal local alignment starting at the maximum entry of the local alignment
    matrix and working backwards to zero as described in Question 13 of the Homework.
    Takes as input two sequences seq_x and seq_y whose elements share a common alphabet with the scoring
    matrix scoring_matrix. This function computes a local alignment of seq_x and seq_y using the local alignment
    matrix alignment_matrix.The function returns a tuple of the form (score, align_x, align_y) where score is the score
    of the optimal local alignment align_x and align_y.
    Note that align_x and align_y should have the same length and may include the padding character '-'.
    """
    align_x = ""
    align_y = ""

    len_x = len(seq_x)
    len_y = len(seq_y)

    #score = max([alignment_matrix[row][col] for row in range(len_x + 1) for col in range(len_y+1)])

    max_score = -1
    max_positions = []
    for row in range(len(seq_x)+1):
        for col in range(len(seq_y)+1):
            if alignment_matrix[row][col] == max_score:
                max_positions.append((row,col))
            if alignment_matrix[row][col] > max_score:
                max_score = alignment_matrix[row][col]
                max_positions = [(row, col)]
    max_row, max_col = random.choice(max_positions)

    #print max_score, max_row, max_col

    len_x = max_row
    len_y = max_col

    while alignment_matrix[len_x][len_y] > 0:
        #print len_x, len_y
        if alignment_matrix[len_x][len_y] == alignment_matrix[len_x -1][len_y - 1] + scoring_matrix[seq_x[len_x-1]][seq_y[len_y-1]]:
            align_x = seq_x[len_x-1] + align_x
            align_y = seq_y[len_y-1] + align_y
            len_x -= 1
            len_y -= 1
        elif alignment_matrix[len_x][len_y] == alignment_matrix[len_x -1][len_y] + scoring_matrix[seq_x[len_x-1]]["-"]:
            align_x = seq_x[len_x-1] + align_x
            align_y = "-" + align_y
            len_x -= 1
        else:
            align_x = "-" + align_x
            align_y = seq_y[len_y-1] + align_y
            len_y -= 1

    #while len_x > 0:
    #    align_x = seq_x[len_x-1] + align_x
    #    align_y = "-" + align_y
    #    len_x -= 1

    #while len_y > 0:
    #    align_x = "-" + align_x
    #    align_y = seq_y[len_y-1] + align_y
    #    len_y -= 1

    return (max_score, align_x, align_y)


def test4():
    """
    test function
    """
    string1 = "kristian"
    string2 = "krtisian"

    scoring_matrix = build_scoring_matrix(set(["k", "r","i","s","t", "a", "n"]), 10, 0, -6)

    alignment_matrix = compute_alignment_matrix(string1, string2, scoring_matrix, False)

    for row in alignment_matrix:
        print (row)
    print ("")

    computed = compute_local_alignment(string1, string2, scoring_matrix, alignment_matrix)

    print (computed)
    #expected = ("a-", "ab", 4)
    #print computed == expected

test4()
