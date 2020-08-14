
"""
Automatic Yahtzee player. Plays game based on expected value calculations for next move.
Yahtzee rules are stated here: https://cardgames.io/yahtzee/.

This version should yield around an average of 205 total points pr. game.

Made by Kristian Moeller Schmidt, Copenhagen. Last edited 14/11/2017.

Strength of my algorithm: I solved a flaw in the suggested strategy function, namely that it
doesn't take into account which Yahtzee game objectives has already been 'scored' by the machine player
in earlier rounds. For example, if a player has already scored "Full House" in an earlier round, the
 expeced value calculation should give 0 points for the opportunity of "Full House".

Weakness of my algorithm: When deciding what to hold after first roll of the dice in each round, the
machine player makes its decision based only on the expected value after next roll. A more clever player
would base his hold decision on the fact that there are two possible rolls left. However, using "brute
force" to solve this problem leads to an unresonably slow program (i've tried).

IDEA: Can I make the program more efficient by storing calculated values in a dictionary? (As in fibonacci?).

"""

import random


## Dictionary for practical purposes
OBJECTIVES = {0: "1's",
              1: "2's",
              2: "3's",
              3: "4's",
              4: "5's",
              5: "6's",
              6: "Three of a kind",
              7: "Four of a kind",
              8: "Full house",
              9: "Small straight",
              10: "Large straight",
              11: "Chance",
              12: "YAHTZEE"}

#List of optimal scores corresponding to each of the above objectives. Used to calculate relative score.
OPTIMAL_SCORES = (5, 10, 15, 20, 25, 30, 30, 29, 25, 30, 40, 30, 50)

## Game is being played with a fair six sided die
DIE_SIDES = (1, 2, 3, 4, 5, 6)


class YahtzeePlayer:
    """
    Automated Yahtzee Player. Can make all the choices and actions required to play a game to the end.
    """

    def __init__(self):
        """
        'score_notes' is the list of game objectives met so far (i.e. the yahtzee player's note book)
        'rolls_left' is 0, 1 or 2. If 0, the player has no more rolls and has to score an objective
        'hand' is alle the dice, the player has on the table

        """
        self.score_notes = [None for dummy in range(13)]
        self.rolls_left = 3
        self.hand= [None for dummy in range(5)]

    def __str__(self):
        """
        Makes a nice string representation of player's score notebook
        """
        game_state = self.get_game_state()
        s = "Player's notebook: \n"
        for key in OBJECTIVES:
            if self.score_notes[key] == None:
                score = "---"
            else:
                score = str(self.score_notes[key])
            s += OBJECTIVES[key] + ": " + score + "\n"
        return s

    def get_game_state(self):
        """
        Returns number of game objectives scored so far : 0, 1, 2, 3,...12, or 13.
        If game_state is 13, the game is over.
        """
        game_state = 0
        for indx in range(13):
            if self.score_notes[indx] != None:
                game_state += 1
        return game_state

    def get_total_score(self):
        """
        Return total score of score_board
        """
        sum_score = 0
        for indx in range(len(self.score_notes)-1):
            if self.score_notes[indx] != None:
                sum_score += self.score_notes[indx]
        return sum_score

    def all_potential_scores(self, hand):
        """
        Returns a list of all the diffent scores a given hand can give if it won't be rolled again.
        If a game objective has already be met, the score of this objective will be set to None.

        Scoring rules are as follows:

        # objective number   objective            score
        #   0                1's                   sum all 1's
        #   1                2's                   sum of all 2's
           (...)            (...)                  (...)
        #   5               6's                    sum of all 6's
        #   6               three of a kind        sum of all 5 dice
        #   7               four of a kind         sum of all 5 dice
        #   8               full house             25 points
        #   9               small straight         30 points
        #   10              large straight         40 Points
        #   11              chance                 sum of all 5 dice
        #   12              YAHTZEE                50 point
        """

        scores=[0 for dummy in range(13)]

        for die in hand:
            #count simple scores (obj. 0-5)
            scores[die-1] += die

            #count chance score
            scores[11] = sum(hand)

            #control for full house, for 3 and 4 of a kind and for YAHTZEE
            exactly_two_of_some_kind = False
            exactly_three_of_some_kind = False

        for die in set(hand):
            if hand.count(die) == 2:
                exactly_two_of_some_kind = True
            if hand.count(die) == 3:
                scores[6] = sum(hand)
                exactly_three_of_some_kind = True
            elif hand.count(die) == 4:
                scores[6] = sum(hand)
                scores[7] = sum(hand)
            elif hand.count(die) == 5:
                scores[6] = sum(hand)
                scores[7] = sum(hand)
                scores[12] = 50

        if exactly_two_of_some_kind and exactly_three_of_some_kind:
            scores[8] = 25

        #check for small and large straight
        small_straights = [set([1,2,3,4]),set([2,3,4,5]),set([3,4,5,6])]
        large_straights = [set([1,2,3,4,5]), set([2,3,4,5,6])]

        for small in small_straights:
            if small.issubset(set(hand)):
                scores[9] = 30

        for large in large_straights:
            if large.issubset(set(hand)):
                scores[10] = 40

        #only scores of game objectives not yet met has relevance
        for idx in range(13):
            if self.score_notes[idx] != None:
                scores[idx] = None
        return scores

    def roll_all_dice(self):
        self.hand = random.choice(list(gen_all_sequences(DIE_SIDES, 5)))
        self.rolls_left -= 1
        print "All dice rolled with result: " + str(tuple(sorted(self.hand))) + "\n"

    def reset_dice(self):
        self.hand = [None for dummy in range(5)]
        self.rolls_left = 3

    def choose_objective(self):
        """
        Chooses game objective to cash in given a final hand.
        Chooses according to the following rule:
            1. Calculate best relative score of the 13 objectives
            2. Don't consider choosing an objective, if it doesn't have the best relative score
            3. If only one objective has best relative score, choose this. If more than one, choose
               the one among these that has the best absolute score.
            4. If there are still more than one to choose between, choose the one of the options left that
                 has the smallest objetive number (as good scores on these tend to be harder to achieve).
            5. Finally there are some (wise??) adhoc rules, to avoid some seemingly bad decisions.
               My ad hoc rules are incomplete and unscientific, deserving of more consideration.
               Playing with onlye ad hoc-rule 2 gives around 204,5 in average!


        Fills out associated objective with assicated score the players' noteboook.
        """
        scores = self.all_potential_scores(self.hand)
        relative_scores = [None for dummy in range(13)]
        for indx in range(13):
            if scores[indx] != None:
                relative_scores[indx] = scores[indx]/float(OPTIMAL_SCORES[indx])

        max_rel_score = max(relative_scores)

        #first choices
        chosen_objective = relative_scores.index(max_rel_score)
        chosen_score = scores[chosen_objective]

        #check for better choices
        for indx in range(13):
            if relative_scores[indx] == max_rel_score and max_rel_score > 0.40:
                if scores[indx] > chosen_score:
                    chosen_score = scores[indx]
                    chosen_objective = indx

        #ad hoc rule 1: Go for 'four of a kind' instead of 'three of a kind', whenever possible
        #This rule seems sound but hasn't proved to mean much in empirical tests, so can be omitted
        #if chosen_objective == 6 and scores[7] != None:
        #    if scores[6] == 0 or scores[7] > 0:
        #        chosen_objective = 7
        #        chosen_score = scores[7]

        #ad hoc rule 2: Better to get 0p for 1's than to get only 6p points for 6's
        if (chosen_objective == 4 and chosen_score == 5) or (chosen_objective == 5 and chosen_score == 6):
            if scores[0] != None:
                chosen_objective = 0
            chosen_score = scores[chosen_objective]

        self.score_notes[chosen_objective] = chosen_score
        return (chosen_objective, chosen_score)

    def expected_value(self, held_dice):
        """
        Compute the expected value based on held_dice.

        Returns a floating point expected value
        """
        num_free_dice = 5 - len(held_dice)
        all_outcomes = gen_all_sequences(range(1,7),num_free_dice)
        num_outcomes = len(all_outcomes)
        cummulated_score = 0
        for outcome in all_outcomes:
            potential_hand = held_dice + outcome
            cummulated_score += max(self.all_potential_scores(potential_hand))

        return (1.0/num_outcomes)*cummulated_score

    def strategy(self):
        """
        Compute the hold that maximizes the (absolute) expected value when the
        discarded dice are rolled.

        Returns the die to hold for next round
        """
        holds = list(gen_all_holds(self.hand))
        exp_vals = [self.expected_value(hold) for hold in holds]
        pos_of_best_hold = exp_vals.index(max(exp_vals))
        return holds[pos_of_best_hold]


    def play_a_round(self):
        """
        Plays one round of Yahtzee to the end.
        Print out relavent information to the screen.
        """
        print ":::::::::::::::: ROUND", self.get_game_state()+1, "::::::::::::::::"
        print ""
        self.roll_all_dice()
        round_not_over = True

        while round_not_over:
            hold = self.strategy()
            if self.rolls_left == 0 or len(hold) == 5:
                chosen_objective, chosen_score = self.choose_objective()
                self.reset_dice()
                round_not_over = False
                print "Player chose", chosen_score, "points for '" + OBJECTIVES[chosen_objective]+ "'"
                print ""
                print self
                if self.get_game_state() == 13:
                    print "Game ended with total score:", self.get_total_score(), "out of", sum(OPTIMAL_SCORES)

            else:
                new_roll = random.choice(list(gen_all_sequences([1,2,3,4,5,6], 5-len(hold))))
                self.rolls_left -= 1
                self.hand = hold + new_roll
                print "Player chose to hold:", print_tuple(hold)
                print "Player rolled", len(new_roll), "dice and got:", print_tuple(new_roll)
                print "Hand after new roll:", print_tuple(self.hand)
                print ""

    def play_full_game(self):
        """
        Plays an intere YAHTZEE game to the end.
        """
        while self.get_game_state() < 13:
            self.play_a_round()

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

def print_tuple(some_tuple):
    """
    Helper function to print out dice tupes nicely
    """

    if len(some_tuple) > 1:
        return tuple(sorted(some_tuple))
    elif len(some_tuple) == 1:
        return str(some_tuple[0])
    else:
        return ""

def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.
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

def test(number):
    """
    function used to test choose_objective method
    """
    player=YahtzeePlayer()
    player.hand = (3,3,3,4,5)
    for indx in range(number):
        print "Hand:", player.hand
        player.choose_objective()
        print player
#test(2)

def get_average(number):
    """
    Plays complete Yahtzee game any number of times.
    Return the average final score.
    This is useful when trying to estimate the quality of the machine player
    """
    summa = 0
    for dummy in range(number):
        player = YahtzeePlayer()
        player.play_full_game()
        summa += player.get_total_score()
    print ""
    print "Played full game", number, "times."
    print "The average final score was:", float(summa)/number

#get_average(50)



def run_program():
    """
    Starts the user interface for the game
    """
    print "Welcome to the automatic YAHTZEE player"
    print "To play first round, press 'Enter'"
    #print "To play game, press 'f' followed by 'Enter'"
    print ""
    player = YahtzeePlayer()
    while True:
        x = raw_input()
        if x == "f":
            player.play_full_game()
        elif player.get_game_state() < 12:
            player.play_a_round()
            print "To play next round, press 'Enter'"
        elif player.get_game_state() == 12:
            player.play_a_round()
run_program()
