
#if elif statements

'''marks = int(input("Enter your marks"))

if marks >= 90:
    print("You have grade A")
elif marks >= 70:
    print("you have grade B")

elif marks >= 60:
    print("you have grade C")

elif marks < 60:
    print("Grade D")

#lists in python
names = ["mike","john","rob","kamau"]

print(names)
'''
'''
numbers = [1,1,1,1,1]

numbers[2] = 5

print(numbers)

fruits = ["apple", "mango", "oranges"]

print("oranges" in fruits)
'''
'''
#range
numbers = list(range(1,31,5))

print(numbers)


#code reuse and functions

def function1():
    print("peter")
    print("kirumba")
    print("new york")

function1()
'''
'''
#for loop
for nums in range(1,20):
    print(nums)

for x in range(1,11):
    print(x)


def repeat_name():
    for nums in range (1,6):
        print("peter kirumba is awsome")

repeat_name()

fruits = ["apple", "banana", "peach","orange"]

for name in fruits:
    print(name)

#prints even numbers
for nam in range(0,21,2):
    print(nam)

'''
'''
username = input("what is your username")

password = input("what is your password")

if username == "admin" and password == "admin123":
    print("valid user")

else:
    print("invalid user")
username = input("what is your username: ")

password = input("what is your password: ")

if username == "admin" or password == "admin123":
    print("valid user")

else:
    print("invalid user")

'''
'''
counter = 0

while(counter <= 11):
    print(counter)

    counter+=1

food_items = ["mukimo","njahi","meat","beans","sorghum"]

print(food_items[3])

food_items.append("potatoes")

print(food_items)

food_items[3] = "tacos"

print(food_items)
'''
'''

def repeat():
    count = 0
    while(count <= 10):
        count =+ 1
        print("peter you are a hero")
repeat()
'''

'''
for words in range (6):
    print("i am a programmer")

def square_num():
    for x in range (0,10):
        print(x*x)
square_num()
'''
'''
def add_nums(num1, num2):
    num3 = num1 + num2
    return num3

result = add_nums(10,20)

print(result)

 '''
'''
def add(a, b):
     return a+b

def square_num(c):
    return c * c

result = square_num(add(2, 3))

print(result)
'''


#modules 
'''

import random 

for x in range(5):

    result = random.randint(1,6)

    print(result)
'''
'''
#BMI calculator
def calculate_bmi(new_height, new_weight):
    new_bmi = new_weight/(pow(new_height, 2))
    return new_bmi

weight = float(input("enter weight in kgs: "))
height = float(input("enter height in meters: "))

bmi = calculate_bmi(weight,height)

print(bmi)
'''

#errors and exceptions
"""
try:
    a = 20
    b = 5
    print(a/b)

except ZeroDivisionError:
    print("There is a divide zero error")

finally:
    print("this is going to execute no matter what")

"""
"""
file = open("homeyy.txt", 'r')

content = file.read()

print(content)

file.close()
"""
'''
file = open("homey.txt", 'w')

file.write("this is the written file")

file.close()
'''
'''
for items in range(5):
    print("you should work")

#dictionaries

people = {
    'john':32,
    'rob':23,
}

print(people["john"])


numbers = {
    1:"one",
    2:"two",
    3:"three"
}

print(5 in numbers)
print(2 in numbers)

print(numbers.get(5, "key not found"))

#tuples..// they are immutale
fruits = ("apple", "mango","peach")
print(fruits[0])
'''
#list slicing
'''
numbers = [0, 100, 200, 300, 400, 500, 600]

print(numbers[4:6])

'''
'''
numbers = [1,1,1,1,1,1]

numbers[2] = 5

print(numbers)
'''
#list comprehension
'''
list = [x**2 for x in range(10) if x**2 % 2 == 0]

print(list)
'''
'''
numbers = [12,12,2016]

newstringg = "date:{0}/{1}/{2}".format(numbers[0],numbers[1],numbers[2])

print(newstringg)


a = "{x}/{y}".format(x = 100, y = 200)

print(a)

#string functions

print("/".join(["apple","banana","mango"]))

print("hello there".replace("there", "world"))

newstring = "hello world"
print(newstring.replace("there", "world"))

newstring = "this is a string"
print(newstring.startswith("this"))
print(newstring.endswith("boy"))
print(newstring.upper())
print(newstring.lower())
'''
'''
print(min(1,2,3,4,5,6,7,8))
print(max(1,2,3,4,5,6,7,8))
print(abs(-203))
'''
'''
products = {
    "volvo":2000,
    "isuzu":3000,
    "mazda":4000,
    "canter":5000,
    "mitsrubishi":6000
}
newproduct = input("enter the name of product: ")
if(newproduct in products):
    print(products.get(newproduct))
else:
    print("product not found")

lists = [x for x in range(1,100) if x % 2 != 0]
print(lists)

new_list = list(range(1, 100))

for x in new_list:

    if x % 2 != 0:
        print (x)
'''
'''
#FUNCTIONAL PROGRAMMING
def add_ten(x):
    return x + 10

def twice(func, arg):
    return func(func(arg))

print(twice(add_ten,10))

#LAMDAS
def square(x):
    return x**2

print(square(4))


result = (lambda x: x**2)(30)
print(result)

#map
def add(x):
    return x+2

newlist = [10,20,30,40,50]

result = list(map(add, newlist))

print(result)
'''

'''
newlist = [1,2,3,4,5,67,5]

result = list(filter(lambda x: x%2 == 0,newlist))

print(newlist)
'''

'''
#generators

def function():
    counter = 0
    while counter < 5:
        yield counter
        counter += 1

for x in function():
    print(x)

def even_numbers(x):

    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(even_numbers(21)))
'''
'''
def student_discount(price):
    price = price - (price * 10) / 100
    return price

def additional_discount(newprice):
    newprice = newprice - (newprice * 5) / 100
    return newprice

selling_price = 100

#applying both discounts simultaneously

print(student_discount(additional_discount(selling_price)))

result = (lambda x: x*(x+5)**2)(5)
print(result)


def discount(price):
    price = price - (price * 10) / 100
    return price

product_prices = [100, 200, 300, 400, 500]

updated_prices = list(map(discount,product_prices))

print(updated_prices)
'''
'''
#OOP
class Students:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print("accepting data")
        self.contact = input("Enter name: ")
        self.name = input("Enter name: ")

    def putdata(self):
        print("the name is: "+self.name,"The contact is: "+self.contact)


John = Students("BLANK",0)
John.getdata()
John.putdata()
'''
'''
#INHERITANCE

class Students:
    def __init__(self,name,contact):
        self.name = name
        self.contact = contact

    def getdata(self):
        print("accepting data")
        self.contact = input("Enter contact: ")
        self.name = input("Enter name: ")

    def putdata(self):
        print("the name is: "+self.name,"The contact is: "+self.contact)

class ScienceStudent(Students):
    def __init__(self,age):
        self.age = age

    def science(self):
        print("i am a science student")

Rob = ScienceStudent(20)
Rob.science()
Rob.getdata()
Rob.putdata()
'''

#recursion
def factorial(x):
    if(x == 1):
        return 1
    else:
        return x*(factorial(x-1))

result = factorial(5)
print(result)

#sets

numbers = {1,2,3,4,5,6,7}
print(numbers)
print(5 in numbers)
numbers.add(9)
print(numbers)
numbers.remove(4)
print(numbers)


seta = {1,2,3,4,5}
setb = {4,5,6,7,8}

print(seta | setb)#union of the sets
print(seta & setb)#ntersection of sets---elements common between the two sets

#itertools
"""
from itertools import count

for i in count(3):
    print(i)

    if i >= 20:
        break
"""
'''
from itertools import accumulate, takewhile

numbers = list(accumulate(range(8)))

print(numbers)
print(list(takewhile(lambda x: x <= 10, numbers)))
'''
'''
#operator overloading

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

point1 = Point(1, 4)
point2 = Point(2, 8)
print(point1 + point2)
'''
'''
#data hidng(encapsulation)
class Myclass:
    __hiddenvariable = 0


    def add(self,increment):
        self. __hiddenvariable += increment
        print(self.__hiddenvariable)

objectone = Myclass()
objectone.add(5)
print(objectone.__hiddenvariable)
'''
'''
class Computer:
    def __init__(self,ram,memory):
        self.ram = ram
        self.memory = memory

    def Getspecs(self):
        print("please enter the details")
        self.ram = input("Enter the ram_size: ")
        self.memory = input("Enter the memory_size: ")

    def Displayspecs(self):
        print("here is the specs of the computer")
        print("the ram is: "+ self.ram,"the memory is: "+self.memory)

class Desktop(Computer):
    def __init__(self,color):
        self.color = color

    def getcolor(self):
        self.color = input("Enter the color : ")

    def displaycolor(self):
        print("the color is: "+self.color)


class Laptop(Computer):
    def __init__(self,weight):
        self.weight = weight


    def getweight(self):
        self.weight = input("Enter the weight : ")

    def displayweight(self):
        print("the weight is: "+self.weight)

Comp = Computer("blank","blank")
comp = Laptop("")
Desk = Desktop("")
Desk.getcolor()
Desk.displaycolor()
Comp.Getspecs()
Comp.Displayspecs()
comp.getweight()
comp.displayweight()
'''

#regular expressions
"""
import re

pattern = r"eggs"

if re.match(pattern,"baconeggseggseggsbacon"):
    print("match found")

else:
    print("no match found")

if re.search(pattern,"baconeggseggseggsbacon"):

    print("match found")
else:
    print("match not found")

if re.findall(pattern,"baconeggseggseggsbacon"):

    print("match found")
else:
    print("match not found")

"""
"""
import re

string = "my name is john, hi i'm john"

pattern = r"john"

newstring = re.sub(pattern, "rob",string)#sub function useses the pattern to replace 

print(newstring)
"""
'''
import re

pattern = r"gr.y"

if re.match(pattern,"gray"):

    print("match found")

'''
'''
import re

pattern = r"^gr.y$"

if re.match(pattern, "grty"):
    print("match 1")

'''
"""
import re

pattern = r"[A-Z][A-Z][0-9]"

if re.search(pattern, "AA6"):
    print("match found")

else:
    print("match not found")
"""

#STAR METACARACTER
import re

pattern = r"eggs(bacon)*"

if re.match(pattern,"eggsbacon"):
    print("match found")

#groups

import re

pattern = r"bread(eggs)*bread"

if re.match(pattern, "breadeggseggsbread"):
    print("match found")
