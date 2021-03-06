import random
from Board import Board


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
        self.cities = []

    def __str__(self):
        return "ID: {}, victoryPoints: {},  brick: {}, ore: {}, sheep: {}, wheat: {}, wood: {}"\
            .format(self.ID, self.victoryPoints, self.brick, self.ore, self.sheep, self.wheat, self.wood)

    def PlacePiece(self, board, pieceID, index, turn):
        possible = board.PlacePiece(self.ID, pieceID, index)

        if possible == True:
            # print("Turn: {} Player {} placed a {} at {}".format(turn, self.ID, pieceID, index))

            if pieceID == "road":
                self.roads.append(index)
            elif pieceID == "settlement":
                self.victoryPoints += 1
                self.settlements.append(index)
            elif pieceID == "city":
                self.victoryPoints += 1
                self.cities.append(index)
            return True
        return False

    def PossibleBuildings(self):
        output = []
        if self.brick > 1 and self.wood > 1:
            output.append("road")
        if self.brick >= 1 and self.sheep >= 1 and self.wheat >= 1 and self.wood >= 1:
            output.append("settlement")
        if self.ore > 2 and self.wheat > 1:
            output.append('city')        
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

    def BuildingAction(self, board, turn):                                # Need AI
        buildings = self.PossibleBuildings()

        if len(buildings) > 0:
            # building = random.choice(buildings)
            building = buildings[-1]

            if building == "settlement":
                settlements = board.PossibleSettlementPositions(self)
                if len(settlements) > 0:
                    if (self.PlacePiece(board, "settlement", random.choice(settlements), turn)):
                        self.brick -= 1
                        self.sheep -= 1
                        self.wheat -= 1
                        self.wood -= 1
                        return True
        
            elif building == "road":
                roads = board.PossibleRoadPositions(self)
                if len(roads) > 0:
                    if (self.PlacePiece(board, "road", random.choice(roads), turn)):
                        self.brick -= 1
                        self.wood -= 1
                        return True
            elif building == "city":
                if len(self.settlements) >= 1:
                    if (self.PlacePiece(board, "city", random.choice(self.settlements), turn)):
                        self.ore-=3
                        self.wheat-=2
                        return True
        return False


    def PlaceRobber(self, board, turn):                             # Need AI
        robberIndex = random.randint(0, 18)
        board.PlaceRobber(self, turn, robberIndex)


    def TradeIn(self, turn):
        if self.sheep == 0 and self.FourForOne("sheep", turn):
            return True
        if self.wheat == 0 and self.FourForOne("wheat", turn):
            return True
        if self.brick == 0 and self.FourForOne("brick", turn):
            return True
        if self.wood == 0 and self.FourForOne("wood", turn):
            return True
        # if self.ore == 0 and self.FourForOne("ore", turn):
        #     return True
        return False

    def FourForOne(self, need, turn):                                     # Need AI
        have = []
        if self.brick > 4:
            have.append("brick")
        if self.ore > 4:
            have.append("ore")
        if self.sheep > 4:
            have.append("sheep")
        if self.wheat > 4:
            have.append("wheat")
        if self.wood > 4:
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

            # print("Turn: {} Player {} traded 4 {} for 1 {}".format(turn, self.ID, choice, need))
            return True
        return False


    def DiscardHalfHand(self):
        handsize = self.brick + self.ore + self.sheep + self.wheat + self.wood
        if handsize > 7:
            for i in range(handsize//2):
                resource = random.choice(range(0,5))
                if resource == 0 and self.brick > 0:
                    self.brick -= 1
                elif resource == 1 and self.ore > 0:
                    self.ore -= 1
                elif resource == 2 and self.sheep > 0:
                    self.sheep -= 1
                elif resource == 3 and self.wheat > 0:
                    self.wheat -= 1
                elif resource == 4 and self.wood > 0:
                    self.wood -= 1
