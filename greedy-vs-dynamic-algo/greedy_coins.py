#coin problem solved with greedy algorithm

def getChange(coins,change,changeList):
	if change in coins:
		changeList.append(change)
		print(changeList)
	else:
		if change >= coins[0]:
			changeList.append(coins[0])
			change = change - coins[0]
			getChange(coins,change,changeList)
		elif change >= coins[1]:
			changeList.append(coins[1])
			change = change - coins[1]
			getChange(coins,change,changeList)
		elif change >= coins[2]:
			changeList.append(coins[2])
			change = change - coins[2]
			getChange(coins,change,changeList)
		elif change > coins[3]:
			changeList.append(coins[3])
			change = change - coins[3]
			getChange(coins,change,changeList)

def main():
	coins = [25,10,5,1]

	change = 146

	changeList = []

	getChange(coins,change,changeList)
main()
