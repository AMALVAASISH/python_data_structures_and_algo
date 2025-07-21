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

