import copy

class Hitbox():

	def __init__(self, object):
	
		self.y1 = [object.rect.y]
		self.x1 = [object.rect.x]
		self.heigth = object.rect.height
		self.width = object.rect.width
		self.y2 = lambda: self.y1[0] + self.heigth
		self.x2 = lambda: self.x1[0] + self.width  
