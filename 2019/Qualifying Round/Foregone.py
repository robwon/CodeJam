import sys
import math
import numpy


def solve(input):
	myString = str(input)
	answerString = ''
	for i in myString:
		if i == '4':
			answerString = answerString + '1'
		else:
			answerString = answerString + '0'
	answer1 = int(answerString)
	return answer1

def main(argv):
	t = int(input())  # read a line with a single integer
	for i in range(1, t + 1):
		n = input()
		print("Case #{}: {} {}".format(i,solve(n),int(n) - solve(n)))
  		# n = input().split(" ")  # read a list of integers, 2 in this case
  		#print("Case #{}: {}".format(i, n))

if __name__ == "__main__":
	main(sys.argv)