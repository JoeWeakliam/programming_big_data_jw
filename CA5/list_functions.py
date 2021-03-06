#1 Variations on add function

#add all the numbers in a list together using Reduce
def sum(values):
	return reduce(lambda x, y: x+y, values)

print sum([1,2,3,4])

#add the numbers in two lists together to create a new single list using Map
def add(first, second):
	return map(lambda x, y: x+y, first, second)

print add([1,2,3,4], [1,2,3,4])

#2 Subtract function

#subtract the numbers in two lists to create a new list	using Map
def difference(first, second):
	return map(lambda x, y: x-y, first, second)

print difference([1,5,7,2], [3,1,1,3])

#3 Variations on multiply function

#multiply all the numbers together in a list using Reduce 
def product(values):
    return reduce(lambda x, y: x*y, values)

print product([1,2,3,4])

#multiply the numbers in 3 lists to create a new single list using Map
def multiply(first, second, third):
	return map(lambda x, y, z: x*y*z, first, second, third)

print multiply([1,2,3,4], [1,2,3,4], [1,2,3,4])

#4 Variations on the divide function 

#divide the numbers in two lists containing no 0's using Map
def divide(first, second):
    return map(lambda x, y: x/float(y), first, second)

print divide([2,4,6,8], [1,2,3,4])

#divide the numbers in two lists returning 'undefined' for 0 denominators using Map
def divide2(first, second):
    return map(lambda x, y: 'undefined' if (y == 0) else x/float(y), first, second)
		
print divide2([2,4,6,8], [1,3,0,2.5])

#divide the numbers in two lists filtering out 0's in the second list using Filter and then Map
def divide3(first, second):
	second = filter(lambda x: x != 0, second)
	return map(lambda x, y: x/float(y), first, second)

print divide3([2,4,6], [1,2,0,4])

#5 Variations on exponential function

#find exponentials for a list of numbers and exponential values using Map
def expo(values, exponent):
    return map(lambda x, y: x**y, values, exponent) 

print expo([1,2,3,4], [2,4,0,1])

#find exponentials of a list of numbers where a single exponential is applied using List Comprehension
def expo2(values, exponent):
    return [ (x**exponent) for x in values ]

print expo2([1,3,5,7], 3)

#6 Variations on square function

#find the square of a list of numbers removing 0's using Filter and Map
def square(values):
	values = filter(lambda y: y != 0, values)
	return map(lambda x: x*x, values)

print square([2,0,3,4])

#find the square of a list using List Comprehension
def square2(list):
	return [ (x**2) for x in list ]

Squares = [2,3,8,4]
print square2(Squares)

#7 Minimum value 

#find the smallest value in a list using Reduce
def min(values):
	return reduce(lambda a,b: a if (a<b) else b, values)

print min([5,34,5,78,3.5,125])

#8 Use List Comprehension to record all unique dice rolls where the total number is 14

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
dice3 = [1,2,3,4,5,6]
total_14 = [ (x,y,z) for x in dice1 for y in dice2 for z in dice3 if x+y+z == 14]
print total_14

#9 Use Generator Function to return strings in a list that contain a specific substring

def contains(words_list):
    counter = 0
    while counter < len(words_list):
		pos = words_list[counter].find('at')
		if pos != -1:
			yield words_list[counter]
		counter += 1

at_words = contains(['at', 'hat', 'mouse', 'car', 'bat', 'chat', 'cow'])
for at_word in at_words:
    print at_word,
print	

#10a Use Filter to return even values in a list

def is_even(values):
    return filter(lambda x: x%2==0, values)

print is_even([6,8,11,16])

#10b Use List Comprehension to return only those rolls of two dice that generate an even number less than 8

dice1 = [1,2,3,4,5,6]
dice2 = [1,2,3,4,5,6]
even_values = [ (x,y) for x in dice1 for y in dice2 if (x+y)%2 == 0 and (x+y) <= 8 ] 

print even_values
