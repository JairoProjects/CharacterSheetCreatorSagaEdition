from setattack import setAttackWhenAttackIsEqualsLevel, setAttackWhenAttackIsNotEqualsLevel

class Charclass():
	def __init__(self, name, level):
		self.name=name
		self.level=level
		self.refbonus=0
		self.fortbonus=0
		self.wilbonus=0
		self.attackbonus=0
		self.numSkills=0
		self.skills=[]
		self.setBonus()

	def setBonus(self):
		if self.name=="Jedi":
			self.refbonus=1
			self.fortbonus=1
			self.wilbonus=1
			self.attackbonus=setAttackWhenAttackIsEqualsLevel(self.level)
			self.numSkills=2
			self.skills=["Acrobáticas", "Aguante", "Iniciativa", "Saltar", "Conocimiento(Tácticas)", "Conocimiento(Ciencias físicas)", "Conocimiento(Biología)", "Conocimiento(Burocracia)", "Mecánica", "Percepción", "Pilotar", "Usar la fuerza"]
		if self.name=="Noble":
			self.refbonus=1
			self.wilbonus=2
			self.attackbonus=setAttackWhenAttackIsNotEqualsLevel(self.level)
			self.numSkills=6
			self.skills=["Engañar", "Recoger información", "Iniciativa", "Conocimiento(Tácticas)", "Conocimiento(Ciencias físicas)", "Conocimiento(Biología)", "Conocimiento(Burocracia)", "Montar", "Percepción", "Pilotar", "Tratar heridas", "Persuasión", "Usar ordenadores"]
		if self.name=="Granuja":
			self.refbonus=2
			self.wilbonus=1
			self.attackbonus=setAttackWhenAttackIsNotEqualsLevel(self.level)
			self.numSkills=4
			self.skills=["Acrobáticas", "Engañar", "Recoger información", "Iniciativa", "Conocimiento(Tácticas)", "Conocimiento(Ciencias físicas)", "Conocimiento(Biología)", "Conocimiento(Burocracia)", "Mecánica", "Percepción", "Pilotar", "Usar ordenadores", "Persuasión", "Sigilo"]
		if self.name=="Explorador":
			self.refbonus=2
			self.fortbonus=1
			self.attackbonus=setAttackWhenAttackIsNotEqualsLevel(self.level)
			self.numSkills=5
			self.skills=["Trepar", "Aguante", "Iniciativa", "Saltar", "Conocimiento(Tácticas)", "Conocimiento(Ciencias físicas)", "Conocimiento(Biología)", "Conocimiento(Burocracia)", "Mecánica", "Percepción", "Pilotar", "Nadar", "Supervivencia", "Montar", "Sigilo"]
		if self.name=="Soldado":
			self.refbonus=1
			self.fortbonus=2
			self.attackbonus=setAttackWhenAttackIsEqualsLevel(self.level)
			self.numSkills=3
			self.skills=["Trepar", "Aguante", "Iniciativa", "Saltar", "Conocimiento(Tácticas)", "Mecánica", "Percepción", "Pilotar", "Nadar", "Tratar heridas", "Usar ordenadores"]
