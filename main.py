""" Final Project AI Fiction in Fact """
import random

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

class Edge:
    def __init__(self):
        self.piece = None
        self.tilesConnectedTo = []
        self.verticesConnectedTo = []
        self.edgeConnectedTo = []

    def __str__(self):
        statement = "Piece: " + str(self.piece) + "\n"
        """
        statement += "   tilesConnectedTo: " + str(self.tilesConnectedTo) + "\n"
        statement += "   verticesConnectedTo: " + str(self.verticesConnectedTo) + "\n"
        statement += "   edgeConnectedTo: " + str(self.edgeConnectedTo) + "\n"

        """
        return statement

    def AddTileConnection(self, index):
        if index not in self.tilesConnectedTo:
            self.tilesConnectedTo.append(index)

    def AddVertexConnection(self, index):
        if index not in self.verticesConnectedTo:
            self.verticesConnectedTo.append(index)

    def AddEdgeConnection(self, index):
        if index not in self.edgeConnectedTo:
            self.edgeConnectedTo.append(index)

class Vertex:
    def __init__(self):
        self.piece = None
        self.tilesConnectedTo = []
        self.verticesConnectedTo = []
        self.edgeConnectedTo = []

    def __str__(self):
        statement = "Piece: " + str(self.piece) + "\n"
        """
        statement += "   tilesConnectedTo: " + str(self.tilesConnectedTo) + "\n"
        statement += "   verticesConnectedTo: " + str(self.verticesConnectedTo) + "\n"
        statement += "   edgeConnectedTo: " + str(self.edgeConnectedTo) + "\n"
        """
        return statement

    def AddTileConnection(self, index):
        if index not in self.tilesConnectedTo:
            self.tilesConnectedTo.append(index)

    def AddVertexConnection(self, index):
        if index not in self.verticesConnectedTo:
            self.verticesConnectedTo.append(index)

    def AddEdgeConnection(self, index):
        if index not in self.edgeConnectedTo:
            self.edgeConnectedTo.append(index)

class Piece:
    def __init__(self, ID, playerID):
        self.ID = ID
        self.playerID = playerID

    def __str__(self):
        return "Player {}'s {}".format(self.playerID, self.ID)

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

    def __str__(self):
        statement = "Value {}, resource: {}\n".format(self.value, self.resource)
        statement += "    Vertices:" +  str(self.vertices) + "\n"
        statement += "    Edges:" +  str(self.edges) + "\n"
        return statement

class Player:
    def __init__(self, ID):
        self.ID     = ID        # Index of player in players list
        self.brick  = 0
        self.ore    = 0
        self.sheep  = 0
        self.wheat  = 0
        self.wood   = 0
        self.victoryPoints = 0  # settlements + (2 * cities)
        self.settlements = []
        self.roads = []

    def __str__(self):
        return "ID: {}, brick: {}, ore: {}, sheep: {}, wheat: {}, wood: {}"\
            .format(self.ID, self.brick, self.ore, self.sheep, self.wheat, self.wood)

    def PlacePiece(self, board, pieceID, index, turn):
        possible = board.PlacePiece(self.ID, pieceID, index)

        if possible == True:
            print("Turn: {} Player {} placed a {} at {}".format(turn, self.ID, pieceID, index))

            if pieceID == "road":
                self.roads.append(index)
            elif pieceID == "settlement":
                self.victoryPoints += 1
                self.settlements.append(index)

    def PossibleBuildings(self):
        output = []
        if self.brick > 1 and self.wood > 1:
            output.append("road")
        if self.brick > 1 and self.sheep > 1 and self.wheat > 1 and self.wood > 1:
            output.append("settlement")
        return output

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

    def BuildingAction(self, board):                                # Need AI
        buildings = self.PossibleBuildings()

        if len(buildings) > 0:
            # building = random.choice(buildings)
            building = buildings[-1]

            if building == "road":
                roads = board.PossibleRoadPositions(self)
                if len(roads) > 0:
                    self.PlacePiece(board, "road", random.choice(roads), turn)
                    self.brick -= 1
                    self.wood -= 1

            elif building == "settlement":
                settlements = board.PossibleSettlementPositions(self)
                if len(settlements) > 0:
                    self.PlacePiece(board, "settlement", random.choice(settlements), turn)
                    self.brick -= 1
                    self.sheep -= 1
                    self.wheat -= 1
                    self.wood -= 1

    def PlaceRobber(self, board, turn):                             # Need AI
        robberIndex = random.randint(0, 18)
        board.PlaceRobber(self, turn, robberIndex)

    def FourForOne(self, need):                                     # Need AI
        have = []
        if self.brick >= 4:
            have.append("brick")
        if self.ore >= 4:
            have.append("ore")
        if self.sheep >= 4:
            have.append("sheep")
        if self.wheat >= 4:
            have.append("wheat")
        if self.wood >= 4:
            have.append("wood")

        if len(have) > 0: 
            choice = random.choice(have)

            if choice == "brick":
                self.brick -= 4
            elif choice == "ore":
                self.ore -= 4
            elif choice == "sheep":
                self.sheep -= 4
            elif choice == "wheat":
                self.wheat -= 4
            elif choice == "wood":
                self.wood -= 4

            if need == "brick":
                self.brick += 1
            elif need == "ore":
                self.ore += 1
            elif need == "sheep":
                self.sheep += 1
            elif need == "wheat":
                self.wheat += 1
            elif need == "wood":
                self.wood += 1

class Board:
    def __init__(self):
        self.tiles = [None] * 19
        self.vertices = [None] * 54
        self.edges = [None] * 72

        self.robberIndex = 0

        self.PlaceTiles()

    def __str__(self):
        statement = ""

        statement += "Tiles\n"
        for i in range(len(self.tiles)):
            statement += "Tile " + str(i) + ": " + str(self.tiles[i])

        statement += "\nVertices:\n"
        for i in range(len(self.vertices)):
            statement += "Vertex " + str(i) + ": " + str(self.vertices[i])

        statement += "\nEdges:\n"
        for i in range(len(self.edges)):
            statement += "Edges " + str(i) + ": " + str(self.edges[i])
        
        statement += "robber is on tile {}"

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

        robberIndex = 14

        row = 0

        edgesTemp = [0, 1, 7, 12, 11, 6]
        verticesTemp = [0, 1, 2, 10, 9, 8]

        for i in range(len(numberOrder)):
            self.tiles[i] = Tile(numberOrder[i], resourceOder[i], verticesTemp.copy(), edgesTemp.copy())

            for j in range(len(verticesTemp)):
                index = verticesTemp[j]

                if self.vertices[index] == None:
                    self.vertices[index] = Vertex()
                
                self.vertices[index].AddTileConnection(i)

                if j == 0:
                    self.vertices[index].AddVertexConnection(verticesTemp[5])
                else:
                    self.vertices[index].AddVertexConnection(verticesTemp[j-1])
                if j == 5:
                    self.vertices[index].AddVertexConnection(verticesTemp[0])
                else:
                    self.vertices[index].AddVertexConnection(verticesTemp[j+1])


                self.vertices[index].AddEdgeConnection(edgesTemp[j])
                if j == 0:
                    self.vertices[index].AddEdgeConnection(edgesTemp[5])
                else:
                    self.vertices[index].AddEdgeConnection(edgesTemp[j-1])


            for j in range(len(edgesTemp)):
                index = edgesTemp[j]

                if self.edges[index] == None:
                    self.edges[index] = Edge()
                
                self.edges[index].tilesConnectedTo.append(i)

                self.edges[index].AddVertexConnection(verticesTemp[j])
                if j == 5:
                    self.edges[index].AddVertexConnection(verticesTemp[0])
                else:
                    self.edges[index].AddVertexConnection(verticesTemp[j+1])

                if j == 0:
                    self.edges[index].AddEdgeConnection(edgesTemp[5])
                else:
                    self.edges[index].AddEdgeConnection(edgesTemp[j-1])
                if j == 5:
                    self.edges[index].AddEdgeConnection(edgesTemp[0])
                else:
                    self.edges[index].AddEdgeConnection(edgesTemp[j+1])

            if row == 0 and i == 2:
                edgesTemp = [10, 11, 19, 25, 24, 18]
                verticesTemp = [7, 8, 9, 19, 18, 17]
                row += 1
            elif row == 1 and i == 6:
                edgesTemp = [23, 24, 34, 40, 39, 33]
                verticesTemp = [16, 17, 18, 29, 28, 27]
                row += 1
            elif row == 2 and i == 11:
                edgesTemp = [40, 41, 50, 55, 54, 49]
                verticesTemp = [28, 29, 30, 40, 39, 38]
                row += 1
            elif row == 3 and i == 15:
                edgesTemp = [55, 56, 63, 67, 66, 62]
                verticesTemp = [39, 40, 41, 49, 48, 47]
                row += 1
            else:            
                edgesTemp[0] += 2
                edgesTemp[1] += 2
                edgesTemp[3] += 2
                edgesTemp[4] += 2

                edgesTemp[2] += 1
                edgesTemp[5] += 1

                verticesTemp[0] += 2
                verticesTemp[1] += 2
                verticesTemp[2] += 2
                verticesTemp[3] += 2
                verticesTemp[4] += 2
                verticesTemp[5] += 2

    def PlacePiece(self, playerID, pieceID, index):
        if pieceID ==  "road":
            if self.ValidRoadLoc(index):
                self.edges[index].piece = Piece(pieceID, playerID)
                return True
            else:
                print("ERROR: INVALID PIECE LOCATION")

        elif pieceID == "settlement":
            if self.ValidSettlementLoc(index):
                self.vertices[index].piece = Piece(pieceID, playerID)
                return True
            else:
                print("ERROR: INVALID PIECE LOCATION")
        else:
            print("ERROR: INVALID PIECE ID")
        return -1

    def DrawResources(self, plyaers, roll):
        for tile in self.tiles:
            if tile.value == roll and tile.robber == False:
                for vertexIndex in tile.vertices:
                    piece = self.vertices[vertexIndex].piece
                    if not piece == None:
                        playerIndex = piece.playerID
                        plyaers[playerIndex].AddResource(tile.resource, 1)

    def BestSpotRemaining(self):                                    # Need AI
        probabilities = [0] * 54
        for vertexIndex in range(len(self.vertices)):
            vertex = self.vertices[vertexIndex]
            if self.ValidSettlementLoc(vertexIndex):
                for tileIndex in vertex.tilesConnectedTo:
                    probabilities[vertexIndex] += NumberToProbability(self.tiles[tileIndex].value)
        return probabilities.index(max(probabilities))

    def ConnectedVertices(self, index):
        if startingType == "vertex":
            return self.vertices[index].verticesConnectedTo
        elif startingType == "road":
            return self.edges[index].verticesConnectedTo

    def ConnectedEdges(self, index, startingType):
        if startingType == "vertex":
            return self.vertices[index].edgeConnectedTo
        elif startingType == "road":
            return self.edges[index].edgeConnectedTo

    def PossibleRoadPositions(self, player):
        output = set()                                                      # New roads that would be connected to other roads

        for edgeIndex in player.roads:                                      # Road locations
            for edgeIndex2 in self.edges[edgeIndex].edgeConnectedTo:        # Edges connected that that road
                if self.ValidRoadLoc(edgeIndex2):                                # There is no other roads on this new edge
                    output.add(edgeIndex2)                                  # This new edge is a valid road placement

        return list(output)

    def PossibleSettlementPositions(self, player):
        output = set()
        for edgeIndex in player.roads:                                      # Road locations
            for vertexIndex in self.edges[edgeIndex].verticesConnectedTo:   # vertices connected that that road
                if self.ValidSettlementLoc(vertexIndex):                    # Is this a valid settlement placement
                    output.add(vertexIndex)                                 # This new edge is a valid settlement placement

        return list(output)

    def ValidSettlementLoc(self, index):
        start = self.vertices[index]
        if start.piece != None:                                             # There is not a settlement already there    
            return False
        for vertexIndex in start.verticesConnectedTo:                       # Vertices connected to start
            if self.vertices[vertexIndex].piece != None:                    # There are not settlements there either
                return False
        return True

    def ValidRoadLoc(self, index):
        if self.edges[index].piece == None:                                 # There is no other roads on this new edge
            return True
        return False

    def PlaceRobber(self, player, turn, index):
        self.tiles[self.robberIndex].robber = False
        self.robberIndex = index
        self.tiles[self.robberIndex].robber = True
        print("Turn: {} Player {} placed the robber on tile {}".format(turn, player.ID, self.robberIndex))

def RollDice():
    x = random.randint(1, 6)
    y = random.randint(1, 6)
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
    players[0].PlacePiece(board, "settlement", index, 0)
    roads = board.ConnectedEdges(index, "vertex")
    # players[0].PlacePiece(board, "road", random.choice(roads), 0)
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

if __name__ == "__main__":
    board = Board() 
    # print(board)

    players = []
    for i in range(3):
        players.append(Player(i))

    """
    players[0].PlacePiece(board, "settlement", 11, 0)
    players[0].PlacePiece(board, "settlement", 22, 0)
    players[0].PlacePiece(board, "settlement", 40, 0)
    players[0].PlacePiece(board, "settlement", 29, 0)
    # print(board)
    """
    

    # board.DrawResources(players, 5)
    # print(players[0])

    # print(board.BestSpotRemaining())

    SetUp(players, board)

    # print(board)

    playerIndex = 0
    turn = 0

    print("\nStart of Game:\n")

    while not GameOver(players) and turn <= 25:
        player = players[playerIndex]

        roll = RollDice()
        if roll == 7:
            player.PlaceRobber(board, turn)
        else:
            board.DrawResources(players, roll)

        player.BuildingAction(board)

        playerIndex += 1
        if playerIndex >= len(players):
            turn += 1
            playerIndex = 0

    print("\nEnd of Game:\n")

    PrintPlayers(players)
