import random

class Player:
	def __init__(self, name, settlements, roads, brick, rock, sheep, wheat, wood, victory_points):
		self.name 	= name #The ownership letter, e.g. player A, B, C, or D for a 4-player match
		self.settlements = settlements
		self.roads 	= roads
		self.brick 	= brick
		self.rock 	= rock
		self.sheep 	= sheep
		self.wheat 	= wheat
		self.wood 	= wood
		self.victory_points = settlements # + (2 * cities)
		
class Tile:
	def __init__(self, robber, value, resource, side1, side2, side3, side4, side5, side6, vertex1, vertex2, vertex3, vertex4, vertex5, vertex6):
		#robber = True / False depending if it's occupying that tile
		#value = 0 for desert; otherwise, it's the number for the tile
		self.robber = False
		self.resource	=	resource
		self.value = value
		#otherwise, every other prop will be a player ID or null for whether a corner/space is occupied, and who by 

def roll_dice(self):
    x=random.randint(1,6)
    y=random.randint(1,6)
    for i in range(n):
        z=x+y
    return z