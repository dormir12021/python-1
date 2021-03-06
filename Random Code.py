from matplotlib import pyplot as plt
from math import *  # More Math functions (Module)
# ("Hello World!")  # Prints into console whatever is in the string.

name_input = "Ramon"  # Variable, can be changed in the ""
# Seperate the "" from the variable and put spaces so it can be spaced out.
# print("There was an old man named " + name_input + ",")
# print(name_input + " loves to feed his animals in the morning.")
# the + adds the variable to the string
# print(name_input + " also loves being on the road with their huge truck.")

# Three basic types of data
is_male = True
character_age = 16.5
character_name = "Ramon"

# a string
# print("Ramon is cool")
# \n makes a new line to what is on the right
# print("Ramon\nis cool")
# Puts a quation mark so it wont end the string
# print("Ramon\"is cool")
# Puts a backslash
# print("Ramon\is cool")

# String variable
phrase = "Hello Ramon"
# print(phrase + " you are cool!")

phrase = "Hello Ramon"
# (phrase)

# Functions

# makes the string all lowercase.
word = "Python"
# (word.lower())

# makes the string all lowercase.
word = "Python"
# (word.upper())

# checks if the string is uppercase. Then it will give back "True" or "False".
word = "Python"
# (word.isupper())

# Makes it uppercase, then it check if its uppercase giving back a "True"
word = "Python"
# (word.upper().isupper())

# Len = lengh function, tells you how many character there are in the string.
phrase = "Learning Python!"
# (len(phrase))

# Returns P because Python starts with # 0, can change to get other letter.
sentence = "Python is a cool programming language."
# (sentence[0])


# Index function, tells you where a specific string or character is located inside of the string.
sentence = "Knowledge is key to success."
# Parameter:  a value that I would give to a function.
# (sentence.index("K"))
# Output: 0 because that is where K is.

# Also:

people = ["Brandon", "Daniel", "Sebastain"]
# (people.index("Brandon"))

# Replace function
phrase = "Read a book"
# (phrase.replace("book", "article"))  # replaces "book" with "article"


# Numbers and Math

# integers
# (2)

# decimals
(2.838389)

# negative
(-2.38202)

# Addition
(3 + 4)

# Multiplication
(4 * 6)

# Division
(2 / 3)

# Subtraction
(2 - 6)

# Order of Operations
((4 + 7) * 7)

# Mod, divides them both and gets the remainder
(10 % 6)

# Variable = number
number = 10
# (number)

# Output into a string
my_num = 5
# Have to put number into string to add to another string.
# print(str(my_num) + " my favorite number")

# Gets the absolute value
my_num - 5
# (abs(my_num))

# 3^2 basically the first number is the integer, second is power. 3 * 3
# print(pow(3, 2))

# prints out the largest number
# print(max(4, 20))

# prints out the smallest number
# print(min(4, 69))

# rounds the decimal.
# (round(5.7))


# import the math module


# Grabs the lowest number so its going to take off the decimal
# (floor(5.7))

# Round the number up no matter what
# (ceil(5.2))

# Square root of a number
# (sqrt(50))

# User Input, you can get many user inputs.
# user_input = input("Enter your name: ")
# print("Hello " + user_input + ".")

# Getting integers and adding them together
# number = input("Enter a number: ")
# number2 = input("Enter a second number: ")
# total = int(number) + int(number2)
# (total)

# Getting decimals and adding them together
# number = input("Enter a number: ")
# number2 = input("Enter a second number: ")
# total = float(number) + float(number2)
# (total)

# User input in setences!
# color = input("Enter your favorite color: ")
# name = input("Enter a persons name: ")
# icecream_flavor = input("Enter your favorite icecream flavor: ")

# print("The sky is " + color + "!")
# print("Hello " + name + " how are you today?")
# print("My favorite iceream flavor is " + icecream_flavor + "!")

# Lists
people = ["Hank", "John", "Sho", "James"]
#         0        1      2        3
# (people[0])
# prints from right to left (back of the list)
# (people[-1])
# Grabs the element at index position 1 and everything to the right of it
# (people[1:])
# Or can do it from a range
# (people[1:2])

# Updates the index postion to whats in the string. (Modify value in array)
people = ["James", "Charles", "Ramon"]
people[1] = "Mike"
# (friends[1])

# Using functions in list

# Takes a list and appends another list into the end.
cool_numbers = [5, 10, 15, 20, 25, 30, 25]
people = ["Kim", "Jim", "The Rock"]
people.extend(cool_numbers)
# (people)

# Adds an individual element to at the end of the list
people = ["Kim", "Jim", "The Rock"]
people.append("Rommel")
# (people)

# At position one it will now have what you want to insert moving others to right
people = ["Trevor", "Oscar", "Karen"]
people.insert(1, "Phil")
# (people)

# Removes the element from the list
people = ["Trevor", "Oscar", "Karen"]
people.remove("Oscar")
# (people)

# removes all the elements from the list, gives you an empthy list.
people = ["Kyle", "Micheal", "John"]
people.clear()
# (people)

# "pops"(removes) the last element from the list
people = ["Xavier", "Robert", "Smith"]
people.pop()
# (people)

# amount of times that element was found in the list so it would be 2.
people = ["Jim", "Jim", "Micheal"]
# (people.count("Jim"))

# Will put the list in alaphbeltical order, puts numbers from lowest to highest.
items = ["Crown", "Sword", "Sheild"]
items.sort()
# (items)

# puts the list in reverse
random_numbers = [1, 28, 2893, 219, 2, 189]
random_numbers.reverse()
# (random_numbers)

# Copys the list from the first list
num_list = [92, 83, 92, 783, 2]
num_list2 = num_list.copy()
# (num_list2)

# Tupel

# You can't change a tuples! Tuples are unchangeable!
coordinates = (3, 7, 9)
# (coordinates[0])

# Functions


# def say_hello():  # has to start with def
# print("Hello!")  # has to be indented

# say_hello()  # calls function


# def say_hello():
# print("Hello!")
# say_hello()

# Ternary Conditionals
# Slower way
condition = True

if condition:
    x = 1
else:
    x = 0

# print(x)

# Faster way
condition = True

x = 1 if condition else 0

# print(x)

# Underscore Placeholders

num1 = 9_292_938_373_374
num2 = 38_641_230_896_094  # you can add underscores between the numbers

total = num1 + num2
# print(f'{total:,}')

# Context Managers
txt = "First module: {}".format(__name__)
# print(txt)


# Stackoverflow developer survey

# Deluxe Package
dev_x = [1, 2, 3, 4, 5, 6, 7]
dev_y = [1, 3, 6, 7, 8, 20, 45]

# Starter
main_dev_x = [1, 2, 3, 4, 5, 6, 7]
main_dev_y = [3, 7, 15, 27, 30, 45, 67]

plt.plot(dev_x, dev_y, label='Deluxe Pack')  # the method to plot
plt.plot(main_dev_x, main_dev_y, label='Starter pack')
plt.xlabel('Day')  # x ais labeled
plt.ylabel('Units sold')  # y ais labeled
plt.title('Products Sold in a Week [Fake Data]')  # title

# plt.legend(['Dount', 'Cake'])
plt.legend()

plt.show()  # shows the data
