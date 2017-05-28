import sys
import math

def f(x):
	return (5+3.592/x**2)*(x-0.04267)-(0.082054*300)
	
def secant(x0,x1,n):
	for i in range(n):
		if f(x1)-f(x0) == 0:
			return x1
		x_temp = x1 - (f(x1)*(x1-x0)*1.0)/(f(x1)-f(x0))
		x0 = x1
		x1 = x_temp
		print i,     x0,       x1,       f(x1)
	
def main(argv):
	if (len(sys.argv) != 4):
		sys.exit('Usage: secant_method.py <x0> <x1> <n>')
	
	print 'The root is: \n',
	print secant(float(sys.argv[1]),float(sys.argv[2]),int(sys.argv[3]))

if __name__ == "__main__":
	main(sys.argv[1:])
		


