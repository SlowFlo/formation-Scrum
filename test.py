import sys
import unittest
from io import StringIO
import random

from trivia import Game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_game(self):
        result = """Chet was added
They are player number 1
Pat was added
They are player number 2
Sue was added
They are player number 3
Chet is the current player
They have rolled a 5
Chet's new location is 5
The category is Science
Science Question 0
Answer was corrent!!!!
Chet now has 1 Gold Coins.
Pat is the current player
They have rolled a 5
Pat's new location is 5
The category is Science
Science Question 1
Answer was corrent!!!!
Pat now has 1 Gold Coins.
Sue is the current player
They have rolled a 5
Sue's new location is 5
The category is Science
Science Question 2
Answer was corrent!!!!
Sue now has 1 Gold Coins.
Chet is the current player
They have rolled a 3
Chet's new location is 8
The category is Pop
Pop Question 0
Answer was corrent!!!!
Chet now has 2 Gold Coins.
Pat is the current player
They have rolled a 4
Pat's new location is 9
The category is Science
Science Question 3
Answer was corrent!!!!
Pat now has 2 Gold Coins.
Sue is the current player
They have rolled a 2
Sue's new location is 7
The category is Rock
Rock Question 0
Answer was corrent!!!!
Sue now has 2 Gold Coins.
Chet is the current player
They have rolled a 4
Chet's new location is 0
The category is Pop
Pop Question 1
Answer was corrent!!!!
Chet now has 3 Gold Coins.
Pat is the current player
They have rolled a 5
Pat's new location is 2
The category is Sports
Sports Question 0
Answer was corrent!!!!
Pat now has 3 Gold Coins.
Sue is the current player
They have rolled a 1
Sue's new location is 8
The category is Pop
Pop Question 2
Answer was corrent!!!!
Sue now has 3 Gold Coins.
Chet is the current player
They have rolled a 2
Chet's new location is 2
The category is Sports
Sports Question 1
Answer was corrent!!!!
Chet now has 4 Gold Coins.
Pat is the current player
They have rolled a 4
Pat's new location is 6
The category is Sports
Sports Question 2
Answer was corrent!!!!
Pat now has 4 Gold Coins.
Sue is the current player
They have rolled a 5
Sue's new location is 1
The category is Science
Science Question 4
Answer was corrent!!!!
Sue now has 4 Gold Coins.
Chet is the current player
They have rolled a 4
Chet's new location is 6
The category is Sports
Sports Question 3
Answer was corrent!!!!
Chet now has 5 Gold Coins.
Pat is the current player
They have rolled a 2
Pat's new location is 8
The category is Pop
Pop Question 3
Answer was corrent!!!!
Pat now has 5 Gold Coins.
Sue is the current player
They have rolled a 4
Sue's new location is 5
The category is Science
Science Question 5
Answer was corrent!!!!
Sue now has 5 Gold Coins.
Chet is the current player
They have rolled a 3
Chet's new location is 9
The category is Science
Science Question 6
Answer was corrent!!!!
Chet now has 6 Gold Coins.
"""

        temp_output = StringIO()
        origin = sys.stdout
        sys.stdout = temp_output

        self.game.add('Chet')
        self.game.add('Pat')
        self.game.add('Sue')

        random.seed(30)
        while True:
            self.game.roll(random.randrange(5) + 1)

            if random.randrange(9) == 7:
                not_a_winner = self.game.wrong_answer()
            else:
                not_a_winner = self.game.was_correctly_answered()

            if not not_a_winner: break

        sys.stdout = origin
        self.assertEqual(result, temp_output.getvalue())

    def test_second_seed(self):
        result = """Chet was added
They are player number 1
Pat was added
They are player number 2
Sue was added
They are player number 3
Chet is the current player
They have rolled a 2
Chet's new location is 2
The category is Sports
Sports Question 0
Question was incorrectly answered
Chet was sent to the penalty box
Pat is the current player
They have rolled a 3
Pat's new location is 3
The category is Rock
Rock Question 0
Answer was corrent!!!!
Pat now has 1 Gold Coins.
Sue is the current player
They have rolled a 2
Sue's new location is 2
The category is Sports
Sports Question 1
Answer was corrent!!!!
Sue now has 1 Gold Coins.
Chet is the current player
They have rolled a 1
Chet is getting out of the penalty box
Chet's new location is 3
The category is Rock
Rock Question 1
Answer was correct!!!!
Chet now has 1 Gold Coins.
Pat is the current player
They have rolled a 4
Pat's new location is 7
The category is Rock
Rock Question 2
Answer was corrent!!!!
Pat now has 2 Gold Coins.
Sue is the current player
They have rolled a 2
Sue's new location is 4
The category is Pop
Pop Question 0
Answer was corrent!!!!
Sue now has 2 Gold Coins.
Chet is the current player
They have rolled a 2
Chet is not getting out of the penalty box
Pat is the current player
They have rolled a 5
Pat's new location is 0
The category is Pop
Pop Question 1
Answer was corrent!!!!
Pat now has 3 Gold Coins.
Sue is the current player
They have rolled a 2
Sue's new location is 6
The category is Sports
Sports Question 2
Answer was corrent!!!!
Sue now has 3 Gold Coins.
Chet is the current player
They have rolled a 1
Chet is getting out of the penalty box
Chet's new location is 4
The category is Pop
Pop Question 2
Question was incorrectly answered
Chet was sent to the penalty box
Pat is the current player
They have rolled a 5
Pat's new location is 5
The category is Science
Science Question 0
Answer was corrent!!!!
Pat now has 4 Gold Coins.
Sue is the current player
They have rolled a 1
Sue's new location is 7
The category is Rock
Rock Question 3
Answer was corrent!!!!
Sue now has 4 Gold Coins.
Chet is the current player
They have rolled a 4
Chet is not getting out of the penalty box
Question was incorrectly answered
Chet was sent to the penalty box
Pat is the current player
They have rolled a 3
Pat's new location is 8
The category is Pop
Pop Question 3
Answer was corrent!!!!
Pat now has 5 Gold Coins.
Sue is the current player
They have rolled a 3
Sue's new location is 10
The category is Sports
Sports Question 3
Answer was corrent!!!!
Sue now has 5 Gold Coins.
Chet is the current player
They have rolled a 5
Chet is getting out of the penalty box
Chet's new location is 9
The category is Science
Science Question 1
Answer was correct!!!!
Chet now has 2 Gold Coins.
Pat is the current player
They have rolled a 4
Pat's new location is 0
The category is Pop
Pop Question 4
Answer was corrent!!!!
Pat now has 6 Gold Coins.
"""

        temp_output = StringIO()
        origin = sys.stdout
        sys.stdout = temp_output

        self.game.add('Chet')
        self.game.add('Pat')
        self.game.add('Sue')

        random.seed(485214524)
        while True:
            self.game.roll(random.randrange(5) + 1)

            if random.randrange(9) == 7:
                not_a_winner = self.game.wrong_answer()
            else:
                not_a_winner = self.game.was_correctly_answered()

            if not not_a_winner: break

        sys.stdout = origin
        self.assertEqual(result, temp_output.getvalue())

    def test_un_joueur(self):
        result = """Chet was added
They are player number 1
Chet is the current player
They have rolled a 5
Chet's new location is 5
The category is Science
Science Question 0
Answer was corrent!!!!
Chet now has 1 Gold Coins.
Chet is the current player
They have rolled a 5
Chet's new location is 10
The category is Sports
Sports Question 0
Answer was corrent!!!!
Chet now has 2 Gold Coins.
Chet is the current player
They have rolled a 5
Chet's new location is 3
The category is Rock
Rock Question 0
Answer was corrent!!!!
Chet now has 3 Gold Coins.
Chet is the current player
They have rolled a 3
Chet's new location is 6
The category is Sports
Sports Question 1
Answer was corrent!!!!
Chet now has 4 Gold Coins.
Chet is the current player
They have rolled a 4
Chet's new location is 10
The category is Sports
Sports Question 2
Answer was corrent!!!!
Chet now has 5 Gold Coins.
Chet is the current player
They have rolled a 2
Chet's new location is 0
The category is Pop
Pop Question 0
Answer was corrent!!!!
Chet now has 6 Gold Coins.
"""

        temp_output = StringIO()
        origin = sys.stdout
        sys.stdout = temp_output

        self.game.add('Chet')

        random.seed(30)
        while True:
            self.game.roll(random.randrange(5) + 1)

            if random.randrange(9) == 7:
                not_a_winner = self.game.wrong_answer()
            else:
                not_a_winner = self.game.was_correctly_answered()

            if not not_a_winner: break

        sys.stdout = origin
        self.assertEqual(result, temp_output.getvalue())


