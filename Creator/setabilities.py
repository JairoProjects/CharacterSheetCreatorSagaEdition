from random import randint

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
