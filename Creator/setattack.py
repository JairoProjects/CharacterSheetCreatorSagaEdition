def setAttackWhenAttackIsEqualsLevel(level):
	attack=level
	return attack

def setAttackWhenAttackIsNotEqualsLevel(level):
	if level>=0 and level<=4:
		attack=level-1
	if level>=5 and level<=8:
		attack=level-2
	if level>=9 and level<=12:
		attack=level-3
	if level>=13 and level<=16:
		attack=level-4
	if level>=17 and level<=20:
		attack=level-5
	return attack
