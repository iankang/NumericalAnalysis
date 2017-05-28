import sys
import math

def func(x):
	return -139.34411+((1.575701*10**5)/x)-((6.642308*10**7)/x**2)+((1.243800*10**10)/x**3)-((8.621949*10**11)/x**4)-math.log(8)

def regula_falsi( a, b, max_steps, tolerance):
    p = 0.0
    for loopCount in range(max_steps):
        p = b - (func(b) * ((a-b)/(func(a)-func(b))))
        print "Current approximation is %.9f" % p
        if math.copysign(func(a), func(b)) != func(a):
            b = p
        else:
            a = p
        if abs(func(p)) < tolerance:
            print "Root is %.9f (%d iterations)" % (p,int(loopCount))
            return
    print "Root find cancelled at %.9f" % p

def main(argv):
	if (len(sys.argv) != 5):
		sys.exit('Usage: regula-falsi.py <a> <b> <tol>')
	
	print 'The root is: \n',
	print regula_falsi(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),float(sys.argv[4]))

if __name__ == '__main__':
    main(sys.argv[1:])
