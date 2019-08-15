""" Final Project AI Fiction in Fact """
import random

from Board import Board
from Player import Player

def RollDice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
    return x + y

def SetUpPlacement(player):
    done = False
    while not done:
        index = random.randint(0, 53)
        index = board.BestSpotRemaining()
        done = player.PlacePiece(board, "settlement", index, 0)

    roads = board.ConnectedEdges(index, "vertex")
    # players[0].PlacePiece(board, "road", random.choice(roads), 0)
    player.PlacePiece(board, "road", roads[0], 0)


def SetUp(players, board):
    # index = board.BestSpotRemaining()

    SetUpPlacement(players[0])
    SetUpPlacement(players[1])
    SetUpPlacement(players[2])
    SetUpPlacement(players[2])
    SetUpPlacement(players[1])
    SetUpPlacement(players[0])
    
def GameOver(players):
    for player in players:
        if player.victoryPoints >= 7:
            return True
    return False

def Winner(players):
    if players[0].victoryPoints > players[1].victoryPoints and players[0].victoryPoints > players[2].victoryPoints:
        return 0
    elif players[1].victoryPoints > players[2].victoryPoints:
        return 1
    return 2

def PrintPlayers(players):
    for player in players:
        print(player)

def DiscardHalfHand(players):
    for player in players:
        player.DiscardHalfHand()

if __name__ == "__main__":

    playersWins =  [0, 0, 0]
    gamesNotCompleted = 0
    tooManyVictoryPoints = 0

    for game in range(1000):
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
        # board.PrintBoard()
        
        playerIndex = 0
        turn = 0

        # print("\nStart of Game:\n")

        while not GameOver(players) and turn < 1000:
            player = players[playerIndex]

            roll = RollDice()
            if roll == 7:
                DiscardHalfHand(players)
                player.PlaceRobber(board, turn)
            else:
                board.DrawResources(players, roll)


            # player.BuildingAction(board, turn)
            
            action = True
            while action:
                A = player.BuildingAction(board, turn)
                B = player.TradeIn(turn)

                action = A or B 

            playerIndex += 1
            if playerIndex >= len(players):
                turn += 1
                playerIndex = 0

        # print("\nEnd of Game:\n")
        # board.PrintBoard()

        PrintPlayers(players)
        print()

        if (turn >= 1000):
            gamesNotCompleted += 1
        else:
            playersWins[Winner(players)] += 1 

            for i in range(3):
                if players[i].victoryPoints > 7:
                    tooManyVictoryPoints += 1

    print("Player 1 won {} games".format(playersWins[0]))
    print("Player 2 won {} games".format(playersWins[1]))
    print("Player 3 won {} games".format(playersWins[2]))
    print("{} Games were not completed".format(gamesNotCompleted))
    print("{} Games Finished with too many victory points".format(tooManyVictoryPoints))
