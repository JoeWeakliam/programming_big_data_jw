"""
App to run our calculator programme
"""

#import all the methods from the Calculator class
from calculator import Calculator

#create an instance of the Calculator class
myCalculator = Calculator()

#keep prompting the user to enter their choice of operator
while True:
    
    choice = raw_input("Enter operator you would like to run or 'Done' to exit the programme: ")
    
    #allow the user to exit the programme
    if choice.lower() == 'done':
        print 'Exiting program...'
        break
    
    elif choice.lower() == 'add':
        value1 = float(raw_input('Enter first operand: '))
        value2 = float(raw_input('Enter second operand: '))
        result = myCalculator.add(value1,value2) #assign result to variable result 
        
    elif choice.lower() == 'subtract':
        value1 = float(raw_input('Enter first operand: '))
        value2 = float(raw_input('Enter second operand: '))
        result = myCalculator.subtract(value1,value2)
        
    elif choice.lower() == 'multiply':
        value1 = float(raw_input('Enter first operand: '))
        value2 = float(raw_input('Enter second operand: '))
        result = myCalculator.multiply(value1,value2)
        
    elif choice.lower() == 'divide':
        value1 = float(raw_input('Enter first operand: '))
        value2 = float(raw_input('Enter second operand: '))
        result = myCalculator.divide(value1,value2)
    
    elif choice.lower() == 'exponent':
        value1 = int(raw_input('Enter number: '))
        value2 = int(raw_input('Enter exponent: '))
        result = myCalculator.expo(value1,value2)
    
    elif choice.lower() == 'square root':
        value = float(raw_input('Enter number: '))
        result = myCalculator.square_root(value)
    
    elif choice.lower() == 'square':
        value = float(raw_input('Enter number: '))
        result = myCalculator.square(value)
    
    elif choice.lower() == 'cube':
        value = float(raw_input('Enter number: '))
        result = myCalculator.cube(value)
    
    elif choice.lower() == 'sine':
        value = int(raw_input('Enter number: '))
        result = myCalculator.sine(value)
    
    elif choice.lower() == 'cosine':
        value = int(raw_input('Enter number: '))
        result = myCalculator.cosine(value)
    
    elif choice.lower() == 'tangent':
        value = int(raw_input('Enter number: '))
        result = myCalculator.tangent(value)
    
    #catch invalid input
    else:
        print 'Invalid operator selected. Please try again.'
    
    #print the result to the console and prompt the user to go again
    print 'The result of your calculation is {}'.format(result)
                                        
          
                




