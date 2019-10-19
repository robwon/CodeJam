import sys
# import math
# import numpy
# bisect
# heapqueue
# collections


def solve(listOfPeople, Q):
	xCoords = [0] * (Q+1)
	yCoords = [0] * (Q+1)
	northBound = [0] * (Q+1)
	southBound = [0] * (Q+1)
	eastBound = [0] * (Q+1)
	westBound = [0] * (Q+1)
	xCoordsE = [0] * (Q+1)
	xCoordsW = [0] * (Q+1)
	yCoordsN = [0]*(Q+1)
	yCoordsS = [0]*(Q+1)
	for person in listOfPeople:
		if person[2] == 'N':
			northBound[person[1]] += 1
		if person[2] == 'S':
			southBound[person[1]] += 1
		if person[2] == 'E':
			eastBound[person[0]] += 1
		if person[2] == 'W':
			westBound[person[0]] += 1
	for i in range(1, Q+1):
		yCoordsN[i] += yCoordsN[i-1] + northBound[i-1]
		xCoordsE[i] += xCoordsE[i-1] + eastBound[i-1]
	for i in range(1,Q+1):
		yCoordsS[Q-i] += yCoordsS[Q- i + 1] + southBound[Q - i + 1]
		xCoordsW[Q-i] += xCoordsW[Q-i+1] + westBound[Q - i + 1]
	for i in range(0, Q+1):
		xCoords[i] = xCoordsE[i] + xCoordsW[i]
		yCoords[i] = yCoordsN[i] + yCoordsS[i]
	return(xCoords.index(max(xCoords)), yCoords.index(max(yCoords)))

def main(argv):
	T = int(input())
	for i in range(0, T):
		myPeople = []
		P,Q = [int(s) for s in input().split(" ")]
		for j in range(0, P):
			temp = input().split(" ")
			myPeople.append([int(temp[0]), int(temp[1]), temp[2]])
		x, y = solve(myPeople, Q)
		print("Case #{}: {} {}".format(i+1, x, y))
		


if __name__ == "__main__":
	main(sys.argv)