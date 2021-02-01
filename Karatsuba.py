#Karatsuba Algorithm
#CIIC4025
#Peter Leroy Santana Rodriguez
import math

def karatsuba(x,y):
	lx = len(str(x))
	ly = len(str(y))


	if (lx and ly) == 1:
		return x * y
	
	else:
		n = max(lx, ly)
		power = math.floor(n/2)
		ex = 10 ** power


	a = (x // ex)
	b = math.floor(x % ex)
	c = (y // ex)
	d = math.floor(y % ex)

	ac = karatsuba(a,c)
	bd = karatsuba(b,d)
	middle = karatsuba(a+b, c+d) - ac - bd

	return (ac * 10 **(2*power)) + (middle * ex) + bd



