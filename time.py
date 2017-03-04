
class Time():

	def __init__(self, ai_settings):
	
		self.time = ai_settings.time()
		self.default = ai_settings.time()
		
	def update(self):
	
		self.time == self.time - 1
		
	def reset(self):
	
		self.time = self.default()