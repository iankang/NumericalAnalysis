import sys
import math

def f(x):
	return 1-x*math.tan(x)
	
def bisection(a,b,tol):
	i=0
	c = (a+b)/2.0
	while (b-a)/2.0 > tol:
		if f(c) == 0:
			return c
		elif f(a)*f(c) < 0:
			b = c
		else :
			a = c
		c = (a+b)/2.0
		i=i+1
		print i,a,b,c,tol
	print c	
	
def main(argv):
	if (len(sys.argv) != 4):
		sys.exit('Usage: bisection.py <a> <b> <tol>')
	
	print 'The root is: \n',
	print bisection(int(sys.argv[1]),int(sys.argv[2]),float(sys.argv[3]))

if __name__ == "__main__":
	main(sys.argv[1:])
