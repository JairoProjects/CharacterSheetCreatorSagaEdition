class Ability():
	def __init__(self, name, value):
		self.name=name
		self.value=value
		self.modifier=0
		self.setModifier()

	def setModifier(self):
		if self.value>=10:
			self.modifier=(self.value-10)//2
		else:
			self.modifier=(self.value-10)//2
