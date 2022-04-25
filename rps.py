#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import sys
import time
import random
from colorama import init
from colorama import Fore, Back, Style


"""The Player class is the parent class for all of the Players
in this game"""

moves = ['rock', 'paper', 'scissors']


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("rock, paper, scissors?"'\n')
            if move in moves:
                return move


class ReflectPlayer(Player):
    def __init__(self):
        self.move = random.choice(moves)

    def move(self):
        return self.move

    def learn(self, my_move, their_move):
        self.move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.options = 0

    def move(self):
        return moves[self.options]

    def learn(self, my_move, their_move):
        if self.options == 2:
            self.options = 0
        else:
            self.options += 1


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:

    print(Fore.YELLOW + "Would you like to play Rock, Paper, Scissors?"'\n')
    time.sleep(1)

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def start_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")

        if beats(move1, move2):
            self.score1 += 1
            print(Fore.BLUE + "You won!")
            print(Fore.WHITE + f"You: {self.score1} Player 2: {self.score2}")
        elif beats(move2, move1):
            self.score2 += 1
            print(Fore.RED + "Player 2 won!")
            print(Fore.WHITE + f"You: {self.score1} Player 2: {self.score2}")
        else:
            print(Fore.YELLOW + "Its a tie !")
            print(Fore.WHITE + f"You: {self.score1} Player 2: {self.score2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Ready Set Go !!"'\n')
        time.sleep(2)
        for round in range(2):
            print(f"Round {round}:")
            self.start_round()
        if self.score1 > self.score2:
            print(Fore.YELLOW + "Congratulations, you won this phase!")
        elif self.score1 < self.score2:
            print(Fore.RED + "Player 2 won this phase!")
        else:
            print(Fore.YELLOW + "This phase ended in a tie!")

        newround = input("Continue game? (y)es or (n)o"'\n')
        while True:
            if newround == 'n':
                print("Uhn Uhn see you next time tho")
                time.sleep(2)
                sys.exit(0)

            elif newround == 'y':
                self.extra_rounds()
                if self.score1 > self.score2:
                    print(Fore.GREEN + "Congrats, you won the overall phase")
                elif self.score1 < self.score2:
                    print(Fore.BLUE + "Player 2 won the overall phase")
                else:
                    print(Fore.YELLOW + "The overall phase ended in a tie")
                sys.exit(0)

            else:
                rightInput = input("Continue game? (y)es or (n)o"'\n')
                if rightInput == 'n':
                    print("Uhn Uhn see you next time tho")
                    time.sleep(2)
                    sys.exit(0)
                elif rightInput == 'y':
                    self.extra_rounds()
                    if self.score1 > self.score2:
                        print(Fore.GREEN+"Congrats, you won the overall phase")
                    elif self.score1 < self.score2:
                        print(Fore.BLUE+"Player 2 won the overall phase")
                    else:
                        print(Fore.YELLOW+"The overall phase ended in a tie")
                    sys.exit(0)

    def extra_rounds(self):
        for round in range(3):
            print(f"Round {round+1}:")
            self.start_round()


if __name__ == '__main__':
    strategy = [Player(), RandomPlayer(), CyclePlayer()]
    behavior = random.choice(strategy)
    human = HumanPlayer()
    game = Game(human, behavior)
    game.play_game()

