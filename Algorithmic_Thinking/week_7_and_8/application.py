"""
Provide code and solution for Application 4
"""

DESKTOP = True

import math
import random
import urllib2

if DESKTOP:
    import matplotlib.pyplot as plt
    import project as p
else:
    import simpleplot
    import userXX_XXXXXXX as student


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"



###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict




def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)

    # read in files as string
    words = word_file.read()

    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list




### Provided code stops here. Rest is my own##############################


### QUESTION 1

def analyze_data():
    global human_protein, fruitfly_protein, alignment, scoring_matrix
    human_protein = read_protein(HUMAN_EYELESS_URL)
    fruitfly_protein = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    alignment_matrix = p.compute_alignment_matrix(human_protein, fruitfly_protein, scoring_matrix, False)
    alignment = p.compute_local_alignment(human_protein, fruitfly_protein, scoring_matrix, alignment_matrix)
analyze_data()

def q1_solution():
    print "Length of fluitfly_protein is {}".format(len(fruitfly_protein))
    print "Length of human_protein is {}".format(len(human_protein))
    print "Alignment", alignment
    print "Length of alignment", len(alignment[1])
#q1_solution()


### QUESTION 2
"""
Load the file ConsensusPAXDomain. For each of the two sequences of the local
 alignment computed in Question 1, do the following:

Delete any dashes '-' present in the sequence.
Compute the global alignment of this dash-less sequence with the ConsensusPAXDomain sequence.
Compare corresponding elements of these two globally-aligned sequences (local vs. consensus) and
compute the percentage of elements in these two sequences that agree.
"""
def q2_solution():
    consensus = read_protein(CONSENSUS_PAX_URL)
    #print "Consensus PAX domain: \n", consensus
    #print "\nLength of census PAX domain", len(consensus)

    local_alignment_human = alignment[1]
    local_alignment_human_no_dashes = local_alignment_human.replace("-", "")
    print "\nLocal_alignment_1: \n", local_alignment_human_no_dashes
    alignment_matrix1 = p.compute_alignment_matrix(consensus,local_alignment_human_no_dashes, scoring_matrix, True)
    global_alignment_consensus_vs_human = p.compute_global_alignment(consensus, local_alignment_human_no_dashes, scoring_matrix, alignment_matrix1)
    print "\nGlobal alignment consensus vs human:\n", global_alignment_consensus_vs_human

    global_human1 = global_alignment_consensus_vs_human[1]
    global_human2 = global_alignment_consensus_vs_human[2]
    num_agree1 = 0
    for indx in range(len(global_human1)):
        if global_human1[indx] == global_human2[indx]:
            num_agree1 += 1
    print "Pencentage of ageeing letters in global alignment of local human VS consensus: {}%".format(num_agree1/float(len(global_human1))*100)

    local_alignment_fruitfly = alignment[2]
    local_alignment_fruitfly_no_dashes = local_alignment_fruitfly.replace("-", "")
    print "\nLocal_alignment_2:\n", local_alignment_fruitfly_no_dashes
    alignment_matrix2 = p.compute_alignment_matrix(consensus, local_alignment_fruitfly_no_dashes, scoring_matrix, True)
    global_alignment_consensus_vs_fruitfly = p.compute_global_alignment(consensus, local_alignment_fruitfly_no_dashes, scoring_matrix, alignment_matrix2)
    print "\nGlobal alignment consensus vs chimp:\n", global_alignment_consensus_vs_fruitfly

    global_fruitfly1 = global_alignment_consensus_vs_fruitfly[1]
    global_fruitfly2 = global_alignment_consensus_vs_fruitfly[2]
    num_agree2 = 0
    for indx in range(len(global_fruitfly1)):
        if global_fruitfly1[indx] == global_fruitfly2[indx]:
            num_agree2 += 1
    print "Pencentage of ageeing letters in global alignment of local fruitfly VS consensus: {}%".format(num_agree2/float(len(global_fruitfly1))*100)

#q2_solution()


### QUESTION 3#:

#Examine your answers to Questions 1 and 2. Is it likely that the level of similarity exhibited by the answers could have
#been due to chance? In particular, if you were comparing two random sequences of amino acids of length similar to that
#of HumanEyelessProtein and FruitflyEyelessProtein, would the level of agreement in these answers be likely?
# To help you in your analysis, there are 23 amino acids with symbols in the string ("ACBEDGFIHKMLNQPSRTWVYXZ").
# Include a short justification for your #answer.
### A: NO!!! HIGHLY UNLIKELY


### Question 4:
def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    """
    Takes as input two sequences seq_x and
    seq_y, a scoring matrix scoring_matrix, and a number of trials num_trials. This function should return a dictionary
    scoring_distribution that represents an un-normalized distribution
    generated by performing the following process num_trials times:

    Generate a random permutation rand_y of the sequence seq_y using random.shuffle().
    Compute the maximum value score for the local alignment of seq_x and rand_y using the score matrix scoring_matrix.
    Increment the entry score in the dictionary scoring_distribution by one.
    """
    scoring_distribution = {}

    for dummy in range(num_trials):
        list_y = list(seq_y)
        random.shuffle(list_y)
        rand_y = ''.join(list_y)
        alignment_matrix = p.compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False)
        score = p.compute_local_alignment(seq_x, rand_y, scoring_matrix, alignment_matrix)[0]
        scoring_distribution[score] = scoring_distribution.get(score, 0) + 1
    return scoring_distribution

def test():
    scoringmatrix = p.build_scoring_matrix(set(["a","b"]),10,4,-6)
    generate_null_distribution("aaaaaaaab", "aabbbbaabbba", scoringmatrix, 500)
#test()

def q4_and_q5():
    """
    Use the function generate_null_distribution to create a distribution with 1000 trials using the protein sequences
    HumanEyelessProtein and FruitflyEyelessProtein (using the PAM50 scoring matrix). Important: Use HumanEyelessProtein
    as the first parameter seq_x (which stays fixed) and FruitflyEyelessProtein as the second parameter seq_y
    (which is randomly shuffled) when calling generate_null_distribution. Switching the order of these two parameters will
    lead to a slightly different answers for question 5 that may lie outside the accepted ranges for correct answers.
    """
    num_trials = 1000
    human_protein = read_protein(HUMAN_EYELESS_URL)
    fruitfly_protein = read_protein(FRUITFLY_EYELESS_URL)
    scoring_matrix = read_scoring_matrix(PAM50_URL)
    distr = generate_null_distribution(human_protein, fruitfly_protein, scoring_matrix, num_trials)

    scores, freqs = [], []

    for score, number in distr.items():
        scores.append(score)
        freqs.append(number/float(num_trials))

    plt.bar(scores, freqs)
    plt.xlabel('Score')
    plt.ylabel('Fraction')

    plt.title("Score distribution when aligning human eyeless protein with random string of same length")

    plt.show()

    mean_score = 0
    for score, freq in zip(scores, freqs):
        mean_score += score*freq
    print "mean", mean_score

    deviation = 0
    for score, number in distr.items():
        deviation += number*((mean_score - score)**2)
    deviation = math.sqrt((1/float(num_trials))*deviation)

    print "deviation", deviation


    ### Calculation of z-score (= antal standardafvigelser som observationen ligger fra middelvaerdien)
    real_score = alignment[0]
    print "real_score=", real_score
    z_score = (real_score-mean_score)/float(deviation)
    print "z-score", z_score

#q4_and_q5()



###Q7: Edit distance
##FORMULA: Edit distance = len(seqx) + len(seqy) - score(seqx, seqy), hvor scoringsmatricen er indrettet som nedenfor
#def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
#def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):

def q7():
    seq_x = "kqistian"
    seq_y = "kristian"
    scor_matrix = p.build_scoring_matrix(["a","b","e","k","q","t","r","i","t","n","s"], 2, 1, 0)
    #print scor_matrix
    #print ""
    align_matrix = p.compute_alignment_matrix(seq_x, seq_y, scor_matrix, True)
    print align_matrix
    score = p.compute_global_alignment(seq_x, seq_y, scor_matrix, align_matrix)
    print score
#q7()

#Question 8
    """
    In practice, edit distance is a useful tool in applications such as spelling correction and plagiarism detection where
     determining whether two strings are similar/dissimilar is important. For this final question, we will implement a
      simple spelling correction function that uses edit distance to determine whether a given string is the misspelling o
      f a word.

    To begin, load this list of 79339 words. Then, write a function check_spelling(checked_word, dist, word_list) that
     iterates through word_list and returns the set of all words that are within edit distance dist of the string
     checked_word.

    Use your function check_spelling to compute the set of words within an edit distance of one from the string "humble" and the set of words within an edit distance of two from the string "firefly". (Note this is not "fruitfly".)

    Enter these two sets of words in the box below. As quick check, both sets should include eleven words.
    """

WORDS = read_words(WORD_LIST_URL)
print WORDS[:100]

def check_spelling(checked_word, dist, word_list):
    answer = set()
    letters = list("qwertyuiopasdfghjklzxcvbnm")
    scor_matrix = p.build_scoring_matrix(letters, 2, 1, 0)

    for word in word_list:
        align_matrix = p.compute_alignment_matrix(checked_word, word, scor_matrix, True)
        score = p.compute_global_alignment(checked_word, word, scor_matrix, align_matrix)[0]
        edit_distance = len(word) + len(checked_word) - score
        if edit_distance <= dist:
            answer.add(word)
    return answer

#print check_spelling("humble",1, WORDS)
#print check_spelling("firefly", 2, WORDS)


import sys
print (sys.version_info)
