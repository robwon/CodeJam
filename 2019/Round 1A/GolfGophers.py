import sys
import math
import numpy

# Uses Chinese remainder theorem to find the congruence class of the integer whose
# remainders mod the moduli are given in the two lists.
# The entries of moduli must be pairwise coprime.
def solve(remainders, moduli):
	N = 4 * 3 * 5 * 7 * 11 * 13 * 17
	sum = 0
	for i in range(0, len(remainders)):
		sum += (N // moduli[i]) * findInverse(N // moduli[i], moduli[i]) * remainders[i]
		sum = sum % N
	return sum

def findInverse(element, modulus):
	if math.gcd(element, modulus) != 1:
		raise ValueError('Not invertible')
	totient = 0
	for i in range(1, modulus):
		if math.gcd(i, modulus) == 1:
			totient += 1
	current = element % modulus
	for i in range(1, totient - 1):
		current = (current * element) % modulus
	return current

def main(argv):
	[T, N, M] = [int(x) for x in input().split()]
	for case in range(1, T+1):
		moduli = [4, 3, 5, 7, 11, 13, 17]
		remainders = []
		for mod in moduli:
			output = " ".join([str(mod)]*18)
			print(output)
			sys.stdout.flush()
			ans = input()
			gophers = [int(x) for x in ans.split()]
			remainders.append(sum(gophers) % mod)
		print(solve(remainders, moduli))
		sys.stdout.flush()
		verdict = int(input())
		if verdict != 1:
			raise ValueError(remainders, moduli)

if __name__ == "__main__":
	main(sys.argv)

## To debug, use raise ValueError(dataIWant)