import net2,unittest

class ProductTestCase(unittest.TestCase):
	"""docstring for Productestcase"""

	def testInt(self):
		for x in xrange(-10,10):
			for y in xrange(-10,10):
				p=net2.square(x,y)
				self.failUnless(p==x*y,'Int failed')

if __name__ == '__main__':
	unittest.main()
