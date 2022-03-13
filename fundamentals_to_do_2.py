# 1. Countdown
# Create a function that accepts a number as an input. 
# Return a new array that counts down by one, from the number (as array’s ‘zeroth’ element) down to 0 (as the last element). 
# How long is this array?

# create a function that accepts a number
# return a new array that counts down by one from the number (value at index 0) down to 0 (last value in array)
#give length of array

# def countdown (number):
#     newArray = []
#     for i in range(number,-1, -1):
#         newArray.append(i)
#     print(len(newArray))
#     return newArray
# print (countdown(5))


# 2. First Plus Length
# Given an array, return the sum of the first value in the array, plus the array’s length. 
# What happens if the array’s first value is not a number, but a string (like "what?") or a boolean (like false).

# write a function that accepts an array
# return the sum of the first value in the array plus the array's length

# def first_plus_length(array):
#     return array[0] + len(array)
# print(first_plus_length([4,8,5,3]))

# 3. Values Greater than Second
# For [1,3,5,7,9,13], print values that are greater than its 2nd value. Return how many values this is.

# def greater_than_second(array):
#     output = []
#     for i in range(0,len(array)):
#         if array[i] > array [1]:
#             output.append(array[i])
#     print(len(output))
#     return output
# print(greater_than_second([5,2,3,2,1,4]))

#another way where we print the values NOT as a new array

# def greater_than_second(array):
#     count = 0
#     for i in array:
#         if i > array[1]:
#             print (i)
#             count = count + 1
#     return count
# print(greater_than_second([5,2,3,2,1,4]))


# 4. Values Greater than Second, Generalized
# Write a function that accepts any array, and returns a new array with the array values that are greater than its 2nd value. 
# Print how many values this is. What will you do if the array is only one element long?

# 5. This Length, That Value
# Given two numbers, return array of length num1 with each value num2. Print "Jinx!" if they are same.

#write a function that takes 2 numbers
# we need the length of num1 
#return an array with length of num1 with each value num2
#print "Jinx" if they are the same

# 6. Fit the First Value
# Your function should accept an array. 
# If value at [0] is greater than array’s length, print "Too big!"; if value at [0] is less than array’s length, print "Too small!"; otherwise print "Just right!".

#write a function that accepts an array
# determine value at [0]
#determine length of array
#if value at [0] is greater than length print "Too big"
# if value at [0] is smaller than length print "Too small" otherwise print "Just right"

# def fit_the_first_value(array):
#     if array[0] > len(array):
#         print("Too big")
#     elif array[0] < len(array):
#         print("Too small")
#     else:
#         print("Just right")
# print(fit_the_first_value([3,5,2,6]))

# 7. Fahrenheit to Celsius
# Kelvin wants to convert between temperature scales. 
# Create fahrenheitToCelsius(fDegrees) that accepts a number of degrees in Fahrenheit and returns the equivalent temperature as expressed in Celsius degrees. 
# For review, Fahrenheit = (9/5 * Celsius) + 32.

# create a function that accepts a number of degress in Fahrenheit
# return the equivalent temp in Celcius

def fahrenheittoCelsius(fDegrees):
    celsius = (fDegrees - 32) * (5/9)
    return celsius
print(fahrenheittoCelsius(40))