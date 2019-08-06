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

    Make sure to put error messages in 

"""

class Piece:
    def __init__(self, ID, playerID):
        self.ID = ID
        self.playerID = playerID

    def __str__(self):
        return "ID {}, player: {}\n".format(self.ID, self.playerID)

class Player:
    def __init__(self, ID):
        self.ID     = ID        # Index of player in players list
        self.brick  = 0
        self.rock   = 0
        self.sheep  = 0
        self.wheat  = 0
        self.wood   = 0
        self.victory_points = 0 # settlements + (2 * cities)

    def __str__(self):
        return "ID: {}, brick: {}, rock: {}, sheep: {}, wheat: {}, wood: {}".format(self.ID, self.brick, self.rock, self.sheep, self.wheat, self.wood)

    def PlacePiece(self, board, pieceID, index):
        board.PlacePiece(self.ID, pieceID, index)


    def AddResource(self, resource, amount):
        if resource == "brick":
            self.brick += amount
        elif resource == "rock":
            self.rock += amount
        elif resource == "sheep":
            self.sheep += amount
        elif resource == "wheat":
            self.wheat += amount
        elif resource == "wood":
            self.wood += amount

class Tile:
    def __init__(self, value, resource, vertices, edges):
        # robber = True / False depending if it's occupying that tile
        # value = 0 for desert; otherwise, it's the number for the tile
        if value == 0:
            self.robber = True
        else:
            self.robber = False

        self.resource = resource
        self.value = value
        # Start in the North West (NW) and goes clockwise
        # Indexes of vertices on the board
        self.vertices = vertices
        # Indexes of edges on the board
        self.edges = edges

    def PlaceRobber(self):
        self.robber = True

    def __str__(self):
        statement = "Value {}, resource: {}\n".format(self.value, self.resource)
        statement += "    Vertices:" +  str(self.vertices) + "\n"
        statement += "    Edges:" +  str(self.edges) + "\n"
        return statement

class Board:
    def __init__(self):
        self.tiles = [None] * 19
        self.vertices = [None] * 54
        self.sides = [None] * 72

        self.PlaceTiles()

    def __str__(self):
        statement = "Tiles\n"

        for tile in self.tiles:
            statement += "    " + str(tile)

        statement += "\nPieces (Vertices):\n"
        for piece in self.vertices:
            statement += "    " + str(piece)

        statement += "\nPieces (Sides):\n"
        for piece in self.sides:
            statement += "    " + str(piece)

        return statement


    def PlaceTiles(self):
        numberOrder = [5, 10, 8, 
                      2, 9, 3, 4, 
                    6, 4, 11, 6, 11,
                      3, 5, 0, 12, 
                      8, 10, 9]
        resourceOrder = ["wheat", "brick", "brick",
                    "sheep", "wood", "sheep", "rock",
                  "rock", "wheat", "wood", "wood", "wheat",
                    "brick", "sheep", "desert", "wheat",
                        "rock", "sheep", "wood"]

        row = 0

        sides = [0, 1, 7, 12, 11, 6]
        vertices = [0, 1, 2, 10, 9, 8]

        for i in range(len(numberOrder)):
            
            self.tiles[i] = Tile(numberOrder[i], resourceOrder[i], vertices.copy(), sides.copy())

            if row == 0 and i == 2:
                sides = [10, 11, 19, 25, 24, 18]
                vertices = [7, 8, 9, 19, 18, 17]
                row += 1
            elif row == 1 and i == 6:
                sides = [23, 24, 34, 40, 39, 33]
                vertices = [16, 17, 18, 29, 28, 27]
                row += 1
            elif row == 2 and i == 11:
                sides = [40, 41, 50, 55, 54, 49]
                vertices = [28, 29, 30, 40, 39, 38]
                row += 1
            elif row == 3 and i == 15:
                sides = [55, 56, 63, 67, 66, 62]
                vertices = [39, 40, 41, 49, 48, 47]
                row += 1
            else:            
                sides[0] += 2
                sides[1] += 2
                sides[3] += 2
                sides[4] += 2

                sides[2] += 1
                sides[5] += 1

                vertices[0] += 2
                vertices[1] += 2
                vertices[2] += 2
                vertices[3] += 2
                vertices[4] += 2
                vertices[5] += 2

    def PlacePiece(self, playerID, pieceID, index):
        if pieceID ==  "road":
            if self.sides[index] == None:
                self.sides[index] = Piece(pieceID, playerID)
                print("Player {} placed a {} at {}".format(playerID, pieceID, index))
            else:
                print("ERROR: INVALID PIECE LOCATION")
        elif pieceID == "settlement" or pieceID == "city":
            if self.vertices[index] == None:
                self.vertices[index] = Piece(pieceID, playerID)
                print("Player {} placed a {} at {}".format(playerID, pieceID, index))
            else:
                print("ERROR: INVALID PIECE LOCATION")
        else:
            print("ERROR: INVALID PIECEID")

    def DrawResources(self, plyaers, roll):
        for tile in self.tiles:
            if tile.value == roll and tile.robber == False:
                for vertexIndex in tile.vertices:
                    vertex = self.vertices[vertexIndex]
                    if not vertex == None:
                        playerIndex = vertex.playerID
                        plyaers[playerIndex].AddResource(tile.resource, 1)

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
    # print(RollDice())

    board = Board() 
    # print(board)


    players = []
    players.append(Player(0))
    players.append(Player(1))
    players.append(Player(2))

    players[0].PlacePiece(board, "settlement", 0)

    # print(board)

    board.DrawResources(players, 5)

    print(players[0])



