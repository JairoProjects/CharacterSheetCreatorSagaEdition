from setattack import setAttackWhenAttackIsEqualsLevel, setAttackWhenAttackIsNotEqualsLevel

class Charclass():
	def __init__(self, name, level):
		self.name=name
		self.level=level
		self.refbonus=0
		self.fortbonus=0
		self.wilbonus=0
		self.attackbonus=0
		self.setBonus()

	def setBonus(self):
		if self.name=="Jedi":
			self.refbonus=1
			self.fortbonus=1
			self.wilbonus=1
			self.attackbonus=setAttackWhenAttackIsEqualsLevel(self.level)
		if self.name=="Noble":
			self.refbonus=1
			self.wilbonus=2
			self.attackbonus=setAttackWhenAttackIsNotEqualsLevel(self.level)
		if self.name=="Granuja":
			self.refbonus=2
			self.wilbonus=1
			self.attackbonus=setAttackWhenAttackIsNotEqualsLevel(self.level)
		if self.name=="Explorador":
			self.refbonus=2
			self.fortbonus=1
			self.attackbonus=setAttackWhenAttackIsNotEqualsLevel(self.level)
		if self.name=="Soldado":
			self.refbonus=1
			self.fortbonus=2
			self.attackbonus=setAttackWhenAttackIsEqualsLevel(self.level)
