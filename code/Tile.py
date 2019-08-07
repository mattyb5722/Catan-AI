

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