# The original source of the notions seen bellow is the following : https://www.youtube.com/watch?v=XKHEtdqhLK8

# NOTE If a comment start with "NOTE" Then that is not a line of code, it's just a note
# NOTE The first line of each section is the name of the section, not code. Remove the "#" to test code.
# NOTE To stop code running, just press crtl + c ... yes, i am serious. I didn't believed it at first too. This helps in endless loops

# Print

# print("Hello World")



# variables types

# name = "Gervais"
# age = 18
# fullName = "Alexandre" + " " + name
# print(type(name))
# print("Hello " + fullName + ", you are " + str(age) + " years old.")
# isGrounded = False
# print(type(isGrounded))



# multiple assignment (different ways of defining variables)

# name, age, isBehindYou = "Alexandre", 18, True
# Alex = Lucas = Etienne = 18



# String Methods 
# NOTE (isdigit checks if it's a digit. isalpha check if it's with the alphabet)
# NOTE (count returns to amount of letter given present in the string. find return the index of the first letter given in the string)

# paragraph = "aleXaNDre "
# print(len(paragraph))
# print(paragraph.find("a"))
# print(paragraph.capitalize())
# print(paragraph.upper())
# print(paragraph.lower())
# print(paragraph.isdigit())
# print(paragraph.isalpha())
# print(paragraph.count("a"))
# print(paragraph.replace("n","m"))
# print(paragraph*3)



# Change value types

# x = 1
# y = 2.5
# z = "3"
# print(type(x))
# print(type(y))
# print(type(z))

# Changed Value types

# print(type(str(x)))
# print(type(int(y)))
# print(type(float(z)))



# Make type of value change

# x = str(x)
# y = int(y)
# z = float(z)



# Inputs

# yourName = input("Enter your name here : ")
# yourAge = int(input("Enter your age here : "))
# yPosition = float(input("Your Y position: "))
# yourAge = yourAge + 1
# yPosition = yPosition*3
# print("Hello " + yourName + ", your age next year : " + str(yourAge) + ", your Y position is " + str(yPosition))



# Maths 
# NOTE (pow = power (exposant in french). max return the biggest number given and min... does the opposite duh)

# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi,2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))



# Slicing indexing[]
# NOTE variable[start:stop:step]
# NOTE If nothing is entered in the [start] or [stop] sections, but a : is there,
# NOTE the value by default will be 0 for [start] and the lenght of the string for [stop]

# name = "Alexandre Gervais"
# firstName = name[0:9]
# lastName = name[10:]
# weirdName = name[::2]
# reversedName = name[::-1]
# print(firstName + " " + lastName + " " + weirdName + " " + reversedName)



# Slicing slice()
# NOTE Indexing and Slicing are very similar

# website1 = "https://google.com"
# website2 = "https://chat.openai.com"
# websiteSlice = slice(8,-4)
# print(website1[websiteSlice] + " " + website2[websiteSlice])



# if statements

# age = int(input("Your age : "))
# if age >= 18:
#     print("Adult Detected")
# elif age < 18:
#     print("Free Kill Detected")
# elif age == 100:
#     print("Another Free Kill Detected")
# else:
#     print("ERROR")



# Logical Operators (and (&& in JavaScript), or (|| in JavaScript), not (!== in JavaScript))

# date = int(input("What day of the month is it? "))
# if date >= 1 and date<=10:
#     print("It's the beginning of the month")
# elif date==14 or date==15 or date==16:
#     print("It's the middle of the month")
# elif not((date>=1 and date<=10) and (date==14 or date==15 or date==16)):
#     print("Nothing special")
# else:
#     print("ERROR")



# While loop

# name = None
# while not name:
#     name = input("Enter your name ")
# print("Hello " + name)



# For loop

# for i in range(10):
#     print(i)
# for index in range(50,100,5):
#     print(index)
# for i in "Joe":
#     print(i)
# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Good Morning")



# Nested loop (a loop in a loop)

# rows = int(input("How many rows? "))
# columns = int(input("How many columns? "))
# symbol = input("What symbol do you want? ")
# for i in range(rows):
#     for j in range(columns):
#         print(symbol, end="")
#     print()



# Loop controls
# NOTE  break = stops the entire loop. continue = skips to the next iteration of the loop. pass = does nothing

# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break
# phoneNmb = "123-456-7890"
# for i in phoneNmb:
#     if i == "-":
#         continue
#     print(i,end="")
# print("")
# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i, end=" ")



# List (Array(tableau in french))

# classes = ["Video","Prog","Web","Audio","3D"]
# for i in range(0,len(classes)):
#     print(classes[i])
# classes[0] = "ThisClassSucks"
# classes.append("Photoshop")
# classes.remove("ThisClassSucks")
# classes.pop()
# classes.insert(2,"2D Animation")
# classes.sort()
# classes.clear()



# 2D Arrays (Lists in a list)

# drinks = ["Water", "Coffee", "Milk", "Soda"]
# meals = ["Chicken", "Lasagna", "Steak", "Sushi"]
# desserts = ["Cake", "Ice Cream", "Brownies", "Pie"]
# menu = [drinks, meals, desserts]
# for i in range(0,3):
#     for j in range(0,4):
#         print(menu[i][j], end=" ")
#     print("")



# Tuple

# student = ("Chad",19,"male")
# for i in student:
#     print(i, end=" ")
# print("")
# if "Chad" in student:
#     print("Chad is a student")



# Sets (Is a collection that is unordered, unindexed and duplicated values are ignored)
# NOTE difference returns only the values only present in one of the two sets given.
# NOTE intersection returns only the values present in both the two sets given.

# utensils = {"Fork","Spoon","Knife"}
# dishes = {"Bowl", "Plate", "Cup", "Knife"}
# things = {"Table", "Chair", "Flowers"}
# utensils.add("Napkin")
# utensils.remove("Spoon")
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))
# utensils.update(dishes)
# dinnerTable = utensils.union(things)
# for i in dinnerTable:
#     print(i, end=" ")
# utensils.clear()



# Dictionary (objects in JavaScript)

# moneySpread = {"Thanos": "12$",
#                "Obama": "750 000$",
#                "Mickey Mouse": "-300 000$",
#                "DiscordMod": "1$"}
# print(moneySpread.get("Jon"))
# moneySpread.update({"Jon Arbuckle": "250$"})
# moneySpread.update({"Mickey Mouse": "-300 001$"})
# moneySpread.pop("DiscordMod")
# print(moneySpread.keys())
# print(moneySpread.values())
# print(moneySpread.items())
# for key,value in moneySpread.items():
#     print(key, value)
# moneySpread.clear()



# functions

# def greeting(param):
#     print("hello " + param)
# name = None
# while not name:
#     name = input("Enter your name ")
# greeting(name)



# Return

# def multiplication(number1,number2):
#     return number1*number2
# theSuperEpicCalculatedNumber = multiplication(10,5)
# print(theSuperEpicCalculatedNumber)



# Keyword Arguments (basically, arguments can be entered in any order with this)

# def hello(first,middle,last):
#     print("Hello "+first+" "+middle+" "+last)
# hello(last="Robinson",first="Dimitri",middle="Kelvin")



# Nested Function Calls

# num1 = input("Choose a full number: ")
# num1 = float(num1)
# num1 = abs(num1)
# num1 = round(num1)
# print(num1)
# NOTE or a fast method of doing the same thing
# print(round(abs(float(input("Choose a full number: ")))))



# Args (Make it so no errors occurs if more argument than planned are declared)

# def addition(*number):
#     total = 0
#     number = list(number)
#     number[2] = -2
#     for i in number:
#         total += i
#     return total
# print(addition(1,20,34))



# Kwargs (Arguments added to a dictionary)

# def hello(**names):
#     message = "Hello "
#     for key,value in names.items():
#         message = message + value + " "
#     return message
# print(hello(first="Joe",middle="Blast",last="Biden"))



# string .format (a way to add variables in strings)

# food = "cheese"
# thingy = "fridge"
# text = "I just got some {} out of the {}"
# print(text.format(food,"oven"))
# print("I just got some {1} out of the {0}".format(thingy,"milk"))
# print("I just got some {coldFood} out of the {container}".format(coldFood="ice cream",container="freezer"))
# print("Hello, my name is {:30}. Nice to meet you".format("Alexandre"))
# print("Hello, my name is {1:^30}. Nice to meet you".format("Roberto","Dimitri"))
# print("Hello, my name is {lastName:>30}. Nice to meet you".format(lastName="Gervais"))
# nbPi = 3.14159
# print("Pi is {:.2f}".format(nbPi))
# bigNumber = 1000000
# print("Very big number: {:,}".format(bigNumber))
# print("Very big binary number: {:b}".format(bigNumber))
# print("Very big octal number: {:o}".format(bigNumber))
# print("Very big hexadecimal number: {:x}".format(bigNumber))
# print("Very big number in scientific notation: {:e}".format(bigNumber))



# Random

# import random
# x = random.randint(1,10)
# y = random.random()
# allOptions = ["rock","paper","scissors"]
# z = random.choice(allOptions)
# print("Value X : {}, Value Y : {}, Value Z : {}".format(x,y,z))
# cards = ["A",2,3,4,5,6,7,8,9,"J","Q","K"]
# random.shuffle(cards)
# print(cards)



# exception (If an error occurs in a try block of code, the block of code in except will occurs, depending on the error type.)

# try:
#     numerator = int(input("Enter a numerator: "))
#     denominator = int(input("Enter a denominator: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("Cannot divide by zero")
# except ValueError:
#     print("Enter numbers, not words!")
# except Exception:
#     print("Something went wrong")
# else:
#     print(result)
# finally:
#     print("This will always execute")



# File detection (Checks if a file exists / is a directory or file)

# import os
# computerName = input("Entrer le nom du User sur votre ordinateur ")
# filePath = "C:\\Users\\{}\\Documents\\GitHub".format(computerName)
# if os.path.exists(filePath):
#    print("Location exists")
#     if os.path.isfile(filePath):
#         print("This is a file")
#     elif os.path.isdir(filePath):
#         print("This is a directory")
# else:
#     print("This location doesn't exist")



# Read a file (read the contents of a file (usally .txt files and used to remember values after the program is closed))

# try:
#     with open("./test.txt") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("Error 404")



# Write a file (Creates a file (\n makes a linebreak (enter key)))

# text = "Hello, this is a file write test\nThis is epic\nYes I agree\n"
# fileName = input("What do you want the text file to be called? ")
# fileName = fileName + ".txt"
# with open(fileName, "w") as file:
#     file.write(text)
#     print("Your text has overriten/created '{}' !".format(fileName))
# with open(fileName, "a") as file:
#     file.write(input("What do you want to write inside of '{}' ? ".format(fileName)))
#     print("Your answer was added to '{}' !".format(fileName))



# Copy a file
# NOTE copyfile() = copies the contents of the file
# NOTE copy() = copyfile() + permission mode + destination can be a directory
# NOTE copy2() = copy() + copies metadatas

# import shutil
# shutil.copyfile("./test.txt","./copy.txt")



# Delete a file
# NOTE rmdir = deletes a directory, but not the content inside
# NOTE rmtree = deletes a directory and EVERYTHING inside.

# import os
# import shutil
# try:
#     os.remove("./test2.txt")
#     os.rmdir("./folderTest")
#     shutil.rmtree("./folderTestWithContent")
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("The permission to delete the file was denied.")
# except OSError:
#     print("Cannot delete the file using the used function")
# else:
#     print("You deleted the file")



# Modules (File containing python code)

# import modules_example as msg
# msg.hello()
# msg.bye()



# Modules but it's a different import method

# from modules_example import hello,bye
# hello()
# bye()



# Finding available modules (Usefull to see premade modules, like random or math)

# help("modules")



# Rock Paper Scissors (To see to code, check the "RockPaperScissors.py" file)

# from RockPaperScissors import rps
# rps()



# Quiz Game (To see to code, check the "quizGame.py" file)
