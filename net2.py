def square(x,y):
	'''
	>>> square(2,3)
	6

	'''
	z=x*y
	return z

if __name__ == '__main__':
	import doctest,net2
	doctest.testmod(net2)