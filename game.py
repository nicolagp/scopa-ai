from computer.computer import Computer
from computer.randomized import Randomized
from scopa import *


def main():
    # Ask for player specifics
    print("Please enter the number of human players: ", end="")
    n = int(input())
    if n == 2:
        print("Please enter the name of player 1: ")
        p1 = Player(input())
        print("Please enter the name of player 2: ", end="")
        p2 = Player(input())
    elif n == 1:
        print("Please enter the name of player 1: ")
        p1 = Player(input())
        p2 = Randomized("Computer")
    elif n == 0:
        p1 = Randomized("Computer 1")
        p2 = Randomized("Computer 2")
    else:
        print("Invalid number of players. ")
        return 1

    scopa = Scopa(p1, p2, test=True)

    while True:
        print(scopa)
        if scopa.round % 2 == 0:
            first = scopa.players[0]
            second = scopa.players[1]
        else:
            first = scopa.players[1]
            second = scopa.players[0]

        # Implements moves for three turns
        for i in range(3):
            # 2 computers
            if n == 0:
                for player in (first, second):
                    player.table = list(scopa.table)
                    while True:
                        print("{} make your move: ".format(player), end='')
                        hand, table = player.move()
                        if scopa.move(player, hand, table):
                            break
                        else:
                            print("Please enter a valid move")
                    print(scopa)
            # 1 player, 1 computer
            elif n == 1:
                for player in (first, second):
                    if not isinstance(player, Computer):
                        while True:
                            print("{} make your move: ".format(player), end='')
                            move = input().split()
                            table = []
                            if len(move) < 1:
                                continue
                            elif len(move) > 1:
                                for j in move[1:]:
                                    table.append(int(j))
                            if scopa.move(player, int(move[0]), table):
                                break
                            else:
                                print("Please enter a valid move")
                    else:
                        while True:
                            print("{} make your move: ".format(player), end='')
                            hand, table = player.move()
                            if scopa.move(player, hand.value, table):
                                break
                            else:
                                print("Please enter a valid move")
                    print(scopa)
            # 2 players
            elif n == 2:
                for player in (first, second):
                    while True:
                        print("{} make your move: ".format(player), end='')
                        move = input().split()
                        table = []
                        if len(move) < 1:
                            continue
                        elif len(move) > 1:
                            for j in move[1:]:
                                table.append(int(j))
                        if scopa.move(player, int(move[0]), table):
                            break
                        else:
                            print("Please enter a valid move")
                print(scopa)

            # Check if round is over or deal more cards
            if len(scopa.deck) > 0:
                scopa.deal()
            else:
                # Give remaining cards to last player to take cards
                for card in scopa.table:
                    scopa.last.pile.append(card)
                scopa.table = []
                if scopa.score_round(p1, p2):
                    if scopa.score[0] > scopa.score[1]:
                        print("{} won!".format(scopa.players[0]))
                    else:
                        print("{} won!".format(scopa.score[1]))
                    print("Score: {} x {}".format(scopa.score[0], scopa.score[1]))
                    break


if __name__ == "__main__":
    main()
