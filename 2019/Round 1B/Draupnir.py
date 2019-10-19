import sys
import math
import numpy


def solve(bigAns, smallAns):
	R6 = (bigAns % (2**44))//(2**36)
	R5 = (bigAns % (2**55) - R6 * (2**36)) // (2**44)
	R4 = (bigAns - R5 * (2**44) - R6 * (2**36))// (2**55)
	smallAns = smallAns - R4*(2**13) -R5*(2**10) - R6*(2**8)
	R3 = (smallAns % (2**26))//(2**17)
	R2 = (smallAns % (2**53) - R3 * (2**17)) // (2**26)
	R1 = (smallAns - R2 * (2**26) - R3 * (2**17))// (2**53)
	return (R1, R2, R3, R4, R5, R6)
	

def main(argv):
	[T,W] = [int(x) for x in input().split()]
	for case in range(1, T+1):
		print(221)
		sys.stdout.flush()
		bigAns = int(input())
		print(53)
		sys.stdout.flush()
		smallAns = int(input())
		[R1, R2, R3, R4, R5, R6] = solve(bigAns, smallAns)
		#raise ValueError("{} {} {} {} {} {}".format(R1, R2, R3, R4, R5, R6))
		print("{} {} {} {} {} {}".format(R1, R2, R3, R4, R5, R6))
		sys.stdout.flush()
		verdict = int(input())
		if verdict != 1:
			raise ValueError(R1, R2, R3, R4, R5, R6)

if __name__ == "__main__":
	main(sys.argv)


## To debug, use raise ValueError(dataIWant)