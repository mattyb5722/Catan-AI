import random



"""
Notes:

Probabilities:
    2 and 12: 1 / 36
    3 and 11: 2 / 36
    4 and 10: 3 / 36
    5 and 9 : 4 / 36
    6 and 8 : 5 / 36
    7       : 6 / 36


Board: 
    Tiles: 29 Total
        3 Tiles
        4 Tiles
        5 Tiles
        4 Tiles
        3 Tiles

    Vertices: 54 Total
        7 spots
        9 spots
        11 spots
        11 spots
        9 spots
        7 spots

    Sides: 72 Total
        6 spots
        4 spots
        8 spots
        5 spots
        10 spots
        6 spots
        10 spots
        5 spots
        8 spots
        4 spots
        6 spots


Documentation:
    Coding Format:
        functions : Capitize the first letter in each word
        variables : Capitize the first letter in each word except the first

        Indent side of 4

"""



class Player:
    def __init__(self, name, settlements, roads, brick, rock, sheep, wheat, wood, victory_points):
        self.name   = name #The ownership letter, e.g. player A, B, C, or D for a 4-player match
        self.settlements = settlements
        self.roads  = roads
        self.brick  = brick
        self.rock   = rock
        self.sheep  = sheep
        self.wheat  = wheat
        self.wood   = wood
        self.victory_points = settlements # + (2 * cities)

    def __init__(self, name):
        self.name   = name #The ownership letter, e.g. player A, B, C, or D for a 4-player match
        self.brick  = 0
        self.rock   = 0
        self.sheep  = 0
        self.wheat  = 0
        self.wood   = 0
        self.victory_points = 0 # settlements + (2 * cities)

    def PlacePiece(self, PieceID, index):

        return


        
class Tile:
    def __init__(self, value, resource):
        #robber = True / False depending if it's occupying that tile
        #value = 0 for desert; otherwise, it's the number for the tile
        self.robber = False
        self.resource = resource
        self.value = value
        #otherwise, every other prop will be a player ID or null for whether a corner/space is occupied, and who by

    def PlaceRobber(self):
        self.robber = True

    def __str__(self):
        return "Value {}, resource: {}\n".format(self.value, self.resource)

class Piece:
    def __init__(self, ID, playerID):
        self.ID = ID
        self.playerID = playerID

class Board:
    def __init__(self):
        self.tiles = [None] * 29
        self.verices = [None] * 54
        self.sides = [None] * 72

        self.PlaceTiles()


    def PlaceTiles(self):
        numberOrder = [5, 10, 8, 
                      2, 9, 3, 4, 
                    6, 4, 11, 6, 11,
                      3, 5, 0, 12, 
                      8, 10, 9]
        resourceOder = ["wheat", "brick", "brick",
                    "sheep", "wood", "sheep", "rock",
                  "rock", "wheat", "wood", "wood", "wheat",
                    "brick", "sheep", "desert", "wheat",
                        "rock", "sheep", "wood"]

        for i in range(len(numberOrder)):
            self.tiles.append(Tile(numberOrder[i], resourceOder[i]))

    def __str__(self):
        statement = ""
        for tile in self.tiles:
            statement += str(tile)
        return statement



def RollDice():
    x = random.randint(1,6)
    y = random.randint(1,6)
    return x + y

def NumberToProbability(number):
    """
    2 and 12: 1 / 36
    3 and 11: 2 / 36
    4 and 10: 3 / 36
    5 and 9 : 4 / 36
    6 and 8 : 5 / 36
    7       : 6 / 36
    """
    if number <= 7:
        return number - 1
    else:
        return 13 - number


if __name__ == "__main__":
    print(RollDice())

    board = Board() 
    print(board)


    players = []
    players.append(Player("A"))
    players.append(Player("B"))
    players.append(Player("C"))
