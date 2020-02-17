#Not finished I still need to write down  functions, while loops.. etc. 

print("Hello World!") #Prints into console whatever is in the string.

name_input = "Ramon" #Variable, can be changed in the ""
print("There was an old man named " + name_input + ",") #Seperate the "" from the variable and put spaces so it can be spaced out. 
print(name_input + " loves to feed his animals in the morning.")
print(name_input + " also loves being on the road with their huge truck.") #the + adds the variable to the string

#Three basic types of data 
is_male = True
character_age = 16.5
character_name = "Ramon"

# a string 
print("Ramon is cool") 
#\n makes a new line to what is on the right 
print("Ramon\nis cool")
#Puts a quation mark so it wont end the string
print("Ramon\"is cool") 
#Puts a backslash
print("Ramon\is cool") 

#String variable
phrase = "Hello Ramon"
print(phrase + " you are cool!")

phrase = "Hello Ramon"
print(phrase)

#Functions 

#makes the string all lowercase.
word = "Python"
print(word.lower())

#makes the string all lowercase.
word = "Python"
print(word.upper())

#checks if the string is uppercase. Then it will give back "True" or "False". 
word = "Python"
print(word.isupper())

#Makes it uppercase, then it check if its uppercase giving back a "True" 
word = "Python"
print(word.upper().isupper())

#Len = lengh function, tells you how many character there are in the string. 
phrase = "Learning Python!"
print(len(phrase))

#Returns P because Python starts with #0, can change to get other letter.
sentence = "Python is a cool programming language."
print(sentence[0])


#Index function, tells you where a specific string or character is located inside of the string.
sentence = "Knowledge is key to success."
print(sentence.index("K")) #Parameter:  a value that I would give to a function. 
#Output: 0 because that is where K is. 

#Also:

people = ["Brandon", "Daniel", "Sebastain"]
print(people.index("Brandon"))

#Replace function
phrase = "Read a book"
print(phrase.replace("book", "article")) #replaces "book" with "article"


#Numbers and Math

#integers
print(2)

#decimals
(2.838389)

#negative
(-2.38202)

#Addition
(3 + 4)

#Multiplication 
(4 * 6)

#Division
(2 / 3)

#Subtraction
(2 - 6)

#Order of Operations 
((4 + 7) * 7) 

#Mod, divides them both and gets the remainder
(10 % 6)

#Variable = number  
number = 10
print(number)

#Output into a string 
my_num = 5
print(str(my_num) + " my favorite number") #Have to put number into string to add to another string.

#Gets the absolute value
my_num -5 
print(abs(my_num))

#3^2 basically the first number is the integer, second is power. 3 * 3
print(pow(3, 2))

#prints out the largest number
print(max(4, 20))

#prints out the smallest number
print(min(4, 69))

#rounds the decimal. 
print(round(5.7))

from math import * #More Math functions (Module)

#Grabs the lowest number so its going to take off the decimal
print(floor(5.7))

#Round the number up no matter what 
print(ceil(5.2))

#Square root of a number
print(sqrt(50))

#User Input, you can get many user inputs. 
user_input = input("Enter your name: ")
print("Hello " + user_input + ".")

#Getting integers and adding them together
number = input("Enter a number: ")
number2 = input("Enter a second number: ")
total = int(number) + int(number2)
print(total)

#Getting decimals and adding them together
number = input("Enter a number: ")
number2 = input("Enter a second number: ")
total = float(number) + float(number2)
print(total)

#User input in setences! 
color = input("Enter your favorite color: ")
name = input("Enter a persons name: ")
icecream_flavor = input("Enter your favorite icecream flavor: ")

print("The sky is " + color + "!")
print("Hello " + name + " how are you today?")
print("My favorite iceream flavor is " + icecream_flavor + "!")

#Lists 
people = ["Hank", "John", "Sho", "James"]
 #           0        1      2        3
print(people[0])
#prints from right to left (back of the list)
print(people[-1])
#Grabs the element at index position 1 and everything to the right of it 
print(people[1:])
#Or can do it from a range
print(people[1:2])

#Updates the index postion to whats in the string. (Modify value in array)
people = ["James", "Charles", "Ramon"]
people[1] = "Mike"
print(friends[1])

#Using functions in list 

#Takes a list and appends another list into the end.
cool_numbers = [5, 10, 15, 20, 25, 30, 25]
people = ["Kim", "Jim", "The Rock"]
people.extend(cool_numbers)
print(people)

#Adds an individual element to at the end of the list
people = ["Kim", "Jim", "The Rock"]
people.append("Rommel")
print(people)

#At position one it will now have what you want to insert moving others to right 
people = ["Trevor", "Oscar", "Karen"]
people.insert(1, "Phil")
print(people)

#Removes the element from the list
people = ["Trevor", "Oscar", "Karen"]
people.remove("Oscar")
print(people)

#removes all the elements from the list, gives you an empthy list. 
people = ["Kyle", "Micheal", "John"]
people.clear()
print(people)

#"pops"(removes) the last element from the list
people = ["Xavier", "Robert", "Smith"]
people.pop()
print(people)

#amount of times that element was found in the list so it would be 2.
people = ["Jim", "Jim", "Micheal"]
print(people.count("Jim"))

#Will put the list in alaphbeltical order, puts numbers from lowest to highest.
items = ["Crown", "Sword", "Sheild"]
items.sort()
print(items)

#puts the list in reverse
random_numbers = [1, 28, 2893, 219, 2, 189]
radom_numbers.reverse()
print(random_numbers)

#Copys the list from the first list
num_list = [92, 83, 92, 783, 2]
num_list2 = num_list.copy()
print(num_list2)

#Tupel

#You can't change a tuples! Tuples are unchangeable!
coordinates = (3, 7, 9)
print(coordinates[0])

#Functions 

def say_hello():   #has to start with def
	print("Hello!") #has to be indented 

say_hello() #calls function 


def say_hello():   
	print("Hello!") 

say_hello()








