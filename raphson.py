def derivative(f, x, h):
      return (f(x+h) - f(x-h)) / (2.0*h) 

def quadratic(x):
	return (5+3.592/x**2)*(x-0.04267)-(0.082054*300)

def solve(f, x0, h):
    i=0
    lastX = x0
    nextX = lastX + 10* h  
    while (abs(lastX - nextX) > h):  
        newY = f(nextX)                     
        print  i, lastX, nextX, newY ,h    
        lastX = nextX
        nextX = lastX - newY / derivative(f, lastX, h) 
	i=i+1
    return nextX

xFound = solve(quadratic, 0, 0.001)   
print "solution: x = ", xFound  
