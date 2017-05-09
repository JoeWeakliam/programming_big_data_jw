#add two numbers together
add <- function(first, second) {
  return (first + second)
}
add(3, 4)
add(-45, -6)

#subtract two numbers
subtract <- function(first, second) {
  return (first - second)
}
subtract(5, 6)
subtract(-19, -4)

#multply two numbers
multiply <- function(first, second) {
  return (first * second)
}
multiply(10, 4)
multiply(8.2, 6)
multiply(7, 0)

#divide two numbers
divide <- function(first, second) {
  if (second == 0) {
  return ('undefined')
  } else {
  return (first / second)
  }
}
divide(12, 4)
divide(16, 5)
divide(9, 0)

#find particular exponential of a number
expo <- function(number, exponent) {
  if (exponent == 0) {
    return (1)
  } else {
    return (number ** exponent)
  }
}
expo(3, 2)
expo(8, 0)
expo(-4, 2)

#find the square root of a number 
square_root <- function(number) {
  if (number <= 0) {
    return ('undefined')
  } else {
    return (number ** 0.5)
  }
}
square_root(49)
square_root(-5)
square_root(7.8)

#find the square of a number - also handles negative numbers
square <- function(number) {
  return (number * number)
}
square(4.4)
square(-3.4)
square(0)

#find the cube of a number - also handles negative numbers
cube <- function(number) {
  return ((number * number) * number)
}
cube(4)
cube(-5)
cube(2.5)

#find the sine of a number
sine <- function(number) {
  return (sin(number))
}
sine(90)
sine(45)
sine(1)

#find the cosine of a number
cosine <- function(number) {
  return (cos(number))
}
cosine(90)
cosine(45)
cosine(1)

#find the tangent of a number
tangent <- function(number) {
  return (tan(number))
}
tangent(90)
tangent(45)
tangent(1)
  
  