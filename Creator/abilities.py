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
