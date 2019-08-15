""" Final Project AI Fiction in Fact """
import random

from Board import Board
from Player import Player

"""
Notes:

Board: 
    Tiles: 19 Total
        3 - 4 - 5 - 4 - 3
    Vertices: 54 Total
        7 - 9 - 11 - 11 - 9 - 7
    Sides: 72 Total
        6 - 4 - 8 - 5 - 10 - 6 - 10 - 5 - 8 - 4 - 6

Documentation:
    Coding Format:
        functions : Capitize the first letter in each word
        variables : Capitize the first letter in each word except the first

        Indent side of 4

    Make sure to put error messages in 

"""

def RollDice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x + y

def SetUpPlacement(player):
    done = False
    while not done:
        index = random.randint(0, 53)
        print("Index: {}".format(index))
        done = player.PlacePiece(board, "settlement", index, 0)

    roads = board.ConnectedEdges(index, "vertex")
    # players[0].PlacePiece(board, "road", random.choice(roads), 0)
    player.PlacePiece(board, "road", roads[0], 0)


def SetUp(players, board):
    # index = board.BestSpotRemaining()

    # SetUpPlacement(players[0])
    # SetUpPlacement(players[1])
    # SetUpPlacement(players[2])
    # SetUpPlacement(players[2])
    # SetUpPlacement(players[1])
    # SetUpPlacement(players[0])

    index = board.BestSpotRemaining()
    players[0].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[1].PlacePiece(board, "road", random.choice(roads), 0)
    players[0].PlacePiece(board, "road", roads[0], 0)

    index = board.BestSpotRemaining()
    players[1].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[1].PlacePiece(board, "road", random.choice(roads), 0)
    players[1].PlacePiece(board, "road", roads[0], 0)

    index = board.BestSpotRemaining()
    players[2].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[2].PlacePiece(board, "road", random.choice(roads), 0)
    players[2].PlacePiece(board, "road", roads[0], 0)

    index = board.BestSpotRemaining()
    players[2].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[2].PlacePiece(board, "road", random.choice(roads), 0)
    players[2].PlacePiece(board, "road", roads[0], 0)

    index = board.BestSpotRemaining()
    players[1].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[1].PlacePiece(board, "road", random.choice(roads), 0)
    players[1].PlacePiece(board, "road", roads[0], 0)

    index = board.BestSpotRemaining()
    players[0].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[0].PlacePiece(board, "road", random.choice(roads), 0)
    players[0].PlacePiece(board, "road", roads[0], 0)

def GameOver(players):
    for player in players:
        if player.victoryPoints >= 10:
            return True
    return False

def PrintPlayers(players):
    for player in players:
        print(player)

def DiscardHalfHand(players):
    for player in players:
        player.DiscardHalfHand()

if __name__ == "__main__":
    board = Board() 

    players = []
    for i in range(3):
        players.append(Player(i))

    """
    players[0].PlacePiece(board, "settlement", 11, 0)
    players[0].PlacePiece(board, "settlement", 22, 0)
    players[0].PlacePiece(board, "settlement", 40, 0)
    players[0].PlacePiece(board, "settlement", 29, 0)
    """
    SetUp(players, board)
    board.PrintBoard()
    

    SetUp(players, board)

    playerIndex = 0
    turn = 0

    print("\nStart of Game:\n")

    while not GameOver(players) and turn <= 25:
        player = players[playerIndex]

        roll = RollDice()
        if roll == 7:
            DiscardHalfHand(players)
            player.PlaceRobber(board, turn)
        else:
            board.DrawResources(players, roll)


        player.BuildingAction(board, turn)
        """
        action = True
        while not action:
            action = player.BuildingAction(board, turn) or player.TradeIn()
            # print("turn: {} action: {}".format(turn, action))
        """

        playerIndex += 1
        if playerIndex >= len(players):
            turn += 1
            playerIndex = 0

    print("\nEnd of Game:\n")
    board.PrintBoard()

    PrintPlayers(players)
