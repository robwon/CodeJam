import sys
import math
import numpy
from string import ascii_uppercase

def solve(upperbound, numWords, cipher):
	answer = ''
	primeText = []
	primeList = set({})
	primeDictionary = {}
	i = 0
	while math.gcd(cipher[i], cipher[i+1]) == cipher[i]:
		i += 1
	currPrime = math.gcd(cipher[i], cipher[i+1])
	primeList.add(currPrime)
	primeText.append(currPrime)
	for j in range(i + 1, numWords):
		nextPrime = cipher[j] // currPrime
		primeList.add(nextPrime)
		primeText.append(nextPrime)
		currPrime = nextPrime
	currPrime = math.gcd(cipher[i], cipher[i+1])
	for j in range(i, -1, -1):
		prevPrime= cipher[j] // currPrime
		primeList.add(prevPrime)
		primeText.insert(0, prevPrime)
		currPrime = prevPrime

	sortedPrimes = sorted(primeList)
	i = 0
	for lett in ascii_uppercase:
		primeDictionary.update({sortedPrimes[i] : lett})
		i += 1
	for x in primeText:
		answer = answer + primeDictionary[x]
	return answer


def main(argv):
	t = int(input())
	for i in range(1, t + 1):
		upperbound, numWords = [int(s) for s in input().split(" ")]
		cipher = [int(s) for s in input().split(" ")]
		print("Case #{}: {}".format(i,solve(upperbound, numWords, cipher)))

if __name__ == "__main__":
	main(sys.argv)