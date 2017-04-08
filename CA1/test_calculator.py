"""
This class is used to test all our calculator functions 
"""

#import all the caluclator methods
from calculator import *

#set up test environment 
import unittest

#create an instance of the Calculator class
myCalculator = Calculator()

class MyTest(unittest.TestCase):
    
    #test to verify 2 + 2 = 4, 5 + 3 = 8, 4 + 0 = 4
    def testAdd(self):
        self.assertEqual(myCalculator.add(2,2), 4)
        self.assertEqual(myCalculator.add(5,3), 8)
        self.assertEqual(myCalculator.add(4,0), 4)
        
    #test to verify 2 - 2 = 0, 5 - 3 = 2, 4 - 0 = 4, 3 - 4 = -1
    def testSubtract(self):
        self.assertEqual(myCalculator.subtract(2,2), 0)
        self.assertEqual(myCalculator.subtract(5,3), 2)
        self.assertEqual(myCalculator.subtract(4,0), 4)
        self.assertEqual(myCalculator.subtract(3,4), -1)

    #test to verify 2 * 2 = 4, 5 * 3 = 15, 4 * 0 = 0, 3 * -4 = 12
    def testMultiply(self):
        self.assertEqual(myCalculator.multiply(2,2), 4)
        self.assertEqual(myCalculator.multiply(5,3), 15)
        self.assertEqual(myCalculator.multiply(4,0), 0)
        self.assertEqual(myCalculator.multiply(3,-4), -12)
    
    #test to verify 2 / 2 = 1.0, 5 / 3 = 1.25, 4 / 1 = 4, 4 / 0 = undefined
    def testDivide(self):
        self.assertEqual(myCalculator.divide(2,2), 1.0)
        self.assertEqual(myCalculator.divide(5,4), 1.25)
        self.assertEqual(myCalculator.divide(4,1), 4)
        self.assertEqual(myCalculator.divide(4,0), 'undefined')
    
    #test to verify 2 ** 2 = 4, 5 ** 3 = 125, 4 ** 0 = 1, 3 ** 4 = 81
    def testExpo(self):
        self.assertEqual(myCalculator.expo(2,2), 4)
        self.assertEqual(myCalculator.expo(5,3), 125)
        self.assertEqual(myCalculator.expo(4,0), 1)
        self.assertEqual(myCalculator.expo(3, 4), 81)
    
    #test to verify sqrt 4 = 2, sqrt 9 = 3.0, sqrt 1 = 1, sqrt -4 = undefined 
    def testSqrt(self):
        self.assertEqual(myCalculator.square_root(4), 2)
        self.assertEqual(myCalculator.square_root(9), 3.0)
        self.assertEqual(myCalculator.square_root(1), 1)
        self.assertEqual(myCalculator.square_root(-4), 'undefined')
    
    #test to verify 4 * 4 = 16, 2 * 2 = 4, 1.2 * 1.2 = 1.44, -3 * -3 = 9
    def testSquare(self):
        self.assertEqual(myCalculator.square(4), 16)
        self.assertEqual(myCalculator.square(2), 4)
        self.assertEqual(myCalculator.square(1.2), 1.44)
        self.assertEqual(myCalculator.square(-3.0), 9.0)
        
    #test to verify (4 * 4 * 4) = 64, (-5 * -5 * -5) = -125, (2.1 * 2.1 * 2.1) = 9.261000000000001
    def testCube(self):
        self.assertEqual(myCalculator.cube(4), 64)
        self.assertEqual(myCalculator.cube(-5), -125)
        self.assertEqual(myCalculator.cube(2.1), 9.261000000000001)
    
    #test to verify sine 90 = 1.0, sine 30 = -1, sine 0 = 0.0
    def testSine(self):
        self.assertEqual(myCalculator.sine(90), 1.0)
        self.assertEqual(myCalculator.sine(30), -1.0)
        self.assertEqual(myCalculator.sine(0), 0.0)
    
    #test to verify cosine 60 = -1.0, cosine 30 = -0, cosine 0 = 1.0
    def testCosine(self):
        self.assertEqual(myCalculator.cosine(60), -1.0)
        self.assertEqual(myCalculator.cosine(30), -0)
        self.assertEqual(myCalculator.cosine(0), 1.0)
    
    #test to verify tangent 90 = -2.0, tangent 60 = 0.0, tangent 30 = -6.0
    def testTangent(self):
        self.assertEqual(myCalculator.tangent(90), -2.0)
        self.assertEqual(myCalculator.tangent(60), 0.0)
        self.assertEqual(myCalculator.tangent(30), -6.0)
        
    
    #test to verify sine(2,4) = 0.5, sine(1,2.5) = 0.4, sine(2.8,4.9) = 0.5714285714285714
    '''def testSine1(self):
        self.assertEqual(sine(2,4), 0.5)
        self.assertEqual(sine(1,2.5), 0.4)
        self.assertEqual(sine(2.8, 4.9), 0.5714285714285714)
    
    #test to verify cosine(2,4) = 0.5, cosine(1.2,2.5) = 0.48, cosine(4.0,4.9) = 0.8163265306122448
    def testCosine1(self):
        self.assertEqual(cosine(2,4), 0.5)
        self.assertEqual(cosine(1.2,2.5), 0.48)
        self.assertEqual(sine(4.0, 4.9), 0.8163265306122448)
                
    #test to verify tangent(2,4) = 0.5, tangent(1.2,2.5) = 0.48, tangent(2.8,4.0) = 0.70
    def testTangent1(self):
        self.assertEqual(tangent(2,4), 0.5)
        self.assertEqual(tangent(1.2,2.5), 0.48)
        self.assertEqual(tangent(2.8,4.0), 0.70)'''
    
#run the test program
if __name__ == '__main__':
    unittest.main()
    
    