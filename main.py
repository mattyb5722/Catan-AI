import random


"""
Notes:

Board: 
    Tiles: 19 Total
        3 - 4 - 5 - 4 - 3

    Vertices: 54 Total
        7 - 9 - 11 - 11 - 9 - 7

    Sides: 72 Total
        6 - 4 - 8 - 5 - 10 - 6 -
        10 - 5 - 8 - 4 - 6


Documentation:
    Coding Format:
        functions : Capitize the first letter in each word
        variables : Capitize the first letter in each word except the first

        Indent side of 4

    Make sure to put error messages in 

"""
class Edge:
    def __init__(self):
        self.piece = None
        self.tilesConnectedTo = []
        self.verticesConnectedTo = []

    def __str__(self):
        statement = "   Piece: " + str(self.piece) + "\n"
        statement += "   tilesConnectedTo: " + str(self.tilesConnectedTo) + "\n"
        statement += "   verticesConnectedTo: " + str(self.verticesConnectedTo) + "\n"
        return statement

    def AddTileConnection(self, index):
        if index not in self.tilesConnectedTo:
            self.tilesConnectedTo.append(index)

    def AddVertexConnection(self, index):
        if index not in self.verticesConnectedTo:
            self.verticesConnectedTo.append(index)

class Vertex:
    def __init__(self):
        self.piece = None
        self.tilesConnectedTo = []
        self.edgeConnectedTo = []

    def __str__(self):
        statement = "   Piece: " + str(self.piece) + "\n"
        statement += "   tilesConnectedTo: " + str(self.tilesConnectedTo) + "\n"
        statement += "   edgeConnectedTo: " + str(self.edgeConnectedTo) + "\n"
        return statement

    def AddTileConnection(self, index):
        if index not in self.tilesConnectedTo:
            self.tilesConnectedTo.append(index)

    def AddEdgeConnection(self, index):
        if index not in self.edgeConnectedTo:
            self.edgeConnectedTo.append(index)

class Piece:
    def __init__(self, ID, playerID):
        self.ID = ID
        self.playerID = playerID

    def __str__(self):
        return "Player {}'s {}".format(self.playerID, self.ID)

class Player:
    def __init__(self, ID):
        self.ID     = ID        # Index of player in players list
        self.brick  = 0
        self.ore   = 0
        self.sheep  = 0
        self.wheat  = 0
        self.wood   = 0
        self.victory_points = 0 # settlements + (2 * cities)

    def __str__(self):
        return "ID: {}, brick: {}, ore: {}, sheep: {}, wheat: {}, wood: {}".format(self.ID, self.brick, self.ore, self.sheep, self.wheat, self.wood)

    def PlacePiece(self, board, pieceID, index):
        possible = board.PlacePiece(self.ID, pieceID, index)
        if possible == True and pieceID == "settlement":
            self.victory_points += 1
        elif possible == True and pieceID == "city":
            self.victory_points += 2

    def AddResource(self, resource, amount):
        if resource == "brick":
            self.brick += amount
        elif resource == "ore":
            self.ore += amount
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
        statement = ""
        """
        statement _+= "Tiles\n"
        for i in range(len(self.tiles)):
            statement += "Tile " + str(i) + ": " + str(self.tiles[i])
        """

        statement += "\nVertices:\n"
        for i in range(len(self.vertices)):
            statement += "Vertex " + str(i) + ":\n" + str(self.vertices[i])

        """
        statement += "\nEdges:\n"
        for i in range(len(self.sides)):
            statement += "Edges " + str(i) + ":\n" + str(self.sides[i])
        """

        return statement

    def PlaceTiles(self):
        numberOrder = [5, 10, 8, 
                      2, 9, 3, 4, 
                    6, 4, 11, 6, 11,
                      3, 5, 0, 12, 
                       8, 10, 9]
        resourceOder = ["wheat", "brick", "brick",
                    "sheep", "wood", "sheep", "ore",
                  "ore", "wheat", "wood", "wood", "wheat",
                    "brick", "sheep", "desert", "wheat",
                        "ore", "sheep", "wood"]

        row = 0

        sidesTemp = [0, 1, 7, 12, 11, 6]
        verticesTemp = [0, 1, 2, 10, 9, 8]

        for i in range(len(numberOrder)):
            self.tiles[i] = Tile(numberOrder[i], resourceOder[i], verticesTemp.copy(), sidesTemp.copy())

            for j in range(len(verticesTemp)):
                index = verticesTemp[j]

                if self.vertices[index] == None:
                    self.vertices[index] = Vertex()
                
                self.vertices[index].AddTileConnection(i)

                self.vertices[index].AddEdgeConnection(sidesTemp[j])

                if j == 0:
                    self.vertices[index].AddEdgeConnection(sidesTemp[5])
                else:
                    self.vertices[index].AddEdgeConnection(sidesTemp[j-1])


            for j in range(len(sidesTemp)):
                index = sidesTemp[j]

                if self.sides[index] == None:
                    self.sides[index] = Edge()
                
                self.sides[index].tilesConnectedTo.append(i)

                self.sides[index].AddVertexConnection(verticesTemp[j])

                if j == 5:
                    self.sides[index].AddVertexConnection(verticesTemp[0])
                else:
                    self.sides[index].AddVertexConnection(verticesTemp[j+1])


            if row == 0 and i == 2:
                sidesTemp = [10, 11, 19, 25, 24, 18]
                verticesTemp = [7, 8, 9, 19, 18, 17]
                row += 1
            elif row == 1 and i == 6:
                sidesTemp = [23, 24, 34, 40, 39, 33]
                verticesTemp = [16, 17, 18, 29, 28, 27]
                row += 1
            elif row == 2 and i == 11:
                sidesTemp = [40, 41, 50, 55, 54, 49]
                verticesTemp = [28, 29, 30, 40, 39, 38]
                row += 1
            elif row == 3 and i == 15:
                sidesTemp = [55, 56, 63, 67, 66, 62]
                verticesTemp = [39, 40, 41, 49, 48, 47]
                row += 1
            else:            
                sidesTemp[0] += 2
                sidesTemp[1] += 2
                sidesTemp[3] += 2
                sidesTemp[4] += 2

                sidesTemp[2] += 1
                sidesTemp[5] += 1

                verticesTemp[0] += 2
                verticesTemp[1] += 2
                verticesTemp[2] += 2
                verticesTemp[3] += 2
                verticesTemp[4] += 2
                verticesTemp[5] += 2

    def PlacePiece(self, playerID, pieceID, index):
        if pieceID ==  "road":
            if self.sides[index].piece == None:
                print("Player {} placed a {} at {}".format(playerID, pieceID, index))
                self.sides[index].piece = Piece(pieceID, playerID)
                return True
            else:
                print("ERROR: INVALID PIECE LOCATION")
        elif pieceID == "settlement" or pieceID == "city":
            if self.vertices[index].piece == None:
                print("Player {} placed a {} at {}".format(playerID, pieceID, index))
                self.vertices[index].piece = Piece(pieceID, playerID)
                return True
            else:
                print("ERROR: INVALID PIECE LOCATION")
        else:
            print("ERROR: INVALID PIECEID")
        return False

    def DrawResources(self, plyaers, roll):
        for tile in self.tiles:
            if tile.value == roll and tile.robber == False:
                for vertexIndex in tile.vertices:
                    vertex = self.vertices[vertexIndex]
                    if not vertex == None:
                        playerIndex = vertex.playerID
                        plyaers[playerIndex].AddResource(tile.resource, 1)

    def BestSpotRemaining(self):
        probabilities = [0] * 54

        for tile in self.tiles:
            for vertexIndex in tile.vertices:
                if not self.vertices[vertexIndex].piece == None:
                    probabilities[vertexIndex] = 0
                else:
                    probabilities[vertexIndex] += NumberToProbability(tile.value)

        return probabilities.index(max(probabilities))

    def ConnectedVertices(self, currentIndex):
        return




    def ConnectedSides(self, currentIndex):
        return


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

def SetUp(players, board):
    index = board.BestSpotRemaining()
    players[0].PlacePiece(board, "settlement", index)

    index = board.BestSpotRemaining()
    players[1].PlacePiece(board, "settlement", index)

    index = board.BestSpotRemaining()
    players[2].PlacePiece(board, "settlement", index)

    index = board.BestSpotRemaining()
    players[2].PlacePiece(board, "settlement", index)

    index = board.BestSpotRemaining()
    players[1].PlacePiece(board, "settlement", index)

    index = board.BestSpotRemaining()
    players[0].PlacePiece(board, "settlement", index)


if __name__ == "__main__":
    board = Board() 
    # print(board)

    players = []
    for i in range(3):
        players.append(Player(i))

    # players[0].PlacePiece(board, "settlement", 0)
    # print(board)

    # board.DrawResources(players, 5)
    # print(players[0])

    # print(board.BestSpotRemaining())

    SetUp(players, board)
    print(board)



