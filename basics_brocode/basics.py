# multiple assignment in pyton


# x,y,z = "orange","apple","mango"
# print(z)


# unpacking a collection
# coll = [1,2,4]

# a,b,c = coll
# print(c)

# string methods

# text = "string is better than text"
# print(text.capitalize())
# print(text.upper())
# print(text.count('string'))


# https://www.geeksforgeeks.org/python/python-string-methods/

# mytuple = ('list', 'full')
# res = '-'.join(mytuple)
# print(res)

# https://www.geeksforgeeks.org/dsa/last-minute-notes-lmns-data-structures-with-python/

#  input
# name= input("enter your name\n")
# print("u can do it",name)

# math functions

# y = min(1,2,3,0.5)
# print(y)

# x = max(1,2,3)
# print(x)

# z = abs(-0.5)
# print(z)

# w = pow(2,3)
# print(w)


# string slicing

# s = "Hello amal"
# print(s[6:])

# print(s[::-1]) # reverse a string

# print(s[-2:-1])

# print entire string
# print(s[:])
# print(s[::])


# a = 1
# if a == 1:
#     print("its correct")
# elif a == 2:
#     print()
# else:
#     print()

# a = "amal"
# if a == "amal" and type(a) == str:
#     print("yay logical operators are done")


# while True:
#     print("its a while loop")


#nested loops

# i = 0
# for i in range(0,10):
#     print("\n")
#     for i in range(0,5):
#         print("*",end="") # using end="" removes the next line



# control statements, pass continue and break
# i = 0
# while True:
#     print("printing")
#     i += 1
#     if i == 0:
#         continue
#     elif i == 1:
#         print("final value", i)
#         break
#     else:
#         pass



# In Python, a list is a built-in dynamic sized array (automatically grows and shrinks). We can store all types of items (including another list) in a list. A list may contain mixed type of items, this is possible because a list mainly stores references at contiguous locations and actual items maybe stored at different locations.

# List can contain duplicate items.
# List in Python are Mutable. Hence, we can modify, replace or delete the items.


# List are ordered. It maintain the order of elements based on how they are added.



# Accessing items in List can be done directly using their position (index), starting from 0

# a = [1,2,3,4,"string"]
# print(type(a[0]))


# b = [0] * 5
# print(b)

# a = list((1,2,3,4)) # create a list using list constructor
# print(a)

# a.append(1) # adding an element at the end
# a.extend([1,2,3]) # adds multiple elements at the end
# a.insert(0,"string") # inserting at the required index

# print("modified list :",a)

# a[-1] = "last element"
# print("final modified list",a)

# a.remove(1) # remove the first occurence of 1
# print(a)

# a.pop() # removes the last element

# del a[0] # deletes the element at that index

# print(a)

# for i in a:
#     print(i)

# squares = [x**2 for x in range(0,2)]
# print(squares)


# rows, cols = (5,5)
# arr = [[0]*cols]*rows
# print(arr)

# arr2 = [[0 for i in range(5)] for j in range(5)] # created using list comprehension
# print(arr2)


# arr = [[0 for i in range(cols)] for j in range(rows)]

# # again in this new array lets change
# # the first element of the first row 
# # to 1 and print the array
# arr[0][0] = 1
# for row in arr:
#     print(row)

# happens because of shallow lists https://www.geeksforgeeks.org/python/python-using-2d-arrays-lists-the-right-way/ 


# arr = ("appl","mango")
# print(type(arr))

# # ordered, unchangeable and allows duplicates

# print(arr[1])


# arr = {10,1,2}
# print(type(arr))

# s = set([1,2,3]) # type casting into set using set()
# print(type(s))

# s.add(10)   
# print(s)

# values cannot be changed,no duplicate values

# there is no order in sets, s.clear()...to clear the content in the set

# d = {1: "amal",
#      2: "alan",
#      3: "karthik"}

# print(d[1])

# keys must be unique and immutable:  This means keys can be strings, numbers or tuples but not lists.
# hashing is used in sets and dictionary, so check the time complexity and space complexity in these

# def amal():
#     return "hi you just called amal"

# s = amal()
# print(s)

# func returning another func

# def fun1():
    
#     def fun2():
#         return "hi you called fun2 "

#     return fun2

# call = fun1()
# print(call())

# **kwargs  if we dont know the number of args coming in the func, we can put ** before the name of the parameter in the func,
# and it can make it a dictionary

# if only one * is used before the parameter name, then it can make it a tuple and can be accessed as kid[0]

# def func1(**kid):
#     print("this is the word", kid["word"], kid["name"])

# func1(name="amal", word="english")

# keyword arguments

# def func(c2,c1,c3):
#     print(c1+c2+c3)

# func(c3 = 1,c2=0,c1=2)



# non local keyword, using this when modifying a variable which inside a func, through a func inside it, it changes the value inside teh 
# variable and not create a new local variable

# def fun1():

#     a = 10

#     def fun2():
#         nonlocal a
#         a=54
#         print(a)
    
#     fun2()
#     print(a)

# fun1()


# closure in inner function

# def fun1(a): # outer function
    
#     def fun2(): # inner function
#         print(a)
#     return fun2  # returning function without parentheses

# closure_func = fun1("Hello, Closure!")
# closure_func()  # inner function remembers 'a'


# https://www.geeksforgeeks.org/python/python-inner-functions/ 

# a = 11
# print(f"the number is {a}")

# print("hi my name is %s" %('amal')) #using the % operator

# print(" the value of ps is %5.4f" %(3.1411)) # 5 - minimum width of the number, 4 is the no of decimal places

# print("we are all equal {}".format("right?"))

# print("{2} {0} {1}". format("you", "sir" ,"thank"))

# print("it can be reused {p} {p}".format(p="again"))

# https://www.geeksforgeeks.org/python/string-formatting-in-python/

# f-strings are faster and better than both %-formatting and str.format().

# import random

# print(random.random())


# # using choice() to generate a random number from a
# # given list of numbers.
# print("A random number from list is : ", end="")
# print(random.choice([1, 4, 8, 10, 3]))

# # using randrange() to generate in range from 20
# # to 50. The last parameter 3 is step size to skip
# # three numbers when selecting.
# print("A random number from range is : ", end="")
# print(random.randrange(20, 50, 3))

# import random
# print(random.randrange(10,20,1))

# a = [1,2,3,4,5]
# random.shuffle(a)
# print(a)

# Python random.seed() function is used to save the state of a random function so that it can generate some random numbers in Python on multiple executions of the code on the same machine or on different machines (for a specific seed value). The seed value is the previous value number generated by the generator. For the first time when there is no previous value, it uses the current system time.

# import random

# # using random() to generate a random number
# # between 0 and 1
# print("A random number between 0 and 1 is : ", end="")
# print(random.random())

# # using seed() to seed a random number
# random.seed(5)

# # printing mapped random number
# print("The mapped random number with 5 is : ", end="")
# print(random.random())


# The uniform() function is used to generate a floating point Python random number between the numbers mentioned in its arguments. It takes two arguments, lower limit(included in generation) and upper limit(not included in generation).

# import random
# print(random.uniform(10,20))


# try except and finally

# try: 
#     a = 10
#     # res = a/0
#     # res = a / "pee"
#     res = a/0
# except ZeroDivisionError as e :
#     print("error is", e)
# except Exception as e:
#     print(e)
# finally: 
#     print("i learned exception handling in python")


# import time
# print(time.time())

# from datetime import datetime
# current_time = datetime.now()

# print("date and time", current_time)

# current_time_time = current_time.time()

# print("only time", current_time_time)

# import time

# time.sleep(5) # delay the code for the time specified

# ________________________________detect a file in python

# import os
# print(os.path.exists("C:\\Users\\amalv\\Desktop\\striver_dsa\\python_data_structures_and_algo\\basics_brocode"))

# path = "C:\\Users\\amalv\\Desktop\\striver_dsa\\python_data_structures_and_algo\\basics_brocode"

# # for i in os.listdir(path):
# #     if i.endswith('.txt'):
# #         print(i)

# for i in os.listdir(path):
#     if i.endswith('.txt'):
#         if i == "hello.txt":
#             with open(i,"r") as f:
#                 for j in f.read():
#                     print(j, end="")
                    



# with open("hello.txt", "w") as f: # for append and writing , we use f.write()
#     f.write("hi i am amal , i just edited the file using code")

# print("\n")

# import time
# time.sleep(5)

# with open("hello.txt","r") as f:
#                 for j in f.read():
#                     print(j, end="")

# with open("create.txt", "x") as f:
#     print("the file is created")


# moving files

# import os
# import shutil
# import time

# path = os.getcwd()
# print(path)

# for i in os.listdir(path):
#     if os.path.isdir(i):
#         print(i)
#         move = i
#     if i == "create.txt":
#         textfile = i

# time.sleep(5)
# shutil.move(textfile, move)
# print("moving done")

# copying files

# import shutil
# import os

# s = 'source'
# t = 'destination'

# files = os.listdir(s)

# for fname in files:
#     shutil.copy(os.path.join(s,fname),t)


# import os

# if os.path.exists("amal.text"):
#     os.remove("amal.txt")


# os.rmdir("") # to remove a directory without any contents

# import shutil
# shutil.rmtree("") # removes the folder along with the contents


# https://www.geeksforgeeks.org/python/create-a-watchdog-in-python-to-look-for-filesystem-changes/

# import sys

# try :
#     while True:
#         print("")
# except KeyboardInterrupt:
#     sys.exit()

# https://www.geeksforgeeks.org/python/10-interesting-modules-in-python-to-play-with/


# duck typing 

# class Bird:
#     def fly(self):
#         print("fly with wings")

# class Airplane:
#     def fly(self):
#         print("fly with fuel")

# class Fish:
#     def swim(self):
#         print("fish swim in sea")

# # Attributes having same name are
# # considered as duck typing
# for obj in Bird(), Airplane(), Fish():
#     obj.fly()

# walrus operator

# Walrus Operator allows you to assign a value to a variable within an expression. This can be useful when you need to use a value multiple times in a loop, but don't want to repeat the calculation.

# The Walrus Operator is represented by the := syntax and can be used in a variety of contexts including while loops and if statements. The Assignment expressions allow a value to be assigned to a variable, even a variable that doesn’t exist yet, in the context of expression rather than as a stand-alone statement.

## The below example is without Walrus Operator


# foods = list()
# while True:
#   food = input("What food do you like?: ")
#   if food == "quit":
#     break
#   foods.append(food)

# # Below Approach uses Walrus Operator

# foods = list()
# while (food := input("what food do u like the most")) != "quit":
#     foods.append(food)

# funcs to variables

# def a():
#     print("GFG")

# var = a
# var()


# +++++++

# x = 12

# def display():
#     x = 1
#     print(x)
#     print(globals()['x'])

# a = display
# a()

# higher order functions

# hof can accept another func as argument and also return a func as result

# def greet(func):
#     return func("hello")

# def uppercase(text):
#     return text.upper()

# print(greet(uppercase))


# def fun(n):
#     return lambda x : x *n

# double = fun(2)
# print(double(2))

# built in higher order funcs

# map func
# A higher-order function that takes another function as an argument and applies it to each element in an iterable, enabling transformation without explicit loops.

# https://www.geeksforgeeks.org/python/higher-order-functions-in-python/ 

# a = [1,2,3,4]

# res = list(map(lambda x : x*3 ,a))
# print(res)

#filter func

# A higher-order function that accepts a function to evaluate each element, returning only those that satisfy the given condition.

# a  = [1,2,3,4]
# res =list(filter(lambda x: x %2 == 0, a))
# print(res)


# # sorted func
# # sorting words based on length
# a = ["python", "java", "javascript"]

# res = sorted(a, key=len)
# print(res)

# reduce func

# The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along

# returns the final single value as output

# from functools import reduce

# a = [1,2,3,4]

# res = reduce(lambda x,y : x+y, a)
# print(res)


# closures

# def counter(start=0):  # higher order function
#     count = start 
    
#     def increment():  # inner function
#         nonlocal count  # retains access to 'count' even after counter() ends
#         count += 1
#         return count
    
#     return increment  # returns the inner function

# counter1 = counter(5)  # closure retains count = 5
# print(counter1())  
# print(counter1())  

# counter2 = counter(10)  # new closure with count = 10
# print(counter2())

# lambda funcs

# a =lambda x: x * 2
# print(a(3))

#lambda funcs with condition checking

# a = lambda x : "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
# print(a(10))

# lambda func with list comprehensions

# li = [lambda arg=x : arg*10 for x in range(1,5)]
# for i in li: 
#     print(i())

# list comprehension 

# a = [1,2,3,4]

# res = [val*2 for val in a]
# print(res)

# zip func in python

# The zip() function in Python combines multiple iterables such as lists, tuples, strings, dict etc, into a single iterator of tuples. Each tuple contains elements from the input iterables that are at the same position.


names = ['amal', 'alan', 'karthik']
scores = ['9.8', '9.9', '10.0']

res = zip(names,scores)
print(list(res))

for i in res:
    print(i) # prints tuples

# https://www.geeksforgeeks.org/python/zip-in-python/
# https://www.geeksforgeeks.org/python/python-dictionary-comprehension/ 
