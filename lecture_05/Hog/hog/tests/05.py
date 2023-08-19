test = {
  'name': 'Question 5',
  'points': 4,
  'suites': [
    {
      'cases': [
        {
          'answer': 'a4d959d6146005b45f9590c6bc256e37',
          'choices': [
            'While score0 and score1 are both less than goal',
            'While at least one of score0 or score1 is less than goal',
            'While score0 is less than goal',
            'While score1 is less than goal'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          The variables score0 and score1 are the scores for Player 0
          and Player 1, respectively. Under what conditions should the
          game continue?
          """
        },
        {
          'answer': 'bcda62bd369acb79a636e354f5ef2f48',
          'choices': [
            'The number of dice a player will roll',
            'A function that returns the number of dice a player will roll',
            "A player's desired turn outcome"
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': 'What is a strategy in the context of this game?'
        },
        {
          'answer': '6092933b58b128fe246b574b1aa79389',
          'choices': [
            'strategy1(score1, score0)',
            'strategy1(score0, score1)',
            'strategy1(score1)',
            'strategy1(score0)'
          ],
          'hidden': False,
          'locked': True,
          'multiline': False,
          'question': r"""
          If strategy1 is Player 1's strategy function, score0 is
          Player 0's current score, and score1 is Player 1's current
          score, then which of the following demonstrates correct
          usage of strategy1?
          """
        }
      ],
      'scored': False,
      'type': 'concept'
    },
    {
      'cases': [
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=69484, score0=15, score1=10, goal=32, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (15, 10).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 6, 6, 6, 5, 4, 4].
          End scores = (16, 10)
          >>> print(turns[1])
          Start scores = (16, 10).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 4, 6, 2].
          End scores = (16, 28)
          >>> print(turns[2])
          Start scores = (16, 28).
          Player 0 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (17, 28)
          >>> print(turns[3])
          Start scores = (17, 28).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (17, 49)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=42415, score0=3, score1=3, goal=46, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (3, 3).
          Player 0 rolls 3 dice and gets outcomes [5, 5, 4].
          End scores = (17, 3)
          >>> print(turns[1])
          Start scores = (17, 3).
          Player 1 rolls 8 dice and gets outcomes [3, 1, 3, 3, 2, 3, 1, 5].
          End scores = (17, 4)
          >>> print(turns[2])
          Start scores = (17, 4).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 4, 5, 2, 5].
          End scores = (18, 4)
          >>> print(turns[3])
          Start scores = (18, 4).
          Player 1 rolls 2 dice and gets outcomes [3, 6].
          End scores = (18, 13)
          >>> print(turns[4])
          Start scores = (18, 13).
          Player 0 rolls 6 dice and gets outcomes [4, 1, 6, 3, 2, 1].
          End scores = (19, 13)
          >>> print(turns[5])
          Start scores = (19, 13).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 2, 1, 3, 4, 1, 3].
          End scores = (19, 14)
          >>> print(turns[6])
          Start scores = (19, 14).
          Player 0 rolls 10 dice and gets outcomes [4, 2, 3, 5, 6, 4, 3, 4, 3, 4].
          End scores = (57, 14)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=15589, score0=14, score1=13, goal=88, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (14, 13).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (23, 13)
          >>> print(turns[1])
          Start scores = (23, 13).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (23, 16)
          >>> print(turns[2])
          Start scores = (23, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (29, 16)
          >>> print(turns[3])
          Start scores = (29, 16).
          Player 1 rolls 6 dice and gets outcomes [3, 4, 1, 5, 2, 6].
          End scores = (29, 17)
          >>> print(turns[4])
          Start scores = (29, 17).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (30, 17)
          >>> print(turns[5])
          Start scores = (30, 17).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 2].
          End scores = (30, 28)
          >>> print(turns[6])
          Start scores = (30, 28).
          Player 0 rolls 10 dice and gets outcomes [6, 6, 5, 2, 1, 6, 6, 3, 5, 1].
          End scores = (31, 28)
          >>> print(turns[7])
          Start scores = (31, 28).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 6, 2, 5, 3].
          End scores = (31, 49)
          >>> print(turns[8])
          Start scores = (31, 49).
          Player 0 rolls 2 dice and gets outcomes [5, 2].
          End scores = (38, 49)
          >>> print(turns[9])
          Start scores = (38, 49).
          Player 1 rolls 4 dice and gets outcomes [3, 2, 4, 6].
          End scores = (38, 64)
          >>> print(turns[10])
          Start scores = (38, 64).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 3, 3, 5, 5].
          End scores = (60, 64)
          >>> print(turns[11])
          Start scores = (60, 64).
          Player 1 rolls 8 dice and gets outcomes [4, 6, 5, 2, 3, 2, 3, 4].
          End scores = (60, 93)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27754, score0=23, score1=55, goal=56, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (23, 55).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 6, 1].
          End scores = (24, 55)
          >>> print(turns[1])
          Start scores = (24, 55).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 1, 3, 6, 4, 4].
          End scores = (24, 56)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50266, score0=64, score1=24, goal=88, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (64, 24).
          Player 0 rolls 9 dice and gets outcomes [5, 5, 1, 4, 6, 6, 2, 4, 1].
          End scores = (65, 24)
          >>> print(turns[1])
          Start scores = (65, 24).
          Player 1 rolls 8 dice and gets outcomes [5, 6, 5, 4, 1, 5, 1, 1].
          End scores = (65, 29)
          >>> print(turns[2])
          Start scores = (65, 29).
          Player 0 rolls 2 dice and gets outcomes [4, 3].
          End scores = (72, 29)
          >>> print(turns[3])
          Start scores = (72, 29).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (72, 31)
          >>> print(turns[4])
          Start scores = (72, 31).
          Player 0 rolls 5 dice and gets outcomes [6, 5, 5, 3, 6].
          End scores = (97, 31)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=3995, score0=3, score1=4, goal=10, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (3, 4).
          Player 0 rolls 4 dice and gets outcomes [5, 4, 5, 3].
          End scores = (20, 4)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=1033, score0=47, score1=10, goal=49, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (47, 10).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 3, 5, 1].
          End scores = (48, 10)
          >>> print(turns[1])
          Start scores = (48, 10).
          Player 1 rolls 7 dice and gets outcomes [3, 3, 5, 5, 2, 1, 2].
          End scores = (48, 11)
          >>> print(turns[2])
          Start scores = (48, 11).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 5, 3, 6, 5, 2, 3, 2, 2].
          End scores = (87, 11)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=23897, score0=8, score1=11, goal=44, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (8, 11).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 4, 4, 3, 3, 2, 2, 3].
          End scores = (9, 11)
          >>> print(turns[1])
          Start scores = (9, 11).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (9, 16)
          >>> print(turns[2])
          Start scores = (9, 16).
          Player 0 rolls 3 dice and gets outcomes [1, 5, 6].
          End scores = (10, 16)
          >>> print(turns[3])
          Start scores = (10, 16).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (10, 22)
          >>> print(turns[4])
          Start scores = (10, 22).
          Player 0 rolls 9 dice and gets outcomes [1, 3, 4, 3, 6, 4, 3, 5, 3].
          End scores = (11, 22)
          >>> print(turns[5])
          Start scores = (11, 22).
          Player 1 rolls 9 dice and gets outcomes [1, 5, 2, 2, 5, 2, 1, 2, 5].
          End scores = (11, 23)
          >>> print(turns[6])
          Start scores = (11, 23).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 4, 1, 6, 6].
          End scores = (12, 23)
          >>> print(turns[7])
          Start scores = (12, 23).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (12, 29)
          >>> print(turns[8])
          Start scores = (12, 29).
          Player 0 rolls 5 dice and gets outcomes [2, 2, 4, 6, 6].
          End scores = (32, 29)
          >>> print(turns[9])
          Start scores = (32, 29).
          Player 1 rolls 3 dice and gets outcomes [3, 4, 2].
          End scores = (32, 38)
          >>> print(turns[10])
          Start scores = (32, 38).
          Player 0 rolls 9 dice and gets outcomes [1, 3, 4, 1, 6, 2, 6, 2, 5].
          End scores = (33, 38)
          >>> print(turns[11])
          Start scores = (33, 38).
          Player 1 rolls 8 dice and gets outcomes [1, 1, 2, 5, 4, 3, 6, 4].
          End scores = (33, 39)
          >>> print(turns[12])
          Start scores = (33, 39).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 39)
          >>> print(turns[13])
          Start scores = (34, 39).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (34, 57)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=17635, score0=7, score1=9, goal=10, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (7, 9).
          Player 0 rolls 2 dice and gets outcomes [3, 2].
          End scores = (12, 9)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98858, score0=0, score1=20, goal=66, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (0, 20).
          Player 0 rolls 4 dice and gets outcomes [5, 1, 4, 1].
          End scores = (1, 20)
          >>> print(turns[1])
          Start scores = (1, 20).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (1, 21)
          >>> print(turns[2])
          Start scores = (1, 21).
          Player 0 rolls 4 dice and gets outcomes [6, 2, 5, 6].
          End scores = (24, 21)
          >>> print(turns[3])
          Start scores = (24, 21).
          Player 1 rolls 5 dice and gets outcomes [6, 6, 5, 6, 4].
          End scores = (24, 48)
          >>> print(turns[4])
          Start scores = (24, 48).
          Player 0 rolls 7 dice and gets outcomes [1, 5, 3, 6, 6, 6, 2].
          End scores = (29, 48)
          >>> print(turns[5])
          Start scores = (29, 48).
          Player 1 rolls 10 dice and gets outcomes [6, 4, 1, 4, 3, 4, 2, 2, 5, 4].
          End scores = (29, 49)
          >>> print(turns[6])
          Start scores = (29, 49).
          Player 0 rolls 7 dice and gets outcomes [4, 3, 2, 3, 4, 4, 6].
          End scores = (55, 49)
          >>> print(turns[7])
          Start scores = (55, 49).
          Player 1 rolls 3 dice and gets outcomes [6, 6, 2].
          End scores = (55, 63)
          >>> print(turns[8])
          Start scores = (55, 63).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 1, 1, 4, 4, 5, 2].
          End scores = (56, 63)
          >>> print(turns[9])
          Start scores = (56, 63).
          Player 1 rolls 4 dice and gets outcomes [2, 6, 3, 4].
          End scores = (56, 78)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=96385, score0=13, score1=20, goal=36, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (13, 20).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (19, 20)
          >>> print(turns[1])
          Start scores = (19, 20).
          Player 1 rolls 6 dice and gets outcomes [5, 2, 3, 5, 2, 5].
          End scores = (19, 42)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=66739, score0=5, score1=4, goal=11, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (5, 4).
          Player 0 rolls 2 dice and gets outcomes [6, 4].
          End scores = (15, 4)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=88253, score0=8, score1=5, goal=35, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (8, 5).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (32, 5)
          >>> print(turns[1])
          Start scores = (32, 5).
          Player 1 rolls 9 dice and gets outcomes [1, 4, 4, 2, 4, 2, 4, 3, 4].
          End scores = (32, 6)
          >>> print(turns[2])
          Start scores = (32, 6).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 3, 5, 5, 5, 3].
          End scores = (60, 6)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=39236, score0=15, score1=32, goal=53, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (15, 32).
          Player 0 rolls 2 dice and gets outcomes [1, 3].
          End scores = (16, 32)
          >>> print(turns[1])
          Start scores = (16, 32).
          Player 1 rolls 5 dice and gets outcomes [2, 4, 1, 4, 1].
          End scores = (16, 33)
          >>> print(turns[2])
          Start scores = (16, 33).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (22, 33)
          >>> print(turns[3])
          Start scores = (22, 33).
          Player 1 rolls 9 dice and gets outcomes [5, 4, 5, 4, 3, 3, 2, 1, 1].
          End scores = (22, 34)
          >>> print(turns[4])
          Start scores = (22, 34).
          Player 0 rolls 5 dice and gets outcomes [5, 6, 3, 6, 4].
          End scores = (46, 34)
          >>> print(turns[5])
          Start scores = (46, 34).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 2, 2, 4, 5, 2, 4, 1, 3].
          End scores = (46, 35)
          >>> print(turns[6])
          Start scores = (46, 35).
          Player 0 rolls 5 dice and gets outcomes [5, 3, 5, 6, 5].
          End scores = (70, 35)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=73001, score0=15, score1=18, goal=23, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (15, 18).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 1, 2, 1, 4].
          End scores = (16, 18)
          >>> print(turns[1])
          Start scores = (16, 18).
          Player 1 rolls 8 dice and gets outcomes [5, 6, 2, 2, 2, 3, 3, 3].
          End scores = (16, 44)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=6301, score0=47, score1=33, goal=71, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (47, 33).
          Player 0 rolls 5 dice and gets outcomes [1, 6, 4, 5, 2].
          End scores = (48, 33)
          >>> print(turns[1])
          Start scores = (48, 33).
          Player 1 rolls 7 dice and gets outcomes [4, 5, 6, 5, 6, 1, 5].
          End scores = (48, 34)
          >>> print(turns[2])
          Start scores = (48, 34).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (51, 34)
          >>> print(turns[3])
          Start scores = (51, 34).
          Player 1 rolls 4 dice and gets outcomes [5, 4, 3, 3].
          End scores = (51, 49)
          >>> print(turns[4])
          Start scores = (51, 49).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 1, 2, 2, 3].
          End scores = (52, 49)
          >>> print(turns[5])
          Start scores = (52, 49).
          Player 1 rolls 7 dice and gets outcomes [4, 1, 5, 3, 6, 2, 5].
          End scores = (52, 50)
          >>> print(turns[6])
          Start scores = (52, 50).
          Player 0 rolls 6 dice and gets outcomes [5, 5, 5, 2, 6, 2].
          End scores = (77, 50)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=96485, score0=51, score1=24, goal=85, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (51, 24).
          Player 0 rolls 4 dice and gets outcomes [3, 4, 4, 1].
          End scores = (52, 24)
          >>> print(turns[1])
          Start scores = (52, 24).
          Player 1 rolls 2 dice and gets outcomes [1, 6].
          End scores = (52, 29)
          >>> print(turns[2])
          Start scores = (52, 29).
          Player 0 rolls 5 dice and gets outcomes [6, 6, 5, 5, 3].
          End scores = (77, 29)
          >>> print(turns[3])
          Start scores = (77, 29).
          Player 1 rolls 8 dice and gets outcomes [5, 6, 5, 6, 3, 5, 5, 5].
          End scores = (77, 69)
          >>> print(turns[4])
          Start scores = (77, 69).
          Player 0 rolls 7 dice and gets outcomes [3, 1, 3, 6, 1, 3, 2].
          End scores = (78, 69)
          >>> print(turns[5])
          Start scores = (78, 69).
          Player 1 rolls 2 dice and gets outcomes [5, 4].
          End scores = (78, 78)
          >>> print(turns[6])
          Start scores = (78, 78).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (79, 78)
          >>> print(turns[7])
          Start scores = (79, 78).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (79, 81)
          >>> print(turns[8])
          Start scores = (79, 81).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 4, 5, 2].
          End scores = (84, 81)
          >>> print(turns[9])
          Start scores = (84, 81).
          Player 1 rolls 10 dice and gets outcomes [3, 4, 4, 2, 6, 3, 6, 1, 2, 2].
          End scores = (84, 82)
          >>> print(turns[10])
          Start scores = (84, 82).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (89, 82)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=20652, score0=30, score1=3, goal=51, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (30, 3).
          Player 0 rolls 7 dice and gets outcomes [3, 6, 3, 3, 2, 1, 2].
          End scores = (31, 3)
          >>> print(turns[1])
          Start scores = (31, 3).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 5].
          End scores = (31, 18)
          >>> print(turns[2])
          Start scores = (31, 18).
          Player 0 rolls 10 dice and gets outcomes [5, 6, 1, 3, 3, 6, 3, 2, 1, 3].
          End scores = (32, 18)
          >>> print(turns[3])
          Start scores = (32, 18).
          Player 1 rolls 9 dice and gets outcomes [5, 3, 3, 6, 2, 3, 5, 1, 6].
          End scores = (32, 19)
          >>> print(turns[4])
          Start scores = (32, 19).
          Player 0 rolls 4 dice and gets outcomes [4, 6, 2, 1].
          End scores = (33, 19)
          >>> print(turns[5])
          Start scores = (33, 19).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (33, 37)
          >>> print(turns[6])
          Start scores = (33, 37).
          Player 0 rolls 8 dice and gets outcomes [2, 5, 3, 4, 1, 6, 5, 1].
          End scores = (34, 37)
          >>> print(turns[7])
          Start scores = (34, 37).
          Player 1 rolls 7 dice and gets outcomes [5, 6, 1, 1, 3, 1, 2].
          End scores = (34, 38)
          >>> print(turns[8])
          Start scores = (34, 38).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (39, 38)
          >>> print(turns[9])
          Start scores = (39, 38).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (39, 53)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=80360, score0=23, score1=11, goal=38, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (23, 11).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (25, 11)
          >>> print(turns[1])
          Start scores = (25, 11).
          Player 1 rolls 2 dice and gets outcomes [6, 1].
          End scores = (25, 12)
          >>> print(turns[2])
          Start scores = (25, 12).
          Player 0 rolls 4 dice and gets outcomes [2, 1, 2, 1].
          End scores = (26, 12)
          >>> print(turns[3])
          Start scores = (26, 12).
          Player 1 rolls 8 dice and gets outcomes [2, 2, 5, 4, 2, 3, 5, 6].
          End scores = (26, 41)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=53740, score0=21, score1=18, goal=56, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (21, 18).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (26, 18)
          >>> print(turns[1])
          Start scores = (26, 18).
          Player 1 rolls 9 dice and gets outcomes [2, 3, 4, 6, 1, 4, 3, 5, 2].
          End scores = (26, 19)
          >>> print(turns[2])
          Start scores = (26, 19).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (29, 19)
          >>> print(turns[3])
          Start scores = (29, 19).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (29, 40)
          >>> print(turns[4])
          Start scores = (29, 40).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 5, 2, 2, 5, 2, 1, 5].
          End scores = (30, 40)
          >>> print(turns[5])
          Start scores = (30, 40).
          Player 1 rolls 2 dice and gets outcomes [4, 6].
          End scores = (30, 50)
          >>> print(turns[6])
          Start scores = (30, 50).
          Player 0 rolls 9 dice and gets outcomes [3, 5, 2, 4, 6, 6, 1, 5, 3].
          End scores = (31, 50)
          >>> print(turns[7])
          Start scores = (31, 50).
          Player 1 rolls 3 dice and gets outcomes [1, 4, 6].
          End scores = (31, 51)
          >>> print(turns[8])
          Start scores = (31, 51).
          Player 0 rolls 9 dice and gets outcomes [3, 1, 5, 5, 2, 6, 1, 6, 6].
          End scores = (32, 51)
          >>> print(turns[9])
          Start scores = (32, 51).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (32, 56)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=53943, score0=29, score1=9, goal=50, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (29, 9).
          Player 0 rolls 4 dice and gets outcomes [6, 3, 3, 4].
          End scores = (45, 9)
          >>> print(turns[1])
          Start scores = (45, 9).
          Player 1 rolls 9 dice and gets outcomes [4, 1, 5, 3, 3, 3, 4, 2, 3].
          End scores = (45, 10)
          >>> print(turns[2])
          Start scores = (45, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (57, 10)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=85875, score0=21, score1=66, goal=67, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (21, 66).
          Player 0 rolls 2 dice and gets outcomes [2, 1].
          End scores = (22, 66)
          >>> print(turns[1])
          Start scores = (22, 66).
          Player 1 rolls 4 dice and gets outcomes [5, 5, 2, 2].
          End scores = (22, 80)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=20869, score0=28, score1=16, goal=39, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (28, 16).
          Player 0 rolls 7 dice and gets outcomes [4, 5, 4, 5, 2, 3, 1].
          End scores = (29, 16)
          >>> print(turns[1])
          Start scores = (29, 16).
          Player 1 rolls 3 dice and gets outcomes [1, 6, 2].
          End scores = (29, 17)
          >>> print(turns[2])
          Start scores = (29, 17).
          Player 0 rolls 6 dice and gets outcomes [6, 1, 1, 2, 2, 6].
          End scores = (30, 17)
          >>> print(turns[3])
          Start scores = (30, 17).
          Player 1 rolls 9 dice and gets outcomes [6, 4, 4, 2, 5, 6, 1, 5, 5].
          End scores = (30, 18)
          >>> print(turns[4])
          Start scores = (30, 18).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 2, 4, 6, 2, 1, 4, 6, 3].
          End scores = (31, 18)
          >>> print(turns[5])
          Start scores = (31, 18).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (31, 33)
          >>> print(turns[6])
          Start scores = (31, 33).
          Player 0 rolls 8 dice and gets outcomes [4, 4, 1, 1, 6, 5, 5, 5].
          End scores = (32, 33)
          >>> print(turns[7])
          Start scores = (32, 33).
          Player 1 rolls 5 dice and gets outcomes [2, 2, 4, 4, 1].
          End scores = (32, 34)
          >>> print(turns[8])
          Start scores = (32, 34).
          Player 0 rolls 8 dice and gets outcomes [4, 1, 5, 2, 6, 2, 5, 3].
          End scores = (33, 34)
          >>> print(turns[9])
          Start scores = (33, 34).
          Player 1 rolls 6 dice and gets outcomes [5, 3, 4, 2, 1, 2].
          End scores = (33, 35)
          >>> print(turns[10])
          Start scores = (33, 35).
          Player 0 rolls 6 dice and gets outcomes [5, 1, 1, 5, 6, 5].
          End scores = (34, 35)
          >>> print(turns[11])
          Start scores = (34, 35).
          Player 1 rolls 10 dice and gets outcomes [2, 3, 2, 2, 6, 3, 4, 4, 5, 2].
          End scores = (34, 68)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=98819, score0=10, score1=37, goal=50, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (10, 37).
          Player 0 rolls 8 dice and gets outcomes [4, 3, 5, 4, 6, 1, 4, 3].
          End scores = (11, 37)
          >>> print(turns[1])
          Start scores = (11, 37).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (11, 42)
          >>> print(turns[2])
          Start scores = (11, 42).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 5, 4, 4].
          End scores = (31, 42)
          >>> print(turns[3])
          Start scores = (31, 42).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (31, 45)
          >>> print(turns[4])
          Start scores = (31, 45).
          Player 0 rolls 8 dice and gets outcomes [1, 1, 1, 6, 4, 6, 5, 5].
          End scores = (32, 45)
          >>> print(turns[5])
          Start scores = (32, 45).
          Player 1 rolls 5 dice and gets outcomes [2, 3, 5, 4, 5].
          End scores = (32, 64)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=82794, score0=60, score1=43, goal=61, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (60, 43).
          Player 0 rolls 3 dice and gets outcomes [3, 5, 2].
          End scores = (70, 43)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=83069, score0=7, score1=76, goal=80, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (7, 76).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 2, 6, 4, 6, 1, 1, 2, 5].
          End scores = (8, 76)
          >>> print(turns[1])
          Start scores = (8, 76).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 5, 5].
          End scores = (8, 94)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95167, score0=30, score1=33, goal=60, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (30, 33).
          Player 0 rolls 10 dice and gets outcomes [6, 6, 6, 5, 3, 3, 3, 3, 4, 5].
          End scores = (74, 33)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=70738, score0=16, score1=15, goal=23, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (16, 15).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 5, 2, 1, 2, 4].
          End scores = (17, 15)
          >>> print(turns[1])
          Start scores = (17, 15).
          Player 1 rolls 4 dice and gets outcomes [4, 1, 1, 3].
          End scores = (17, 16)
          >>> print(turns[2])
          Start scores = (17, 16).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (35, 16)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=28923, score0=8, score1=25, goal=50, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (8, 25).
          Player 0 rolls 8 dice and gets outcomes [5, 1, 1, 2, 5, 2, 2, 1].
          End scores = (9, 25)
          >>> print(turns[1])
          Start scores = (9, 25).
          Player 1 rolls 5 dice and gets outcomes [6, 2, 2, 1, 6].
          End scores = (9, 26)
          >>> print(turns[2])
          Start scores = (9, 26).
          Player 0 rolls 2 dice and gets outcomes [1, 1].
          End scores = (10, 26)
          >>> print(turns[3])
          Start scores = (10, 26).
          Player 1 rolls 5 dice and gets outcomes [3, 1, 1, 2, 3].
          End scores = (10, 27)
          >>> print(turns[4])
          Start scores = (10, 27).
          Player 0 rolls 6 dice and gets outcomes [3, 3, 6, 2, 6, 3].
          End scores = (33, 27)
          >>> print(turns[5])
          Start scores = (33, 27).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (33, 28)
          >>> print(turns[6])
          Start scores = (33, 28).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (36, 28)
          >>> print(turns[7])
          Start scores = (36, 28).
          Player 1 rolls 9 dice and gets outcomes [5, 4, 1, 1, 4, 2, 6, 1, 3].
          End scores = (36, 29)
          >>> print(turns[8])
          Start scores = (36, 29).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (48, 29)
          >>> print(turns[9])
          Start scores = (48, 29).
          Player 1 rolls 3 dice and gets outcomes [3, 5, 2].
          End scores = (48, 39)
          >>> print(turns[10])
          Start scores = (48, 39).
          Player 0 rolls 5 dice and gets outcomes [6, 2, 2, 6, 4].
          End scores = (68, 39)
          >>> print(turns[11])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=58200, score0=32, score1=95, goal=99, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (32, 95).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 4, 6, 1, 5].
          End scores = (33, 95)
          >>> print(turns[1])
          Start scores = (33, 95).
          Player 1 rolls 2 dice and gets outcomes [2, 5].
          End scores = (33, 102)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=72093, score0=5, score1=20, goal=31, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (5, 20).
          Player 0 rolls 1 dice and gets outcomes [5].
          End scores = (10, 20)
          >>> print(turns[1])
          Start scores = (10, 20).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 3, 5, 2, 6, 1, 3, 2].
          End scores = (10, 21)
          >>> print(turns[2])
          Start scores = (10, 21).
          Player 0 rolls 7 dice and gets outcomes [3, 2, 6, 5, 3, 4, 5].
          End scores = (38, 21)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=71578, score0=16, score1=49, goal=81, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (16, 49).
          Player 0 rolls 6 dice and gets outcomes [4, 3, 2, 1, 6, 3].
          End scores = (17, 49)
          >>> print(turns[1])
          Start scores = (17, 49).
          Player 1 rolls 10 dice and gets outcomes [6, 3, 6, 6, 2, 1, 2, 6, 3, 1].
          End scores = (17, 60)
          >>> print(turns[2])
          Start scores = (17, 60).
          Player 0 rolls 10 dice and gets outcomes [2, 5, 3, 5, 3, 3, 1, 3, 3, 5].
          End scores = (18, 60)
          >>> print(turns[3])
          Start scores = (18, 60).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 2].
          End scores = (18, 69)
          >>> print(turns[4])
          Start scores = (18, 69).
          Player 0 rolls 9 dice and gets outcomes [6, 3, 5, 5, 4, 3, 6, 1, 5].
          End scores = (19, 69)
          >>> print(turns[5])
          Start scores = (19, 69).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (19, 72)
          >>> print(turns[6])
          Start scores = (19, 72).
          Player 0 rolls 2 dice and gets outcomes [2, 2].
          End scores = (23, 72)
          >>> print(turns[7])
          Start scores = (23, 72).
          Player 1 rolls 9 dice and gets outcomes [2, 4, 6, 3, 6, 6, 5, 5, 5].
          End scores = (23, 114)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=72869, score0=5, score1=4, goal=11, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (5, 4).
          Player 0 rolls 2 dice and gets outcomes [3, 1].
          End scores = (6, 4)
          >>> print(turns[1])
          Start scores = (6, 4).
          Player 1 rolls 4 dice and gets outcomes [5, 4, 4, 4].
          End scores = (6, 21)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=66473, score0=39, score1=74, goal=81, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (39, 74).
          Player 0 rolls 6 dice and gets outcomes [5, 3, 3, 1, 5, 4].
          End scores = (40, 74)
          >>> print(turns[1])
          Start scores = (40, 74).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 1].
          End scores = (40, 75)
          >>> print(turns[2])
          Start scores = (40, 75).
          Player 0 rolls 4 dice and gets outcomes [6, 3, 4, 5].
          End scores = (58, 75)
          >>> print(turns[3])
          Start scores = (58, 75).
          Player 1 rolls 5 dice and gets outcomes [4, 4, 5, 2, 3].
          End scores = (58, 93)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=43296, score0=56, score1=14, goal=69, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (56, 14).
          Player 0 rolls 5 dice and gets outcomes [5, 3, 1, 4, 5].
          End scores = (57, 14)
          >>> print(turns[1])
          Start scores = (57, 14).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (57, 17)
          >>> print(turns[2])
          Start scores = (57, 17).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (65, 17)
          >>> print(turns[3])
          Start scores = (65, 17).
          Player 1 rolls 8 dice and gets outcomes [1, 4, 5, 6, 4, 6, 4, 3].
          End scores = (65, 18)
          >>> print(turns[4])
          Start scores = (65, 18).
          Player 0 rolls 2 dice and gets outcomes [4, 6].
          End scores = (79, 18)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=15289, score0=61, score1=5, goal=69, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (61, 5).
          Player 0 rolls 5 dice and gets outcomes [6, 4, 6, 5, 4].
          End scores = (86, 5)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=13609, score0=14, score1=0, goal=15, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (14, 0).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (26, 0)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=99130, score0=70, score1=53, goal=72, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (70, 53).
          Player 0 rolls 2 dice and gets outcomes [5, 3].
          End scores = (78, 53)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=32108, score0=9, score1=37, goal=93, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (9, 37).
          Player 0 rolls 9 dice and gets outcomes [1, 2, 1, 2, 2, 5, 2, 6, 5].
          End scores = (10, 37)
          >>> print(turns[1])
          Start scores = (10, 37).
          Player 1 rolls 4 dice and gets outcomes [4, 2, 6, 4].
          End scores = (10, 53)
          >>> print(turns[2])
          Start scores = (10, 53).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (29, 53)
          >>> print(turns[3])
          Start scores = (29, 53).
          Player 1 rolls 7 dice and gets outcomes [3, 6, 6, 2, 1, 4, 5].
          End scores = (29, 54)
          >>> print(turns[4])
          Start scores = (29, 54).
          Player 0 rolls 8 dice and gets outcomes [2, 2, 1, 5, 1, 4, 6, 3].
          End scores = (30, 54)
          >>> print(turns[5])
          Start scores = (30, 54).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 4, 4, 2].
          End scores = (30, 72)
          >>> print(turns[6])
          Start scores = (30, 72).
          Player 0 rolls 9 dice and gets outcomes [2, 1, 3, 5, 1, 2, 3, 4, 2].
          End scores = (31, 72)
          >>> print(turns[7])
          Start scores = (31, 72).
          Player 1 rolls 9 dice and gets outcomes [1, 2, 3, 3, 6, 5, 3, 5, 4].
          End scores = (31, 73)
          >>> print(turns[8])
          Start scores = (31, 73).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 1, 2, 2, 6, 2, 2, 2].
          End scores = (32, 73)
          >>> print(turns[9])
          Start scores = (32, 73).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (32, 74)
          >>> print(turns[10])
          Start scores = (32, 74).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 1, 4, 4, 4, 4, 2, 2].
          End scores = (33, 74)
          >>> print(turns[11])
          Start scores = (33, 74).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 3, 6, 1].
          End scores = (33, 79)
          >>> print(turns[12])
          Start scores = (33, 79).
          Player 0 rolls 8 dice and gets outcomes [2, 1, 6, 3, 5, 5, 5, 3].
          End scores = (34, 79)
          >>> print(turns[13])
          Start scores = (34, 79).
          Player 1 rolls 6 dice and gets outcomes [5, 6, 3, 2, 4, 3].
          End scores = (34, 102)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=2069, score0=55, score1=37, goal=64, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (55, 37).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 2, 5, 5, 6, 5, 4, 1].
          End scores = (56, 37)
          >>> print(turns[1])
          Start scores = (56, 37).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 2].
          End scores = (56, 45)
          >>> print(turns[2])
          Start scores = (56, 45).
          Player 0 rolls 9 dice and gets outcomes [6, 1, 1, 3, 5, 5, 1, 1, 5].
          End scores = (57, 45)
          >>> print(turns[3])
          Start scores = (57, 45).
          Player 1 rolls 4 dice and gets outcomes [5, 4, 6, 2].
          End scores = (57, 62)
          >>> print(turns[4])
          Start scores = (57, 62).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (60, 62)
          >>> print(turns[5])
          Start scores = (60, 62).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (60, 65)
          >>> print(turns[6])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=39055, score0=54, score1=8, goal=64, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (54, 8).
          Player 0 rolls 6 dice and gets outcomes [5, 6, 3, 4, 5, 5].
          End scores = (82, 8)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=65291, score0=4, score1=3, goal=23, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (4, 3).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (16, 3)
          >>> print(turns[1])
          Start scores = (16, 3).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 1].
          End scores = (16, 4)
          >>> print(turns[2])
          Start scores = (16, 4).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 4)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=76703, score0=25, score1=24, goal=76, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (25, 24).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 24)
          >>> print(turns[1])
          Start scores = (34, 24).
          Player 1 rolls 8 dice and gets outcomes [4, 6, 5, 5, 3, 6, 2, 6].
          End scores = (34, 61)
          >>> print(turns[2])
          Start scores = (34, 61).
          Player 0 rolls 4 dice and gets outcomes [3, 4, 6, 4].
          End scores = (51, 61)
          >>> print(turns[3])
          Start scores = (51, 61).
          Player 1 rolls 3 dice and gets outcomes [3, 2, 5].
          End scores = (51, 71)
          >>> print(turns[4])
          Start scores = (51, 71).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 1, 5, 5, 5, 1].
          End scores = (52, 71)
          >>> print(turns[5])
          Start scores = (52, 71).
          Player 1 rolls 7 dice and gets outcomes [3, 1, 4, 2, 6, 3, 5].
          End scores = (52, 72)
          >>> print(turns[6])
          Start scores = (52, 72).
          Player 0 rolls 8 dice and gets outcomes [5, 6, 3, 2, 3, 6, 1, 4].
          End scores = (53, 72)
          >>> print(turns[7])
          Start scores = (53, 72).
          Player 1 rolls 9 dice and gets outcomes [2, 5, 1, 3, 4, 6, 5, 1, 4].
          End scores = (53, 73)
          >>> print(turns[8])
          Start scores = (53, 73).
          Player 0 rolls 8 dice and gets outcomes [2, 4, 2, 1, 3, 5, 2, 5].
          End scores = (54, 73)
          >>> print(turns[9])
          Start scores = (54, 73).
          Player 1 rolls 6 dice and gets outcomes [6, 5, 5, 5, 6, 1].
          End scores = (54, 74)
          >>> print(turns[10])
          Start scores = (54, 74).
          Player 0 rolls 2 dice and gets outcomes [1, 4].
          End scores = (55, 74)
          >>> print(turns[11])
          Start scores = (55, 74).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (55, 79)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27707, score0=55, score1=8, goal=66, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (55, 8).
          Player 0 rolls 8 dice and gets outcomes [5, 1, 5, 6, 5, 4, 1, 4].
          End scores = (56, 8)
          >>> print(turns[1])
          Start scores = (56, 8).
          Player 1 rolls 8 dice and gets outcomes [6, 3, 1, 6, 5, 2, 1, 1].
          End scores = (56, 9)
          >>> print(turns[2])
          Start scores = (56, 9).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (58, 9)
          >>> print(turns[3])
          Start scores = (58, 9).
          Player 1 rolls 3 dice and gets outcomes [3, 1, 2].
          End scores = (58, 10)
          >>> print(turns[4])
          Start scores = (58, 10).
          Player 0 rolls 8 dice and gets outcomes [6, 2, 3, 5, 4, 2, 2, 5].
          End scores = (87, 10)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=95614, score0=21, score1=52, goal=74, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (21, 52).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 4, 5].
          End scores = (39, 52)
          >>> print(turns[1])
          Start scores = (39, 52).
          Player 1 rolls 8 dice and gets outcomes [6, 2, 6, 4, 3, 1, 3, 6].
          End scores = (39, 53)
          >>> print(turns[2])
          Start scores = (39, 53).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (41, 53)
          >>> print(turns[3])
          Start scores = (41, 53).
          Player 1 rolls 2 dice and gets outcomes [5, 1].
          End scores = (41, 54)
          >>> print(turns[4])
          Start scores = (41, 54).
          Player 0 rolls 3 dice and gets outcomes [5, 6, 2].
          End scores = (54, 54)
          >>> print(turns[5])
          Start scores = (54, 54).
          Player 1 rolls 5 dice and gets outcomes [3, 2, 4, 1, 4].
          End scores = (54, 55)
          >>> print(turns[6])
          Start scores = (54, 55).
          Player 0 rolls 6 dice and gets outcomes [1, 4, 6, 3, 3, 2].
          End scores = (55, 55)
          >>> print(turns[7])
          Start scores = (55, 55).
          Player 1 rolls 6 dice and gets outcomes [5, 2, 5, 5, 5, 4].
          End scores = (55, 81)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59761, score0=37, score1=12, goal=81, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (37, 12).
          Player 0 rolls 9 dice and gets outcomes [5, 2, 6, 2, 5, 1, 4, 3, 5].
          End scores = (38, 12)
          >>> print(turns[1])
          Start scores = (38, 12).
          Player 1 rolls 7 dice and gets outcomes [5, 5, 4, 3, 2, 1, 6].
          End scores = (38, 13)
          >>> print(turns[2])
          Start scores = (38, 13).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 6, 5].
          End scores = (58, 13)
          >>> print(turns[3])
          Start scores = (58, 13).
          Player 1 rolls 2 dice and gets outcomes [5, 5].
          End scores = (58, 23)
          >>> print(turns[4])
          Start scores = (58, 23).
          Player 0 rolls 4 dice and gets outcomes [5, 2, 1, 4].
          End scores = (59, 23)
          >>> print(turns[5])
          Start scores = (59, 23).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (59, 25)
          >>> print(turns[6])
          Start scores = (59, 25).
          Player 0 rolls 2 dice and gets outcomes [2, 4].
          End scores = (65, 25)
          >>> print(turns[7])
          Start scores = (65, 25).
          Player 1 rolls 4 dice and gets outcomes [2, 3, 3, 3].
          End scores = (65, 36)
          >>> print(turns[8])
          Start scores = (65, 36).
          Player 0 rolls 5 dice and gets outcomes [5, 5, 6, 5, 5].
          End scores = (91, 36)
          >>> print(turns[9])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=12023, score0=20, score1=6, goal=42, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (20, 6).
          Player 0 rolls 4 dice and gets outcomes [1, 1, 5, 2].
          End scores = (21, 6)
          >>> print(turns[1])
          Start scores = (21, 6).
          Player 1 rolls 10 dice and gets outcomes [6, 1, 2, 6, 2, 3, 5, 5, 5, 3].
          End scores = (21, 7)
          >>> print(turns[2])
          Start scores = (21, 7).
          Player 0 rolls 2 dice and gets outcomes [2, 4].
          End scores = (27, 7)
          >>> print(turns[3])
          Start scores = (27, 7).
          Player 1 rolls 7 dice and gets outcomes [3, 5, 5, 5, 1, 3, 5].
          End scores = (27, 8)
          >>> print(turns[4])
          Start scores = (27, 8).
          Player 0 rolls 4 dice and gets outcomes [1, 4, 2, 5].
          End scores = (28, 8)
          >>> print(turns[5])
          Start scores = (28, 8).
          Player 1 rolls 7 dice and gets outcomes [4, 6, 2, 3, 6, 4, 4].
          End scores = (28, 37)
          >>> print(turns[6])
          Start scores = (28, 37).
          Player 0 rolls 2 dice and gets outcomes [1, 6].
          End scores = (29, 37)
          >>> print(turns[7])
          Start scores = (29, 37).
          Player 1 rolls 5 dice and gets outcomes [4, 2, 5, 1, 4].
          End scores = (29, 38)
          >>> print(turns[8])
          Start scores = (29, 38).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (33, 38)
          >>> print(turns[9])
          Start scores = (33, 38).
          Player 1 rolls 3 dice and gets outcomes [6, 1, 1].
          End scores = (33, 39)
          >>> print(turns[10])
          Start scores = (33, 39).
          Player 0 rolls 2 dice and gets outcomes [1, 2].
          End scores = (34, 39)
          >>> print(turns[11])
          Start scores = (34, 39).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 1, 2, 1, 2, 1].
          End scores = (34, 40)
          >>> print(turns[12])
          Start scores = (34, 40).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (38, 40)
          >>> print(turns[13])
          Start scores = (38, 40).
          Player 1 rolls 10 dice and gets outcomes [1, 4, 4, 1, 2, 1, 4, 1, 5, 1].
          End scores = (38, 41)
          >>> print(turns[14])
          Start scores = (38, 41).
          Player 0 rolls 6 dice and gets outcomes [1, 5, 3, 5, 2, 5].
          End scores = (39, 41)
          >>> print(turns[15])
          Start scores = (39, 41).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (39, 42)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=9065, score0=45, score1=30, goal=46, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (45, 30).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (47, 30)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=52376, score0=72, score1=18, goal=75, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (72, 18).
          Player 0 rolls 4 dice and gets outcomes [4, 4, 5, 3].
          End scores = (88, 18)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=47323, score0=23, score1=6, goal=92, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (23, 6).
          Player 0 rolls 2 dice and gets outcomes [4, 1].
          End scores = (24, 6)
          >>> print(turns[1])
          Start scores = (24, 6).
          Player 1 rolls 6 dice and gets outcomes [4, 1, 6, 2, 5, 4].
          End scores = (24, 7)
          >>> print(turns[2])
          Start scores = (24, 7).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 5, 2, 4, 5, 4].
          End scores = (49, 7)
          >>> print(turns[3])
          Start scores = (49, 7).
          Player 1 rolls 9 dice and gets outcomes [3, 4, 2, 5, 6, 5, 6, 2, 4].
          End scores = (49, 44)
          >>> print(turns[4])
          Start scores = (49, 44).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 6, 2, 1, 1, 2].
          End scores = (50, 44)
          >>> print(turns[5])
          Start scores = (50, 44).
          Player 1 rolls 9 dice and gets outcomes [5, 4, 3, 1, 4, 1, 1, 1, 4].
          End scores = (50, 45)
          >>> print(turns[6])
          Start scores = (50, 45).
          Player 0 rolls 6 dice and gets outcomes [6, 4, 4, 2, 6, 5].
          End scores = (77, 45)
          >>> print(turns[7])
          Start scores = (77, 45).
          Player 1 rolls 4 dice and gets outcomes [6, 1, 1, 6].
          End scores = (77, 46)
          >>> print(turns[8])
          Start scores = (77, 46).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 1, 4, 5, 3, 1].
          End scores = (78, 46)
          >>> print(turns[9])
          Start scores = (78, 46).
          Player 1 rolls 3 dice and gets outcomes [5, 5, 5].
          End scores = (78, 61)
          >>> print(turns[10])
          Start scores = (78, 61).
          Player 0 rolls 3 dice and gets outcomes [1, 4, 1].
          End scores = (79, 61)
          >>> print(turns[11])
          Start scores = (79, 61).
          Player 1 rolls 7 dice and gets outcomes [2, 5, 3, 5, 3, 1, 5].
          End scores = (79, 62)
          >>> print(turns[12])
          Start scores = (79, 62).
          Player 0 rolls 9 dice and gets outcomes [2, 1, 2, 4, 6, 1, 2, 5, 4].
          End scores = (80, 62)
          >>> print(turns[13])
          Start scores = (80, 62).
          Player 1 rolls 3 dice and gets outcomes [6, 3, 4].
          End scores = (80, 75)
          >>> print(turns[14])
          Start scores = (80, 75).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 1, 2, 2, 3, 1].
          End scores = (81, 75)
          >>> print(turns[15])
          Start scores = (81, 75).
          Player 1 rolls 7 dice and gets outcomes [4, 3, 3, 3, 4, 6, 4].
          End scores = (81, 102)
          >>> print(turns[16])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=44237, score0=12, score1=79, goal=89, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (12, 79).
          Player 0 rolls 3 dice and gets outcomes [3, 3, 4].
          End scores = (22, 79)
          >>> print(turns[1])
          Start scores = (22, 79).
          Player 1 rolls 5 dice and gets outcomes [5, 4, 3, 6, 3].
          End scores = (22, 100)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27065, score0=2, score1=0, goal=12, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (2, 0).
          Player 0 rolls 5 dice and gets outcomes [5, 2, 2, 1, 3].
          End scores = (3, 0)
          >>> print(turns[1])
          Start scores = (3, 0).
          Player 1 rolls 3 dice and gets outcomes [2, 1, 3].
          End scores = (3, 1)
          >>> print(turns[2])
          Start scores = (3, 1).
          Player 0 rolls 6 dice and gets outcomes [4, 5, 2, 2, 4, 3].
          End scores = (23, 1)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=37376, score0=71, score1=22, goal=97, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (71, 22).
          Player 0 rolls 5 dice and gets outcomes [6, 3, 1, 2, 5].
          End scores = (72, 22)
          >>> print(turns[1])
          Start scores = (72, 22).
          Player 1 rolls 3 dice and gets outcomes [3, 6, 6].
          End scores = (72, 37)
          >>> print(turns[2])
          Start scores = (72, 37).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 5, 3, 2, 2, 2, 5, 4].
          End scores = (103, 37)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=97077, score0=13, score1=2, goal=17, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (13, 2).
          Player 0 rolls 10 dice and gets outcomes [1, 5, 3, 4, 3, 1, 5, 5, 1, 6].
          End scores = (14, 2)
          >>> print(turns[1])
          Start scores = (14, 2).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (14, 5)
          >>> print(turns[2])
          Start scores = (14, 5).
          Player 0 rolls 10 dice and gets outcomes [6, 4, 1, 2, 2, 2, 5, 6, 1, 6].
          End scores = (15, 5)
          >>> print(turns[3])
          Start scores = (15, 5).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 3, 2, 5, 5, 3].
          End scores = (15, 32)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=66508, score0=38, score1=25, goal=97, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (38, 25).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (44, 25)
          >>> print(turns[1])
          Start scores = (44, 25).
          Player 1 rolls 4 dice and gets outcomes [4, 4, 2, 3].
          End scores = (44, 38)
          >>> print(turns[2])
          Start scores = (44, 38).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (47, 38)
          >>> print(turns[3])
          Start scores = (47, 38).
          Player 1 rolls 1 dice and gets outcomes [1].
          End scores = (47, 39)
          >>> print(turns[4])
          Start scores = (47, 39).
          Player 0 rolls 5 dice and gets outcomes [5, 3, 4, 2, 4].
          End scores = (65, 39)
          >>> print(turns[5])
          Start scores = (65, 39).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (65, 42)
          >>> print(turns[6])
          Start scores = (65, 42).
          Player 0 rolls 7 dice and gets outcomes [1, 6, 2, 5, 2, 2, 2].
          End scores = (66, 42)
          >>> print(turns[7])
          Start scores = (66, 42).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (66, 48)
          >>> print(turns[8])
          Start scores = (66, 48).
          Player 0 rolls 3 dice and gets outcomes [4, 3, 3].
          End scores = (76, 48)
          >>> print(turns[9])
          Start scores = (76, 48).
          Player 1 rolls 7 dice and gets outcomes [6, 1, 6, 6, 6, 1, 1].
          End scores = (76, 49)
          >>> print(turns[10])
          Start scores = (76, 49).
          Player 0 rolls 2 dice and gets outcomes [2, 2].
          End scores = (84, 49)
          >>> print(turns[11])
          Start scores = (84, 49).
          Player 1 rolls 7 dice and gets outcomes [2, 3, 6, 4, 5, 3, 2].
          End scores = (84, 74)
          >>> print(turns[12])
          Start scores = (84, 74).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 3, 5, 3].
          End scores = (85, 74)
          >>> print(turns[13])
          Start scores = (85, 74).
          Player 1 rolls 7 dice and gets outcomes [2, 6, 3, 6, 3, 1, 4].
          End scores = (85, 79)
          >>> print(turns[14])
          Start scores = (85, 79).
          Player 0 rolls 5 dice and gets outcomes [3, 4, 3, 4, 2].
          End scores = (101, 79)
          >>> print(turns[15])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75418, score0=2, score1=5, goal=11, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (2, 5).
          Player 0 rolls 2 dice and gets outcomes [4, 4].
          End scores = (10, 5)
          >>> print(turns[1])
          Start scores = (10, 5).
          Player 1 rolls 7 dice and gets outcomes [6, 3, 6, 1, 4, 6, 5].
          End scores = (10, 6)
          >>> print(turns[2])
          Start scores = (10, 6).
          Player 0 rolls 7 dice and gets outcomes [6, 1, 6, 5, 2, 2, 1].
          End scores = (11, 6)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=68629, score0=17, score1=25, goal=47, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (17, 25).
          Player 0 rolls 4 dice and gets outcomes [2, 6, 2, 1].
          End scores = (18, 25)
          >>> print(turns[1])
          Start scores = (18, 25).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (18, 37)
          >>> print(turns[2])
          Start scores = (18, 37).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 1, 1, 1, 5, 5, 3].
          End scores = (19, 37)
          >>> print(turns[3])
          Start scores = (19, 37).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (19, 55)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=1568, score0=3, score1=29, goal=51, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (3, 29).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (7, 29)
          >>> print(turns[1])
          Start scores = (7, 29).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (7, 56)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=72434, score0=8, score1=45, goal=67, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (8, 45).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 6, 6, 6, 3, 5, 4].
          End scores = (9, 45)
          >>> print(turns[1])
          Start scores = (9, 45).
          Player 1 rolls 4 dice and gets outcomes [3, 3, 4, 4].
          End scores = (9, 59)
          >>> print(turns[2])
          Start scores = (9, 59).
          Player 0 rolls 9 dice and gets outcomes [3, 2, 5, 5, 1, 6, 4, 3, 3].
          End scores = (10, 59)
          >>> print(turns[3])
          Start scores = (10, 59).
          Player 1 rolls 5 dice and gets outcomes [5, 6, 6, 6, 5].
          End scores = (10, 87)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55979, score0=75, score1=80, goal=95, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (75, 80).
          Player 0 rolls 4 dice and gets outcomes [4, 1, 6, 4].
          End scores = (76, 80)
          >>> print(turns[1])
          Start scores = (76, 80).
          Player 1 rolls 4 dice and gets outcomes [3, 1, 1, 3].
          End scores = (76, 81)
          >>> print(turns[2])
          Start scores = (76, 81).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 6].
          End scores = (89, 81)
          >>> print(turns[3])
          Start scores = (89, 81).
          Player 1 rolls 4 dice and gets outcomes [3, 2, 5, 5].
          End scores = (89, 96)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=93729, score0=37, score1=63, goal=83, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (37, 63).
          Player 0 rolls 8 dice and gets outcomes [3, 1, 1, 4, 5, 5, 1, 5].
          End scores = (38, 63)
          >>> print(turns[1])
          Start scores = (38, 63).
          Player 1 rolls 6 dice and gets outcomes [2, 5, 1, 3, 3, 5].
          End scores = (38, 64)
          >>> print(turns[2])
          Start scores = (38, 64).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 6, 5, 3, 3, 3, 3].
          End scores = (67, 64)
          >>> print(turns[3])
          Start scores = (67, 64).
          Player 1 rolls 5 dice and gets outcomes [5, 3, 2, 5, 6].
          End scores = (67, 85)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=53739, score0=54, score1=50, goal=58, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (54, 50).
          Player 0 rolls 9 dice and gets outcomes [4, 3, 5, 6, 3, 2, 3, 4, 2].
          End scores = (86, 50)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=30305, score0=21, score1=1, goal=55, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (21, 1).
          Player 0 rolls 6 dice and gets outcomes [1, 6, 5, 2, 2, 5].
          End scores = (22, 1)
          >>> print(turns[1])
          Start scores = (22, 1).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (22, 4)
          >>> print(turns[2])
          Start scores = (22, 4).
          Player 0 rolls 5 dice and gets outcomes [6, 4, 6, 4, 1].
          End scores = (23, 4)
          >>> print(turns[3])
          Start scores = (23, 4).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (23, 10)
          >>> print(turns[4])
          Start scores = (23, 10).
          Player 0 rolls 7 dice and gets outcomes [3, 3, 5, 3, 2, 1, 6].
          End scores = (24, 10)
          >>> print(turns[5])
          Start scores = (24, 10).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 4, 3, 6].
          End scores = (24, 33)
          >>> print(turns[6])
          Start scores = (24, 33).
          Player 0 rolls 9 dice and gets outcomes [3, 4, 1, 5, 4, 6, 3, 1, 4].
          End scores = (29, 33)
          >>> print(turns[7])
          Start scores = (29, 33).
          Player 1 rolls 4 dice and gets outcomes [3, 4, 2, 1].
          End scores = (29, 34)
          >>> print(turns[8])
          Start scores = (29, 34).
          Player 0 rolls 3 dice and gets outcomes [5, 2, 3].
          End scores = (39, 34)
          >>> print(turns[9])
          Start scores = (39, 34).
          Player 1 rolls 6 dice and gets outcomes [4, 3, 4, 5, 3, 5].
          End scores = (39, 58)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=63941, score0=1, score1=44, goal=73, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (1, 44).
          Player 0 rolls 6 dice and gets outcomes [2, 1, 1, 5, 1, 6].
          End scores = (2, 44)
          >>> print(turns[1])
          Start scores = (2, 44).
          Player 1 rolls 9 dice and gets outcomes [5, 2, 3, 5, 1, 1, 5, 5, 1].
          End scores = (2, 45)
          >>> print(turns[2])
          Start scores = (2, 45).
          Player 0 rolls 8 dice and gets outcomes [5, 4, 3, 4, 3, 1, 2, 2].
          End scores = (3, 45)
          >>> print(turns[3])
          Start scores = (3, 45).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (3, 60)
          >>> print(turns[4])
          Start scores = (3, 60).
          Player 0 rolls 9 dice and gets outcomes [2, 6, 5, 5, 2, 2, 3, 2, 1].
          End scores = (4, 60)
          >>> print(turns[5])
          Start scores = (4, 60).
          Player 1 rolls 2 dice and gets outcomes [4, 3].
          End scores = (4, 67)
          >>> print(turns[6])
          Start scores = (4, 67).
          Player 0 rolls 8 dice and gets outcomes [6, 6, 4, 5, 3, 3, 4, 3].
          End scores = (38, 67)
          >>> print(turns[7])
          Start scores = (38, 67).
          Player 1 rolls 5 dice and gets outcomes [2, 6, 5, 6, 6].
          End scores = (38, 92)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=55351, score0=33, score1=18, goal=69, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (33, 18).
          Player 0 rolls 7 dice and gets outcomes [5, 2, 1, 2, 3, 5, 1].
          End scores = (34, 18)
          >>> print(turns[1])
          Start scores = (34, 18).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 2, 2, 2, 2, 2, 5, 6, 2].
          End scores = (34, 49)
          >>> print(turns[2])
          Start scores = (34, 49).
          Player 0 rolls 1 dice and gets outcomes [2].
          End scores = (36, 49)
          >>> print(turns[3])
          Start scores = (36, 49).
          Player 1 rolls 1 dice and gets outcomes [5].
          End scores = (36, 54)
          >>> print(turns[4])
          Start scores = (36, 54).
          Player 0 rolls 7 dice and gets outcomes [3, 1, 1, 5, 2, 2, 6].
          End scores = (37, 54)
          >>> print(turns[5])
          Start scores = (37, 54).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (37, 57)
          >>> print(turns[6])
          Start scores = (37, 57).
          Player 0 rolls 2 dice and gets outcomes [5, 6].
          End scores = (48, 57)
          >>> print(turns[7])
          Start scores = (48, 57).
          Player 1 rolls 4 dice and gets outcomes [1, 2, 4, 2].
          End scores = (48, 58)
          >>> print(turns[8])
          Start scores = (48, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (57, 58)
          >>> print(turns[9])
          Start scores = (57, 58).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (57, 67)
          >>> print(turns[10])
          Start scores = (57, 67).
          Player 0 rolls 3 dice and gets outcomes [3, 6, 1].
          End scores = (58, 67)
          >>> print(turns[11])
          Start scores = (58, 67).
          Player 1 rolls 6 dice and gets outcomes [1, 2, 2, 2, 5, 6].
          End scores = (58, 68)
          >>> print(turns[12])
          Start scores = (58, 68).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 6, 3, 6, 2, 3, 2, 1].
          End scores = (59, 68)
          >>> print(turns[13])
          Start scores = (59, 68).
          Player 1 rolls 6 dice and gets outcomes [1, 3, 6, 4, 3, 3].
          End scores = (59, 69)
          >>> print(turns[14])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50979, score0=50, score1=2, goal=56, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (50, 2).
          Player 0 rolls 5 dice and gets outcomes [6, 2, 3, 4, 5].
          End scores = (70, 2)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=64647, score0=11, score1=5, goal=33, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (11, 5).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (12, 5)
          >>> print(turns[1])
          Start scores = (12, 5).
          Player 1 rolls 9 dice and gets outcomes [6, 6, 6, 6, 2, 3, 4, 6, 3].
          End scores = (12, 47)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=87563, score0=63, score1=55, goal=90, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (63, 55).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (69, 55)
          >>> print(turns[1])
          Start scores = (69, 55).
          Player 1 rolls 10 dice and gets outcomes [5, 5, 4, 2, 4, 6, 2, 5, 6, 6].
          End scores = (69, 100)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=46403, score0=9, score1=12, goal=13, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (9, 12).
          Player 0 rolls 9 dice and gets outcomes [4, 6, 3, 2, 3, 2, 6, 4, 1].
          End scores = (10, 12)
          >>> print(turns[1])
          Start scores = (10, 12).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 6, 3, 4, 3, 3].
          End scores = (10, 13)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=77217, score0=2, score1=39, goal=83, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (2, 39).
          Player 0 rolls 3 dice and gets outcomes [6, 4, 6].
          End scores = (18, 39)
          >>> print(turns[1])
          Start scores = (18, 39).
          Player 1 rolls 10 dice and gets outcomes [4, 4, 5, 1, 2, 3, 3, 5, 6, 3].
          End scores = (18, 44)
          >>> print(turns[2])
          Start scores = (18, 44).
          Player 0 rolls 10 dice and gets outcomes [3, 6, 6, 3, 3, 2, 2, 5, 5, 4].
          End scores = (57, 44)
          >>> print(turns[3])
          Start scores = (57, 44).
          Player 1 rolls 5 dice and gets outcomes [3, 4, 4, 6, 6].
          End scores = (57, 67)
          >>> print(turns[4])
          Start scores = (57, 67).
          Player 0 rolls 3 dice and gets outcomes [6, 1, 1].
          End scores = (58, 67)
          >>> print(turns[5])
          Start scores = (58, 67).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (58, 73)
          >>> print(turns[6])
          Start scores = (58, 73).
          Player 0 rolls 6 dice and gets outcomes [6, 6, 5, 3, 3, 5].
          End scores = (86, 73)
          >>> print(turns[7])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=32342, score0=1, score1=1, goal=15, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (1, 1).
          Player 0 rolls 5 dice and gets outcomes [5, 4, 1, 6, 1].
          End scores = (2, 1)
          >>> print(turns[1])
          Start scores = (2, 1).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (2, 7)
          >>> print(turns[2])
          Start scores = (2, 7).
          Player 0 rolls 8 dice and gets outcomes [5, 3, 4, 6, 4, 3, 1, 1].
          End scores = (3, 7)
          >>> print(turns[3])
          Start scores = (3, 7).
          Player 1 rolls 6 dice and gets outcomes [1, 4, 1, 6, 6, 6].
          End scores = (3, 8)
          >>> print(turns[4])
          Start scores = (3, 8).
          Player 0 rolls 7 dice and gets outcomes [5, 3, 3, 6, 5, 5, 3].
          End scores = (33, 8)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=81605, score0=73, score1=74, goal=91, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (73, 74).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (77, 74)
          >>> print(turns[1])
          Start scores = (77, 74).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (77, 83)
          >>> print(turns[2])
          Start scores = (77, 83).
          Player 0 rolls 10 dice and gets outcomes [3, 4, 5, 2, 6, 5, 6, 2, 6, 4].
          End scores = (124, 83)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=25561, score0=69, score1=44, goal=89, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (69, 44).
          Player 0 rolls 4 dice and gets outcomes [5, 6, 3, 1].
          End scores = (70, 44)
          >>> print(turns[1])
          Start scores = (70, 44).
          Player 1 rolls 3 dice and gets outcomes [3, 4, 1].
          End scores = (70, 45)
          >>> print(turns[2])
          Start scores = (70, 45).
          Player 0 rolls 9 dice and gets outcomes [6, 2, 3, 4, 5, 1, 3, 1, 3].
          End scores = (71, 45)
          >>> print(turns[3])
          Start scores = (71, 45).
          Player 1 rolls 10 dice and gets outcomes [4, 2, 6, 4, 4, 5, 1, 5, 1, 1].
          End scores = (71, 46)
          >>> print(turns[4])
          Start scores = (71, 46).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (80, 46)
          >>> print(turns[5])
          Start scores = (80, 46).
          Player 1 rolls 2 dice and gets outcomes [3, 2].
          End scores = (80, 51)
          >>> print(turns[6])
          Start scores = (80, 51).
          Player 0 rolls 10 dice and gets outcomes [6, 3, 5, 1, 1, 2, 4, 4, 6, 6].
          End scores = (81, 51)
          >>> print(turns[7])
          Start scores = (81, 51).
          Player 1 rolls 2 dice and gets outcomes [6, 5].
          End scores = (81, 62)
          >>> print(turns[8])
          Start scores = (81, 62).
          Player 0 rolls 6 dice and gets outcomes [1, 5, 3, 4, 3, 6].
          End scores = (82, 62)
          >>> print(turns[9])
          Start scores = (82, 62).
          Player 1 rolls 8 dice and gets outcomes [5, 1, 5, 6, 4, 1, 6, 3].
          End scores = (82, 63)
          >>> print(turns[10])
          Start scores = (82, 63).
          Player 0 rolls 9 dice and gets outcomes [6, 5, 2, 1, 5, 5, 5, 2, 4].
          End scores = (83, 63)
          >>> print(turns[11])
          Start scores = (83, 63).
          Player 1 rolls 6 dice and gets outcomes [2, 3, 2, 3, 5, 5].
          End scores = (83, 83)
          >>> print(turns[12])
          Start scores = (83, 83).
          Player 0 rolls 2 dice and gets outcomes [2, 5].
          End scores = (90, 83)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=599, score0=3, score1=0, goal=14, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (3, 0).
          Player 0 rolls 7 dice and gets outcomes [2, 3, 2, 4, 1, 2, 6].
          End scores = (4, 0)
          >>> print(turns[1])
          Start scores = (4, 0).
          Player 1 rolls 4 dice and gets outcomes [3, 4, 5, 2].
          End scores = (4, 14)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=59603, score0=27, score1=58, goal=90, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (27, 58).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (33, 58)
          >>> print(turns[1])
          Start scores = (33, 58).
          Player 1 rolls 5 dice and gets outcomes [2, 1, 2, 1, 6].
          End scores = (33, 59)
          >>> print(turns[2])
          Start scores = (33, 59).
          Player 0 rolls 5 dice and gets outcomes [4, 2, 1, 6, 5].
          End scores = (34, 59)
          >>> print(turns[3])
          Start scores = (34, 59).
          Player 1 rolls 5 dice and gets outcomes [5, 5, 3, 4, 2].
          End scores = (34, 78)
          >>> print(turns[4])
          Start scores = (34, 78).
          Player 0 rolls 5 dice and gets outcomes [4, 1, 4, 3, 5].
          End scores = (35, 78)
          >>> print(turns[5])
          Start scores = (35, 78).
          Player 1 rolls 2 dice and gets outcomes [3, 2].
          End scores = (35, 83)
          >>> print(turns[6])
          Start scores = (35, 83).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 5, 2, 5, 1, 5, 1, 1, 1].
          End scores = (36, 83)
          >>> print(turns[7])
          Start scores = (36, 83).
          Player 1 rolls 10 dice and gets outcomes [6, 1, 3, 4, 1, 5, 6, 2, 6, 3].
          End scores = (36, 84)
          >>> print(turns[8])
          Start scores = (36, 84).
          Player 0 rolls 4 dice and gets outcomes [2, 3, 2, 3].
          End scores = (46, 84)
          >>> print(turns[9])
          Start scores = (46, 84).
          Player 1 rolls 10 dice and gets outcomes [6, 5, 5, 6, 1, 6, 4, 1, 1, 4].
          End scores = (46, 85)
          >>> print(turns[10])
          Start scores = (46, 85).
          Player 0 rolls 4 dice and gets outcomes [2, 4, 5, 4].
          End scores = (61, 85)
          >>> print(turns[11])
          Start scores = (61, 85).
          Player 1 rolls 4 dice and gets outcomes [6, 6, 4, 4].
          End scores = (61, 105)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=29427, score0=18, score1=35, goal=56, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (18, 35).
          Player 0 rolls 7 dice and gets outcomes [6, 4, 3, 1, 5, 5, 4].
          End scores = (19, 35)
          >>> print(turns[1])
          Start scores = (19, 35).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (19, 47)
          >>> print(turns[2])
          Start scores = (19, 47).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (34, 47)
          >>> print(turns[3])
          Start scores = (34, 47).
          Player 1 rolls 8 dice and gets outcomes [1, 5, 3, 1, 6, 4, 6, 6].
          End scores = (34, 48)
          >>> print(turns[4])
          Start scores = (34, 48).
          Player 0 rolls 8 dice and gets outcomes [1, 6, 4, 5, 5, 3, 6, 2].
          End scores = (35, 48)
          >>> print(turns[5])
          Start scores = (35, 48).
          Player 1 rolls 5 dice and gets outcomes [2, 4, 6, 1, 1].
          End scores = (35, 49)
          >>> print(turns[6])
          Start scores = (35, 49).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 2, 2, 5, 5, 4, 4].
          End scores = (36, 49)
          >>> print(turns[7])
          Start scores = (36, 49).
          Player 1 rolls 5 dice and gets outcomes [2, 4, 5, 1, 3].
          End scores = (36, 50)
          >>> print(turns[8])
          Start scores = (36, 50).
          Player 0 rolls 7 dice and gets outcomes [1, 1, 2, 1, 1, 3, 6].
          End scores = (37, 50)
          >>> print(turns[9])
          Start scores = (37, 50).
          Player 1 rolls 10 dice and gets outcomes [4, 5, 3, 2, 4, 3, 4, 2, 5, 2].
          End scores = (37, 84)
          >>> print(turns[10])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=90865, score0=9, score1=18, goal=35, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (9, 18).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (33, 18)
          >>> print(turns[1])
          Start scores = (33, 18).
          Player 1 rolls 4 dice and gets outcomes [3, 1, 5, 6].
          End scores = (33, 19)
          >>> print(turns[2])
          Start scores = (33, 19).
          Player 0 rolls 5 dice and gets outcomes [3, 1, 3, 1, 4].
          End scores = (34, 19)
          >>> print(turns[3])
          Start scores = (34, 19).
          Player 1 rolls 6 dice and gets outcomes [3, 1, 4, 6, 1, 3].
          End scores = (34, 20)
          >>> print(turns[4])
          Start scores = (34, 20).
          Player 0 rolls 5 dice and gets outcomes [5, 6, 3, 4, 3].
          End scores = (55, 20)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=27412, score0=3, score1=10, goal=22, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (3, 10).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (9, 10)
          >>> print(turns[1])
          Start scores = (9, 10).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (9, 16)
          >>> print(turns[2])
          Start scores = (9, 16).
          Player 0 rolls 9 dice and gets outcomes [3, 3, 4, 2, 2, 6, 4, 6, 2].
          End scores = (41, 16)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=64099, score0=14, score1=44, goal=46, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (14, 44).
          Player 0 rolls 10 dice and gets outcomes [2, 2, 2, 4, 4, 2, 1, 3, 2, 6].
          End scores = (15, 44)
          >>> print(turns[1])
          Start scores = (15, 44).
          Player 1 rolls 8 dice and gets outcomes [6, 4, 2, 2, 4, 1, 2, 6].
          End scores = (15, 45)
          >>> print(turns[2])
          Start scores = (15, 45).
          Player 0 rolls 6 dice and gets outcomes [5, 6, 2, 6, 2, 5].
          End scores = (41, 45)
          >>> print(turns[3])
          Start scores = (41, 45).
          Player 1 rolls 8 dice and gets outcomes [1, 5, 3, 3, 4, 6, 6, 1].
          End scores = (41, 46)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=99115, score0=30, score1=22, goal=34, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (30, 22).
          Player 0 rolls 6 dice and gets outcomes [5, 5, 6, 4, 4, 4].
          End scores = (58, 22)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=41138, score0=84, score1=25, goal=92, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (84, 25).
          Player 0 rolls 4 dice and gets outcomes [1, 5, 2, 5].
          End scores = (85, 25)
          >>> print(turns[1])
          Start scores = (85, 25).
          Player 1 rolls 5 dice and gets outcomes [2, 4, 2, 6, 5].
          End scores = (85, 44)
          >>> print(turns[2])
          Start scores = (85, 44).
          Player 0 rolls 5 dice and gets outcomes [2, 4, 3, 6, 5].
          End scores = (105, 44)
          >>> print(turns[3])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=75946, score0=76, score1=58, goal=91, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (76, 58).
          Player 0 rolls 9 dice and gets outcomes [2, 4, 1, 3, 4, 6, 6, 3, 4].
          End scores = (77, 58)
          >>> print(turns[1])
          Start scores = (77, 58).
          Player 1 rolls 3 dice and gets outcomes [4, 6, 6].
          End scores = (77, 74)
          >>> print(turns[2])
          Start scores = (77, 74).
          Player 0 rolls 9 dice and gets outcomes [6, 1, 3, 3, 6, 3, 6, 4, 1].
          End scores = (78, 74)
          >>> print(turns[3])
          Start scores = (78, 74).
          Player 1 rolls 4 dice and gets outcomes [5, 3, 4, 1].
          End scores = (78, 75)
          >>> print(turns[4])
          Start scores = (78, 75).
          Player 0 rolls 2 dice and gets outcomes [5, 2].
          End scores = (85, 75)
          >>> print(turns[5])
          Start scores = (85, 75).
          Player 1 rolls 3 dice and gets outcomes [3, 3, 4].
          End scores = (85, 85)
          >>> print(turns[6])
          Start scores = (85, 85).
          Player 0 rolls 7 dice and gets outcomes [1, 3, 1, 5, 2, 4, 5].
          End scores = (86, 85)
          >>> print(turns[7])
          Start scores = (86, 85).
          Player 1 rolls 4 dice and gets outcomes [5, 6, 5, 6].
          End scores = (86, 107)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=29276, score0=44, score1=6, goal=85, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (44, 6).
          Player 0 rolls 3 dice and gets outcomes [3, 1, 6].
          End scores = (45, 6)
          >>> print(turns[1])
          Start scores = (45, 6).
          Player 1 rolls 2 dice and gets outcomes [1, 4].
          End scores = (45, 7)
          >>> print(turns[2])
          Start scores = (45, 7).
          Player 0 rolls 6 dice and gets outcomes [4, 2, 5, 4, 1, 5].
          End scores = (46, 7)
          >>> print(turns[3])
          Start scores = (46, 7).
          Player 1 rolls 4 dice and gets outcomes [1, 1, 3, 3].
          End scores = (46, 8)
          >>> print(turns[4])
          Start scores = (46, 8).
          Player 0 rolls 9 dice and gets outcomes [6, 4, 1, 1, 3, 1, 4, 5, 5].
          End scores = (47, 8)
          >>> print(turns[5])
          Start scores = (47, 8).
          Player 1 rolls 8 dice and gets outcomes [3, 5, 5, 3, 2, 5, 1, 4].
          End scores = (47, 9)
          >>> print(turns[6])
          Start scores = (47, 9).
          Player 0 rolls 10 dice and gets outcomes [6, 5, 2, 5, 2, 5, 3, 1, 5, 1].
          End scores = (48, 9)
          >>> print(turns[7])
          Start scores = (48, 9).
          Player 1 rolls 10 dice and gets outcomes [2, 1, 3, 1, 1, 4, 5, 4, 1, 6].
          End scores = (48, 10)
          >>> print(turns[8])
          Start scores = (48, 10).
          Player 0 rolls 5 dice and gets outcomes [2, 5, 4, 4, 4].
          End scores = (67, 10)
          >>> print(turns[9])
          Start scores = (67, 10).
          Player 1 rolls 2 dice and gets outcomes [5, 3].
          End scores = (67, 18)
          >>> print(turns[10])
          Start scores = (67, 18).
          Player 0 rolls 3 dice and gets outcomes [2, 5, 4].
          End scores = (78, 18)
          >>> print(turns[11])
          Start scores = (78, 18).
          Player 1 rolls 3 dice and gets outcomes [2, 2, 6].
          End scores = (78, 28)
          >>> print(turns[12])
          Start scores = (78, 28).
          Player 0 rolls 4 dice and gets outcomes [6, 6, 4, 4].
          End scores = (98, 28)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=5971, score0=31, score1=81, goal=100, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (31, 81).
          Player 0 rolls 6 dice and gets outcomes [4, 1, 4, 5, 3, 4].
          End scores = (32, 81)
          >>> print(turns[1])
          Start scores = (32, 81).
          Player 1 rolls 2 dice and gets outcomes [2, 4].
          End scores = (32, 87)
          >>> print(turns[2])
          Start scores = (32, 87).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 1, 2, 4].
          End scores = (33, 87)
          >>> print(turns[3])
          Start scores = (33, 87).
          Player 1 rolls 9 dice and gets outcomes [2, 5, 2, 3, 1, 5, 2, 3, 2].
          End scores = (33, 88)
          >>> print(turns[4])
          Start scores = (33, 88).
          Player 0 rolls 7 dice and gets outcomes [4, 4, 4, 3, 4, 4, 2].
          End scores = (58, 88)
          >>> print(turns[5])
          Start scores = (58, 88).
          Player 1 rolls 8 dice and gets outcomes [1, 1, 2, 6, 1, 1, 3, 6].
          End scores = (58, 89)
          >>> print(turns[6])
          Start scores = (58, 89).
          Player 0 rolls 7 dice and gets outcomes [5, 5, 5, 6, 1, 6, 5].
          End scores = (59, 89)
          >>> print(turns[7])
          Start scores = (59, 89).
          Player 1 rolls 2 dice and gets outcomes [1, 3].
          End scores = (59, 90)
          >>> print(turns[8])
          Start scores = (59, 90).
          Player 0 rolls 6 dice and gets outcomes [1, 4, 3, 4, 1, 5].
          End scores = (64, 90)
          >>> print(turns[9])
          Start scores = (64, 90).
          Player 1 rolls 1 dice and gets outcomes [6].
          End scores = (64, 96)
          >>> print(turns[10])
          Start scores = (64, 96).
          Player 0 rolls 1 dice and gets outcomes [6].
          End scores = (70, 96)
          >>> print(turns[11])
          Start scores = (70, 96).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 3, 3, 4, 5, 5].
          End scores = (70, 122)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=88253, score0=4, score1=10, goal=37, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (4, 10).
          Player 0 rolls 6 dice and gets outcomes [1, 4, 4, 2, 4, 2].
          End scores = (5, 10)
          >>> print(turns[1])
          Start scores = (5, 10).
          Player 1 rolls 3 dice and gets outcomes [4, 3, 4].
          End scores = (5, 21)
          >>> print(turns[2])
          Start scores = (5, 21).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (14, 21)
          >>> print(turns[3])
          Start scores = (14, 21).
          Player 1 rolls 2 dice and gets outcomes [5, 2].
          End scores = (14, 28)
          >>> print(turns[4])
          Start scores = (14, 28).
          Player 0 rolls 7 dice and gets outcomes [3, 5, 5, 5, 3, 1, 5].
          End scores = (15, 28)
          >>> print(turns[5])
          Start scores = (15, 28).
          Player 1 rolls 1 dice and gets outcomes [3].
          End scores = (15, 31)
          >>> print(turns[6])
          Start scores = (15, 31).
          Player 0 rolls 4 dice and gets outcomes [1, 5, 4, 1].
          End scores = (16, 31)
          >>> print(turns[7])
          Start scores = (16, 31).
          Player 1 rolls 5 dice and gets outcomes [5, 4, 4, 5, 2].
          End scores = (16, 51)
          >>> print(turns[8])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=53592, score0=7, score1=91, goal=96, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (7, 91).
          Player 0 rolls 2 dice and gets outcomes [1, 5].
          End scores = (8, 91)
          >>> print(turns[1])
          Start scores = (8, 91).
          Player 1 rolls 4 dice and gets outcomes [3, 6, 5, 4].
          End scores = (8, 109)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61601, score0=39, score1=1, goal=65, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (39, 1).
          Player 0 rolls 4 dice and gets outcomes [4, 5, 4, 1].
          End scores = (40, 1)
          >>> print(turns[1])
          Start scores = (40, 1).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (40, 10)
          >>> print(turns[2])
          Start scores = (40, 10).
          Player 0 rolls 3 dice and gets outcomes [4, 4, 6].
          End scores = (54, 10)
          >>> print(turns[3])
          Start scores = (54, 10).
          Player 1 rolls 8 dice and gets outcomes [5, 5, 6, 5, 1, 2, 1, 2].
          End scores = (54, 11)
          >>> print(turns[4])
          Start scores = (54, 11).
          Player 0 rolls 5 dice and gets outcomes [6, 2, 4, 2, 3].
          End scores = (71, 11)
          >>> print(turns[5])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61473, score0=14, score1=16, goal=55, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (14, 16).
          Player 0 rolls 3 dice and gets outcomes [3, 4, 1].
          End scores = (15, 16)
          >>> print(turns[1])
          Start scores = (15, 16).
          Player 1 rolls 2 dice and gets outcomes [3, 1].
          End scores = (15, 17)
          >>> print(turns[2])
          Start scores = (15, 17).
          Player 0 rolls 8 dice and gets outcomes [6, 5, 6, 2, 2, 2, 1, 3].
          End scores = (16, 17)
          >>> print(turns[3])
          Start scores = (16, 17).
          Player 1 rolls 10 dice and gets outcomes [1, 2, 4, 2, 2, 4, 5, 1, 6, 4].
          End scores = (16, 18)
          >>> print(turns[4])
          Start scores = (16, 18).
          Player 0 rolls 8 dice and gets outcomes [5, 5, 3, 5, 1, 6, 2, 6].
          End scores = (17, 18)
          >>> print(turns[5])
          Start scores = (17, 18).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 1, 4, 2, 2, 6].
          End scores = (17, 19)
          >>> print(turns[6])
          Start scores = (17, 19).
          Player 0 rolls 2 dice and gets outcomes [2, 1].
          End scores = (18, 19)
          >>> print(turns[7])
          Start scores = (18, 19).
          Player 1 rolls 5 dice and gets outcomes [3, 3, 6, 2, 5].
          End scores = (18, 38)
          >>> print(turns[8])
          Start scores = (18, 38).
          Player 0 rolls 1 dice and gets outcomes [1].
          End scores = (19, 38)
          >>> print(turns[9])
          Start scores = (19, 38).
          Player 1 rolls 10 dice and gets outcomes [6, 2, 1, 5, 1, 1, 2, 3, 2, 6].
          End scores = (19, 39)
          >>> print(turns[10])
          Start scores = (19, 39).
          Player 0 rolls 3 dice and gets outcomes [1, 6, 1].
          End scores = (24, 39)
          >>> print(turns[11])
          Start scores = (24, 39).
          Player 1 rolls 8 dice and gets outcomes [2, 4, 4, 6, 5, 4, 5, 4].
          End scores = (24, 73)
          >>> print(turns[12])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=64089, score0=31, score1=87, goal=88, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (31, 87).
          Player 0 rolls 2 dice and gets outcomes [4, 1].
          End scores = (32, 87)
          >>> print(turns[1])
          Start scores = (32, 87).
          Player 1 rolls 10 dice and gets outcomes [3, 1, 4, 1, 4, 3, 2, 4, 6, 4].
          End scores = (32, 88)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=61086, score0=7, score1=17, goal=18, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (7, 17).
          Player 0 rolls 9 dice and gets outcomes [4, 1, 6, 6, 1, 3, 5, 1, 4].
          End scores = (8, 17)
          >>> print(turns[1])
          Start scores = (8, 17).
          Player 1 rolls 3 dice and gets outcomes [1, 1, 5].
          End scores = (8, 18)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=51837, score0=8, score1=14, goal=17, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (8, 14).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (29, 14)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=42021, score0=2, score1=17, goal=79, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (2, 17).
          Player 0 rolls 5 dice and gets outcomes [6, 2, 4, 2, 6].
          End scores = (22, 17)
          >>> print(turns[1])
          Start scores = (22, 17).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (22, 32)
          >>> print(turns[2])
          Start scores = (22, 32).
          Player 0 rolls 4 dice and gets outcomes [6, 3, 2, 5].
          End scores = (38, 32)
          >>> print(turns[3])
          Start scores = (38, 32).
          Player 1 rolls 7 dice and gets outcomes [2, 4, 4, 2, 6, 2, 6].
          End scores = (38, 58)
          >>> print(turns[4])
          Start scores = (38, 58).
          Player 0 rolls 6 dice and gets outcomes [1, 1, 4, 1, 2, 6].
          End scores = (39, 58)
          >>> print(turns[5])
          Start scores = (39, 58).
          Player 1 rolls 4 dice and gets outcomes [1, 5, 5, 6].
          End scores = (39, 59)
          >>> print(turns[6])
          Start scores = (39, 59).
          Player 0 rolls 7 dice and gets outcomes [6, 2, 3, 6, 5, 3, 1].
          End scores = (40, 59)
          >>> print(turns[7])
          Start scores = (40, 59).
          Player 1 rolls 7 dice and gets outcomes [6, 6, 3, 5, 1, 6, 6].
          End scores = (40, 60)
          >>> print(turns[8])
          Start scores = (40, 60).
          Player 0 rolls 5 dice and gets outcomes [6, 4, 4, 2, 2].
          End scores = (58, 60)
          >>> print(turns[9])
          Start scores = (58, 60).
          Player 1 rolls 3 dice and gets outcomes [2, 5, 6].
          End scores = (58, 73)
          >>> print(turns[10])
          Start scores = (58, 73).
          Player 0 rolls 9 dice and gets outcomes [4, 5, 2, 2, 3, 5, 4, 2, 1].
          End scores = (59, 73)
          >>> print(turns[11])
          Start scores = (59, 73).
          Player 1 rolls 7 dice and gets outcomes [1, 1, 2, 6, 1, 5, 4].
          End scores = (59, 74)
          >>> print(turns[12])
          Start scores = (59, 74).
          Player 0 rolls 9 dice and gets outcomes [4, 6, 4, 2, 3, 6, 6, 3, 6].
          End scores = (99, 74)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=62911, score0=5, score1=32, goal=50, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (5, 32).
          Player 0 rolls 8 dice and gets outcomes [3, 5, 5, 4, 3, 1, 2, 3].
          End scores = (6, 32)
          >>> print(turns[1])
          Start scores = (6, 32).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (6, 38)
          >>> print(turns[2])
          Start scores = (6, 38).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 1, 1, 2, 2, 4, 1, 2, 4].
          End scores = (7, 38)
          >>> print(turns[3])
          Start scores = (7, 38).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (7, 62)
          >>> print(turns[4])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=48409, score0=22, score1=10, goal=61, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (22, 10).
          Player 0 rolls 8 dice and gets outcomes [6, 1, 3, 3, 3, 2, 2, 6].
          End scores = (23, 10)
          >>> print(turns[1])
          Start scores = (23, 10).
          Player 1 rolls 5 dice and gets outcomes [6, 4, 6, 6, 2].
          End scores = (23, 34)
          >>> print(turns[2])
          Start scores = (23, 34).
          Player 0 rolls 1 dice and gets outcomes [3].
          End scores = (26, 34)
          >>> print(turns[3])
          Start scores = (26, 34).
          Player 1 rolls 1 dice and gets outcomes [2].
          End scores = (26, 36)
          >>> print(turns[4])
          Start scores = (26, 36).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (35, 36)
          >>> print(turns[5])
          Start scores = (35, 36).
          Player 1 rolls 6 dice and gets outcomes [2, 1, 5, 1, 6, 3].
          End scores = (35, 37)
          >>> print(turns[6])
          Start scores = (35, 37).
          Player 0 rolls 2 dice and gets outcomes [3, 5].
          End scores = (43, 37)
          >>> print(turns[7])
          Start scores = (43, 37).
          Player 1 rolls 4 dice and gets outcomes [1, 4, 1, 3].
          End scores = (43, 38)
          >>> print(turns[8])
          Start scores = (43, 38).
          Player 0 rolls 2 dice and gets outcomes [2, 4].
          End scores = (49, 38)
          >>> print(turns[9])
          Start scores = (49, 38).
          Player 1 rolls 3 dice and gets outcomes [4, 5, 1].
          End scores = (49, 39)
          >>> print(turns[10])
          Start scores = (49, 39).
          Player 0 rolls 10 dice and gets outcomes [5, 2, 4, 5, 3, 5, 1, 6, 3, 3].
          End scores = (60, 39)
          >>> print(turns[11])
          Start scores = (60, 39).
          Player 1 rolls 1 dice and gets outcomes [4].
          End scores = (60, 43)
          >>> print(turns[12])
          Start scores = (60, 43).
          Player 0 rolls 5 dice and gets outcomes [4, 6, 5, 6, 4].
          End scores = (85, 43)
          >>> print(turns[13])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=50497, score0=8, score1=17, goal=19, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (8, 17).
          Player 0 rolls 8 dice and gets outcomes [3, 3, 1, 2, 5, 2, 4, 5].
          End scores = (9, 17)
          >>> print(turns[1])
          Start scores = (9, 17).
          Player 1 rolls 0 dice and gets outcomes [].
          End scores = (9, 38)
          >>> print(turns[2])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=52997, score0=15, score1=17, goal=23, update=hog.simple_update)
          >>> print(turns[0])
          Start scores = (15, 17).
          Player 0 rolls 0 dice and gets outcomes [].
          End scores = (27, 17)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
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
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
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
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
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
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        },
        {
          'code': r"""
          >>> turns = tests.play_utils.describe_game(hog, test_number=67024, score0=59, score1=4, goal=60, update=hog.fuzzy_update)
          >>> print(turns[0])
          Start scores = (59, 4).
          Player 0 rolls 1 dice and gets outcomes [4].
          End scores = (63, 4)
          >>> print(turns[1])
          Game Over
          """,
          'hidden': False,
          'locked': False,
          'multiline': False
        }
      ],
      'scored': True,
      'setup': r"""
      >>> # Fuzz Testing
      >>> # Plays a lot of random games, and calculates a secret value.
      >>> # Failing this test means something is wrong, but you should
      >>> # look at other tests to see where the problem might be.
      >>> # Hint: make sure you're only calling update once per turn!
      >>> #
      >>> import hog, importlib
      >>> # importlib.reload(hog)
      >>> import tests.play_utils
      """,
      'teardown': r"""
      
      """,
      'type': 'doctest'
    }
  ]
}
