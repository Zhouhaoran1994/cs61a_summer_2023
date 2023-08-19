"""The Game of Hog."""

from dice import six_sided, make_test_dice
from ucb import main, trace, interact

GOAL = 100  # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    point, sow_sad = 0, False
    for _ in range(num_rolls):
        single_point = dice()
        if single_point == 1:
            sow_sad = True
        point += single_point
    if sow_sad:
        point = 1
    return point
    # END PROBLEM 1


def boar_brawl(player_score, opponent_score):
    """Return the points scored by rolling 0 dice according to Boar Brawl.

    player_score:     The total score of the current player.
    opponent_score:   The total score of the other player.

    """
    # BEGIN PROBLEM 2
    tens_digit = opponent_score // 10 % 10
    ones_digit = player_score % 10
    return max(3 * abs(tens_digit - ones_digit), 1)
    # END PROBLEM 2


def take_turn(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the points scored on a turn rolling NUM_ROLLS dice when the
    player has PLAYER_SCORE points and the opponent has OPPONENT_SCORE points.

    num_rolls:       The number of dice rolls that will be made.
    player_score:    The total score of the current player.
    opponent_score:  The total score of the other player.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    # BEGIN PROBLEM 3
    if num_rolls == 0:
        return boar_brawl(player_score, opponent_score)
    return roll_dice(num_rolls, dice)
    # END PROBLEM 3


def simple_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, ignoring Fuzzy Factors.
    """
    score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return score


def hog_gcd(x, y):
    """Return the greatest common divisor between X and Y"""
    # BEGIN PROBLEM 4
    if y == 0:
        return x
    return hog_gcd(y, x % y)
    # END PROBLEM 4


def fuzzy_points(score):
    """Return the new score of a player taking into account the Fuzzy Factors rule.
    """
    # BEGIN PROBLEM 4
    gcd = hog_gcd(score, 100)
    if gcd > 10:
        score = score + 2 * (gcd // 10 % 10)
    return score
    # END PROBLEM 4


def fuzzy_update(num_rolls, player_score, opponent_score, dice=six_sided):
    """Return the total score of a player who starts their turn with
    PLAYER_SCORE and then rolls NUM_ROLLS DICE, *including* Fuzzy Factors.
    
    >>> fuzzy_update(3, 11, 12, make_test_dice(4, 5, 6))
    26
    >>> fuzzy_update(2, 29, 17, make_test_dice(1, 3))
    30
    >>> fuzzy_update(0, 41, 42)
    60
    >>> fuzzy_update(2, 56, 56, make_test_dice(4))
    64
    """
    # BEGIN PROBLEM 4
    current_score = player_score + take_turn(num_rolls, player_score, opponent_score, dice)
    return fuzzy_points(current_score)
    # END PROBLEM 4


def always_roll_5(score, opponent_score):
    """A strategy of always rolling 5 dice, regardless of the player's score or
    the oppononent's score.
    """
    return 5


def play(strategy0, strategy1, update,
         score0=0, score1=0, dice=six_sided, goal=GOAL):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first and Player 1's score second.

    E.g., play(always_roll_5, always_roll_5, fuzzy_update) simulates a game in
    which both players always choose to roll 5 dice on every turn and the Fuzzy
    Factors rule is in effect.

    A strategy function, such as always_roll_5, takes the current player's
    score and their opponent's score and returns the number of dice the current
    player chooses to roll.

    An update function, such as fuzzy_update or simple_update, takes the number
    of dice to roll, the current player's score, the opponent's score, and the
    dice function used to simulate rolling dice. It returns the updated score
    of the current player after they take their turn.

    strategy0: The strategy for player0.
    strategy1: The strategy for player1.
    update:    The update function (used for both players).
    score0:    Starting score for Player 0
    score1:    Starting score for Player 1
    dice:      A function of zero arguments that simulates a dice roll.
    goal:      The game ends and someone wins when this score is reached.

    >>> import hog, importlib
    >>> import tests.play_utils
    >>> turns = tests.play_utils.describe_game(hog, test_number=67024, score0=59, score1=4, goal=60, update=hog.fuzzy_update)
    >>> print(turns[0])
    Start scores = (59, 4).
    Player 0 rolls 1 dice and gets outcomes [4].
    End scores = (63, 4)
    >>> print(turns[1])
    Game Over

    >>> turns = tests.play_utils.describe_game(hog, test_number=33242, score0=15, score1=34, goal=50, update=hog.simple_update)
    >>> print(turns[0])
    Start scores = (15, 34).
    Player 0 rolls 10 dice and gets outcomes [6, 3, 1, 5, 5, 6, 4, 4, 4, 2].
    End scores = (16, 34)
    >>> print(turns[1])
    Start scores = (16, 34).
    Player 1 rolls 10 dice and gets outcomes [3, 5, 6, 5, 4, 5, 5, 1, 5, 2].
    End scores = (16, 35)
    >>> print(turns[2])
    Start scores = (16, 35).
    Player 0 rolls 10 dice and gets outcomes [4, 6, 1, 5, 4, 4, 2, 6, 2, 6].
    End scores = (17, 35)
    >>> print(turns[3])
    Start scores = (17, 35).
    Player 1 rolls 3 dice and gets outcomes [6, 4, 6].
    End scores = (17, 51)
    >>> print(turns[4])
    Game Over

    >>> turns = tests.play_utils.describe_game(hog, test_number=49921, score0=0, score1=5, goal=17, update=hog.simple_update)
    >>> print(turns[0])
    Start scores = (0, 5).
    Player 0 rolls 4 dice and gets outcomes [1, 1, 2, 4].
    End scores = (1, 5)
    >>> print(turns[1])
    Start scores = (1, 5).
    Player 1 rolls 3 dice and gets outcomes [6, 1, 5].
    End scores = (1, 6)
    >>> print(turns[2])
    Start scores = (1, 6).
    Player 0 rolls 6 dice and gets outcomes [3, 1, 5, 5, 1, 4].
    End scores = (2, 6)
    >>> print(turns[3])
    Start scores = (2, 6).
    Player 1 rolls 6 dice and gets outcomes [6, 4, 4, 4, 4, 3].
    End scores = (2, 31)
    >>> print(turns[4])
    Game Over

    >>> turns = tests.play_utils.describe_game(hog, test_number=52065, score0=5, score1=34, goal=67, update=hog.fuzzy_update)
    >>> print(turns[0])
    Start scores = (5, 34).
    Player 0 rolls 10 dice and gets outcomes [5, 2, 6, 2, 4, 4, 5, 3, 1, 4].
    End scores = (6, 34)
    >>> print(turns[1])
    Start scores = (6, 34).
    Player 1 rolls 4 dice and gets outcomes [3, 5, 2, 2].
    End scores = (6, 46)
    >>> print(turns[2])
    Start scores = (6, 46).
    Player 0 rolls 1 dice and gets outcomes [4].
    End scores = (10, 46)
    >>> print(turns[3])
    Start scores = (10, 46).
    Player 1 rolls 8 dice and gets outcomes [5, 2, 6, 2, 3, 2, 3, 3].
    End scores = (10, 72)
    >>> print(turns[4])
    Game Over
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    # BEGIN PROBLEM 5
    while score0 < goal and score1 < goal:
        if not who:
            score0 = update(strategy0(score0, score1), score0, score1, dice)
        else:
            score1 = update(strategy1(score1, score0), score1, score0, dice)
        who = 1 - who

    # END PROBLEM 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################


def always_roll(n):
    """Return a player strategy that always rolls N dice.

    A player strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(3)
    >>> strategy(0, 0)
    3
    >>> strategy(99, 99)
    3
    """
    assert n >= 0 and n <= 10
    # BEGIN PROBLEM 6
    return n
    # END PROBLEM 6


def catch_up(score, opponent_score):
    """A player strategy that always rolls 5 dice unless the opponent
    has a higher score, in which case 6 dice are rolled.

    >>> catch_up(9, 4)
    5
    >>> strategy(17, 18)
    6
    """
    if score < opponent_score:
        return 6  # Roll one more to catch up
    else:
        return 5


def is_always_roll(strategy, goal=GOAL):
    """Return whether STRATEGY always chooses the same number of dice to roll
    given a game that goes to GOAL points.

    >>> is_always_roll(always_roll_5)
    True
    >>> is_always_roll(always_roll(3))
    True
    >>> is_always_roll(catch_up)
    False
    """
    first_roll = strategy(0, 0)
    # BEGIN PROBLEM 7
    for score0 in range(goal):
        for score1 in range(goal):
            if strategy(score0, score1) != first_roll:
                return False
    return True
    # END PROBLEM 7


def make_averaged(original_function, total_samples=1000):
    """Return a function that returns the average value of ORIGINAL_FUNCTION
    called TOTAL_SAMPLES times.

    To implement this function, you will have to use *args syntax.

    >>> dice = make_test_dice(4, 2, 5, 1)
    >>> averaged_dice = make_averaged(roll_dice, 40)
    >>> averaged_dice(1, dice)  # The avg of 10 4's, 10 2's, 10 5's, and 10 1's
    3.0
    """
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    # END PROBLEM 8


def max_scoring_num_rolls(dice=six_sided, total_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn score
    by calling roll_dice with the provided DICE a total of TOTAL_SAMPLES times.
    Assume that the dice always return positive outcomes.

    >>> dice = make_test_dice(1, 6)
    >>> max_scoring_num_rolls(dice)
    1
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    # END PROBLEM 9


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1, fuzzy_update)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(6)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    six_sided_max = max_scoring_num_rolls(six_sided)
    print('Max scoring num rolls for six-sided dice:', six_sided_max)

    print('always_roll(6) win rate:', average_win_rate(always_roll(6)))  # near 0.5
    print('catch_up win rate:', average_win_rate(catch_up))
    print('always_roll(3) win rate:', average_win_rate(always_roll(3)))
    print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    print('boar_strategy win rate:', average_win_rate(boar_strategy))
    print('fuzzy_strategy win rate:', average_win_rate(fuzzy_strategy))
    print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"


def boar_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice if Boar Brawl gives at least THRESHOLD
    points, and returns NUM_ROLLS otherwise. Ignore score and Fuzzy Factors.
    """
    # BEGIN PROBLEM 10
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 10


def fuzzy_strategy(score, opponent_score, threshold=12, num_rolls=6):
    """This strategy returns 0 dice when your score would increase by at least threshold."""
    # BEGIN PROBLEM 11
    return num_rolls  # Remove this line once implemented.
    # END PROBLEM 11


def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.

    *** YOUR DESCRIPTION HERE ***
    """
    # BEGIN PROBLEM 12
    return 6  # Remove this line once implemented.
    # END PROBLEM 12


##########################
# Command Line Interface #
##########################

# NOTE: The function in this section does not need to be changed. It uses
# features of Python not yet covered in the course.

@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
