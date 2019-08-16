""" Final Project AI Fiction in Fact """
import random
import csv
from Board import Board
from Player import Player
from Tile import Tile

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
    player.PlacePiece(board, "road", random.choice(roads), 0)

def PrintToCSV(players, board, num):
    i = 1
    for player in players:
        newlist = []
        newlist.append(num)
        newlist.append(i)
        i += 1
        newlist.append(player.victoryPoints)
        wood = 0
        sheep = 0
        brick = 0
        ore = 0
        wheat = 0
        Vertex1 = board.vertices[player.settlements[0]]
        Vertex2 = board.vertices[player.settlements[1]]
        tiles1 = []
        tiles2 = []

        connectedTo1 = len(Vertex1.tilesConnectedTo)
        connectedTo2 = len(Vertex2.tilesConnectedTo)

        for tile in range(0, 3):
            if tile < connectedTo1:
                tiles1.append(board.tiles[Vertex1.tilesConnectedTo[tile]])
            else:
                tiles1.append(Tile(0, "ocean", [], []))
            if tile < connectedTo2:
                tiles2.append(board.tiles[Vertex2.tilesConnectedTo[tile]])
            else:
                tiles2.append(Tile(0, "ocean", [], []))
    

        for tile in range(0,3):
            if(tiles1[tile].resource == "wood"):
                wood += NumToProbability(tiles1[tile].value)

            elif(tiles1[tile].resource  == "sheep"):
                sheep += NumToProbability(tiles1[tile].value)

            elif(tiles1[tile].resource  == "brick"):
                brick += NumToProbability(tiles1[tile].value)

            elif(tiles1[tile].resource  == "ore"):
                ore += NumToProbability(tiles1[tile].value)

            elif(tiles1[tile].resource  == "wheat"):
                wheat += NumToProbability(tiles1[tile].value)
        
        for tile in range(0,3):
            if( tiles2[tile].resource == "wood"):
                wood += NumToProbability( tiles2[tile].value)

            elif( tiles2[tile].resource  == "sheep"):
                sheep += NumToProbability( tiles2[tile].value)

            elif( tiles2[tile].resource  == "brick"):
                brick += NumToProbability( tiles2[tile].value)

            elif( tiles2[tile].resource  == "ore"):
                ore += NumToProbability( tiles2[tile].value)

            elif( tiles2[tile].resource  == "wheat"):
                wheat += NumToProbability( tiles2[tile].value)

        newlist.append(ore)
        newlist.append(wood)
        newlist.append(wheat)
        newlist.append(brick)
        newlist.append(sheep)
        newlist.append(ore + wood + wheat + brick + sheep)
        with open('outdata.csv', 'a') as myfile:
            wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, lineterminator = '\n')
            wr.writerow(newlist)
            myfile.close()

def NumToProbability(number):
    if number == 2 or number == 12:
        return 2.78
    elif number == 3 or number == 11:
        return 5.56
    elif number == 4 or number == 10:
        return 8.33
    elif number == 5 or number == 9:
        return 11.11
    else:
        return 13.89

def SetUp(players, board):
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

    for game in range(100):
        board = Board() 

        players = []
        for i in range(3):
            players.append(Player(i))

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
        # PrintPlayers(players)
        # print()

        if (turn >= 1000):
            gamesNotCompleted += 1
        else:
            print("Player {} won the game".format(Winner(players)) )

            playersWins[Winner(players)] += 1 

            for i in range(3):
                if players[i].victoryPoints > 7:
                    tooManyVictoryPoints += 1
            PrintToCSV(players, board, game)

    print("\nPlayer 1 won {} games".format(playersWins[0]))
    print("Player 2 won {} games".format(playersWins[1]))
    print("Player 3 won {} games".format(playersWins[2]))
    print("{} Games were not completed".format(gamesNotCompleted))
    print("{} Games Finished with too many victory points".format(tooManyVictoryPoints))
    
