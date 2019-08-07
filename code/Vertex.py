

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