from scopa import *
def main():
    print("Please enter the name of player 1: ", end="")
    p1 = Player(input())
    print("Please enter the name of player 2: ", end="")
    p2 = Player(input())
    scopa = Scopa(p1, p2)
    print("To make a move enter the index of the card you want to play and the indices of cards on the table separated "
          "by spaces")
    print("Example: ")
    print("""Player 1: (clubs, 5) (spades, 9) (cups, 7) 
    Table: (coins, 2) (clubs, 3) (cups, 5) (coins, 8) 
    Player 2: (clubs, 10) (coins, 4) (cups, 1)""")
    # main loop for the game
    while True:
        print(scopa)
        if scopa.round % 2 == 0:
            first = scopa.players[0]
            second = scopa.players[1]
        else:
            first = scopa.players[1]
            second = scopa.players[0]

        while True:
            print("{}, make your move: ".format(first))
            move = input().split()
            table = list(map(int, move[1:]))
            if scopa.move(first, int(move[0]), table):
                break
            else:
                print("Please enter a valid move")
        print(scopa)

        while True:
            print("{} make your move: ".format(second))
            move = input().split()
            table = list(map(int, move[1:]))
            if scopa.move(second, int(move[0]), table):
                break
            else:
                print("Please enter a valid move")
        print(scopa)

        if scopa.score_round(p1, p2):
            if scopa.score[0] > scopa.score[1]:
                print("{} won!".format(scopa.players[0]))
            else:
                print("{} won!".format(scopa.score[1]))
            print("Score: {} x {}".format(scopa.score[0], scopa.score[1]))
            break

# TODO check the move input to see if the length is correct
# TODO move for putting card on table

if __name__ == "__main__":
    main()