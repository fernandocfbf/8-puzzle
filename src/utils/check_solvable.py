from src.constants.goal_position import CHECK_SOLVABLE

#CODE SOURCE: https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/
def getInvCount(arr):
	inv_count = 0
	empty_value = -1
	for i in range(0, 9):
		for j in range(i + 1, 9):
			if arr[j] != empty_value and arr[i] != empty_value and CHECK_SOLVABLE[arr[i]] > CHECK_SOLVABLE[arr[j]]:
				inv_count += 1
	return inv_count

def isSolvable(puzzle) :
	inv_count = getInvCount([j for sub in puzzle for j in sub])
	return (inv_count % 2 == 0)