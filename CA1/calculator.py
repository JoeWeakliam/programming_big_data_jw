"""
This class contains definitions of the various functions to be included in our calculator programme
"""
#import relevant in-built math functions
import math

#create the Calculator class
class Calculator(object):
    
    #create the init function which is empty to begin with
    def __init__(self):
        pass

    #add two numbers together
    def add(self,first,second): 
        return first + second
        
    #subtract two numbers
    def subtract(self,first,second):
        return first - second

    #multply two numbers
    def multiply(self,first,second):
        return first * second

    #divide two numbers
    def divide(self,first,second):
        if second == 0:
            return 'undefined'
        else:
            return first / float(second)

    #find particular exponential of a number
    def expo(self,number,exponent):
        if exponent == 0:
            return 1
        else:
            return number ** exponent

    #find the square root of a number 
    def square_root(self,number):
        if number <= 0:
            return 'undefined'
        else:
            return number ** (0.5) 
            #return math.sqrt(number)

    #find the square of a number - also handles negative numbers
    def square(self,number):
        return number * number

    #find the cube of a number - also handles negative numbers
    def cube(self,number):
        return (number * number) * number

    #find the sine of a number
    def sine(self,number):
        return round(math.sin(number))
                
    #find the cosine of a number
    def cosine(self,number):
        return round(math.cos(number))

    #find the tangent of a number
    def tangent(self,number):
        return round(math.tan(number))

    #find the sine of a right-angled triangle given lengths of 2 relevant sides
    def sine1(self,opposite,hypoteneuse):
        if opposite <= 0 or hypoteneuse <= 0:
            return 'undefined'
        else: 
            return opposite / float(hypoteneuse)
 
    #find the cosine of a right-angled triangle given lengths of 2 relevant sides
    def cosine1(self,adjacent,hypoteneuse):
        if adjacent <= 0 or hypoteneuse <= 0:
            return 'undefined'
        else:
            return adjacent / float(hypoteneuse)

    #find the tangent of a right-angled triangle given lengths of 2 relevant sides
    def tangent1(self,opposite,adjacent):
        if opposite <= 0 or adjacent <= 0:
            return 'undefined'
        else:
            return opposite / float(adjacent)
    
    
    
    
    
    
    
    


