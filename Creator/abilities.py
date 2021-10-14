from random import randint

class Stat():
	def __init__(self, name, value):
		self.name=name
		self.value=value

class Ability(Stat):
	def __init__(self):
		super().__init__()
		self.modifier=0

	def setModifier(self):
		if self.value>=10:
			self.modifier=(self.value-10)//2
		else:
			setModifierWhenValueIsLessThanTen()

	def setModifierWhenValueIsLessThanTen(self):
		if self.value%2==1:
			self.modifier=10-self.value
		if self.value%2==0:
			self.modifier=(10-(self.value+1)

def rollingDices():
	results=[]
	for x in range(4):
		dice=randint(1, 6)
		results.append(dice)
	return results

def deleteTheSmallestResult():
	results=rollingDices()
	results.remove(min(results))
	return results

def sumTheDices():
	dices=deleteTheSmallestResult()
	total=sum(dices)
	return total
