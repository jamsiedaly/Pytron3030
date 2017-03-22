import copy

class Hitbox():

	def __init__(self, object):
	
		self.y1 = [object.centerY]
		self.x1 = [object.centerX]
		self.heigth = object.rect.y
		self.width = object.rect.x
		self.y2 = lambda: self.y1[0][0] + self.heigth
		self.x2 = lambda: self.x1[0][0] + self.width  
