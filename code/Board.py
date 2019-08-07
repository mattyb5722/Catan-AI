from Edge import Edge
from Vertex import Vertex
from Piece import Piece
from Tile import Tile

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
