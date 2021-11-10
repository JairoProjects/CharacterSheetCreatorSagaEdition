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

class Defense():
	def __init__(self, charlevel, abilitymodifier):
		self.level=charlevel
		self.abilitymodifier=abilitymodifier
		self.value=10
		self.setValue()

	def setValue(self):
		self.value=self.value+self.level+self.abilitymodifier
