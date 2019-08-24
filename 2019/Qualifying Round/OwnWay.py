import sys
import math
import numpy

def solve(inputPath):
	answer = ''
	for i in inputPath:
		if i == 'E':
			answer += 'S'
		else:
			answer += 'E'
	return answer

def main(argv):
	t = int(input())
	for i in range(1, t + 1):
		n = input()
		path = input()
		print("Case #{}: {}".format(i,solve(path)))

if __name__ == "__main__":
	main(sys.argv)