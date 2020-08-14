

"""
OUTDATED VERSION. IVE MADE A MUCH BETTER PROGRAM THAN THIS

"""

# Used to increase the timeout, if necessary
#import codeskulptor
#codeskulptor.set_timeout(20)
import random

class Yahtzee:
    """
    Class to control game_state
    """
    def __init__(self):
        """
        #0 = 1's
        #1 = 2's
        #2 = 3's
        (...)
        #5 = 6's
        #6 = three of a kind.
        #7 = four of a kind.
        #8 = full house
        #9 = small straight
        #10= large straight
        #11 = chance
        #12 = YAHTZEE 50 point

        None means that the field has not yet been played

        """
        self.score_board = [None for dummy in range(13)]
        self.roll_number = 0
        #dices in play
        self.hand= [None for dummy in range(5)]

    def __str__(self):
        s = "Yahtzee Score Board:" + "\n"
        s += "1's: "+ str(self.score_board[0]) + "\n"
        s += "2's: " +str(self.score_board[1])+ "\n"
        s += "3's: "+str( self.score_board[2])+ "\n"
        s += "4's: "+str( self.score_board[3])+ "\n"
        s += "5's: "+str( self.score_board[4])+ "\n"
        s += "6's: "+str( self.score_board[5])+ "\n"
        s += "Three of a kind: " +str( self.score_board[6])+ "\n"
        s += "Four of a kind: " + str(self.score_board[7])+ "\n"
        s += "Full House: " + str(self.score_board[8])+ "\n"
        s += "Small straight: " + str(self.score_board[9])+ "\n"
        s += "Large straight: "+ str(self.score_board[10])+ "\n"
        s += "Change: " + str(self.score_board[11])+ "\n"
        s += "YAHTZEE: " + str(self.score_board[12])+ "\n"
        return s

    def is_game_on(self):
        """
        checks if score_board is full
        """
        if None in self.score_board:
            return True
        else:
            return False

    def get_score(self):
        """
        return total score of score_board
        """
        sum_score = 0
        for indx in range(len(self.score_board)-1):
            sum_score += self.score_board[indx]
        return sum_score

    def choose_pos(self, hand):
        """
        Given a hand after two rolls, this method should fill out the best postition on the scoreboard
        Should this be a function instead of a method?

        """
        game_finished = True

        for position in self.score_board:
            if position == None:
                game_finished = False

        if game_finished:
            print "Game finished \n"
            return

        scores = score_list(hand)

        max_val = 0
        best_choice = 0

        for idx in range(13):
            if self.score_board[idx] == None:
                if scores[idx] >= max_val:
                    max_val = scores[idx]
                    best_choice = idx

        self.score_board[best_choice] = max_val

def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """
    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set

def score_list(hand):
    """
    Returns a list score values of a given hand of 5 dices according to the following rules:
    #0 = sum score count of 1's
    #1 = sum score count of 2's
    #...
    #5 = sum score count of 6's
    #6 = three of a kind. score is sum of all 5 dices
    #7 = four of a kind. score is sum of all 5 dices
    #8 = full house 25 point
    #9 = small straight 1,2,3,4 og 2,3,4,5 or 3,4,5,6 30 point
    #10= large straight 1,2,3,4,5 or 2,3,4,5,6  40 Point
    #11 = chance
    #12 = YAHTZEE 50 point
    """

    scores=[0 for dummy in range(13)]

    #register upper scores:
    for dice in hand:
        scores[dice-1] += dice

    #count chance score
    scores[11] = sum(hand)

    #control for full house, for 3 and 4 of a kind and for YAHTZEE
    exactly_two_of_some_kind = False
    exactly_three_of_some_kind = False

    die_with_3_occ = [0]
    die_with_4_occ = [0]

    for x in set(hand):
        if hand.count(x) == 2:
            exactly_two_of_some_kind = True
        if hand.count(x) == 3:
            scores[6] = sum(hand)
            exactly_three_of_some_kind = True
        elif hand.count(x) == 4:
            scores[6] = sum(hand)
            scores[7] = sum(hand)
            die_with_4_occ.append(4)
        elif hand.count(x) == 5:
            scores[6] = sum(hand)
            scores[7] = sum(hand)
            scores[12] = 50

    if exactly_two_of_some_kind and exactly_three_of_some_kind:
        scores[8] = 25

    #check of small and large straight
    small_straights = [set([1,2,3,4]),set([2,3,4,5]),set([3,4,5,6])]
    large_straights = [set([1,2,3,4,5]), set([2,3,4,5,6])]


    for small in small_straights:
        if small.issubset(set(hand)):
            scores[9] = 30

    for large in large_straights:
        if large.issubset(set(hand)):
            scores[10] = 40

    return scores

def score(hand, comp_player):
    """
    Compute the maximal score for a Yahtzee hand.

    hand: full yahtzee hand

    Returns an integer score
    """
    possible_scores = []
    all_scores = score_list(hand)

    for indx in range(13):
        if comp_player.score_board[indx] == None:
            possible_scores.append(all_scores[indx])

    return max(possible_scores)

#print score ((1,2,3,4,2))
"""
yat = Yahtzee()
print yat
yat.choose_pos((1,1,1,1,6))
print yat
yat.choose_pos((1,1,1,1,1))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((1,1,1,1,1))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((1,1,1,1,1))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
yat.choose_pos((5,5,5,5,5))
print yat
"""

def expected_value(held_dice, num_die_sides, num_free_dice, comp_player):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value

    """
    all_outcomes = gen_all_sequences(range(1,num_die_sides+1),num_free_dice)
    num_outcomes = len(all_outcomes)
    cummulated_score = 0
    for outcome in all_outcomes:
        final_hand = held_dice+outcome
        cummulated_score += score(final_hand, comp_player)
    return (1.0/num_outcomes)*cummulated_score


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """
    answer_set = set([()])
    for position in range(len(hand)):
        temp_set = set()
        for partial_seq in answer_set:
            new_seq1 = (list(partial_seq))
            new_seq1.append(hand[position])
            new_seq2 = list(partial_seq)
            temp_set.add(tuple(new_seq1))
            temp_set.add(tuple(new_seq2))
        answer_set = temp_set
    return answer_set


def strategy(hand, num_die_sides, comp_player):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    holds = list(gen_all_holds(hand))
    exp_vals = [expected_value(hold, num_die_sides, len(hand)-len(hold), comp_player) for hold in holds]
    pos_of_best_hold = exp_vals.index(max(exp_vals))
    return (max(exp_vals), holds[pos_of_best_hold])



def auto_play(comp_player):
    """
    if rolls=2 > choose_pos
    if rolls<2: if it chooses to hold all ->> choose_pos
    if rolls <2: if it chooses to roll some dices ->> roll dices
     method or function
    """
    hand = comp_player.hand

    if None in hand:
        print "First roll"
        comp_player.hand = random.choice(list(gen_all_sequences([1,2,3,4,5,6], 5)))
        hand = comp_player.hand
    print hand
    print ""

    if comp_player.roll_number == 2 or len(strategy(hand, 6, comp_player)[1]) == 5:
        comp_player.choose_pos(hand)
        comp_player.roll_number = 0
        print "Computer scored some points"
        print comp_player

    else:
        hand_score, hold = strategy(hand, 6, comp_player)
        print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score
        comp_player.roll_number += 1


        dices_to_roll = list(hand)
        hold_list = list(hold)

        for dice in hand:
            if dice in hold_list:
                dices_to_roll.remove(dice)
                hold_list.remove(dice)

        new_roll = random.choice(list(gen_all_sequences([1,2,3,4,5,6], len(dices_to_roll))))

        print ""
        print "New roll is:", new_roll
        print ""
        comp_player.hand=hold+new_roll
        print "Computer player now has the hand:", comp_player.hand
        print "Roll number is", comp_player.roll_number

def play_full_game(comp_player):
        while comp_player.is_game_on():
            auto_play(comp_player)
        print "Game ended. Final score is", comp_player.get_score()
        return

yat = Yahtzee()
play_full_game(yat)





def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (6,6,6,6,6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score

#run_example()

"""
Test suites for the game
"""
import poc_simpletest

def test_suite():

    # create a TestSuite object
    suite = poc_simpletest.TestSuite()

    #test expexted_value
    suite.run_test(expected_value((1,2,3,6),6,1),7.0, "Test #7")

    #suite.run_test(expected_value((1,2,3,2),6,1),31/6.0, "test #8")
    suite.run_test(expected_value((1,1,1,1,1),6,0), 5.0, "Test #9")
    suite.run_test(expected_value((), 6,2), 182.0/36, "Test #10")
    suite.run_test(expected_value((),2,0),0)
    suite.run_test(expected_value((3,),3,1),4.0, "Test #12")

    # test function "score"
    suite.run_test(score([1,1,1,1,1]), 5, "Test #1:")
    suite.run_test(score([1,2,3,4,5]),5, "Test #2:")
    suite.run_test(score([1,2,3,4,4]),8, "Test #3:")
    suite.run_test(score([6,1,1,1,1]), 6, "Test #4:")
    suite.run_test(score([6,6,5,5,5]),15, "Test #5:")
    suite.run_test(score([1,2,3,4,4]),8, "Test #6:")

    #report test results
    suite.report_results()

#test_suite()





#import poc_holds_testsuite
#poc_holds_testsuite.run_suite(gen_all_holds)
