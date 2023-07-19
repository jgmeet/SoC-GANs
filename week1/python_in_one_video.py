
""" **** Data Types ****"""
"""
rating = 5.0      # float
name = "Jagmeet"  # string
marks = 100       # int

is_right = False  # bool
complex_number = 6 + 8j  # sets
a_list = ["Red","Green","Blue"]  # list

# checking data type
print(rating, type(rating))
print(type(a_list))
"""


""" **** Operators ****"""
"""
x = 15
y = 9

print(x+y) # sum of x and y
print(x/y) # x divide by y including decimals
print(x%y) # remainder when x divided by y
print(x//y) # only quationt when x divided by y
print(x**y) # x to the power y

# assignment operator
y += 3
# now, updated value of y is 12
print(y)

# relational operators
print('x>y', x>y)
print('x<=y', x<=y)

# logical operators (not, or, and)
t = True
f = False

print('not f is', not f)
print('t and f is', t and f)
print('t or f is', t or f)
"""



""" **** Input and Typecasting ****"""
"""
p = input('enter p: ')
q = input('enter q: ')

print('p is of ', type(p), ' type')
print('q is of ', type(q), ' type')

# as you can see, input takes string format
# to convert it into int, we need to do typecasting
p = int(p)  # or typecast at the time of input, p = int(input())
q = int(q)  # or typecast at the time of input, q = int(input())

r = p%q
print(r)
"""



""" **** if...else ****"""
"""
time = int(input("What's time now? "))

if time < 12 and time > 4:
    print('Good morning')
elif time >=12 and time < 16:
    print('Good afternoon')
elif time >= 16 and time < 20:
    print("Good evening")
else: print('Good night')
"""



""" **** range ****"""
"""
# range(first int, second int, steps)
# first int included, by default it's value is 0
# second int excluded, no default value, it's value given by user
# steps, default value is 1, take consecutive steps to reach second int from first int

a = range(10)
b = list(range(0,11,2))

print(a)
print(b)
"""



""" **** for and while loops ****"""
"""
for x in range(10):
    print(2*x, end=', ') # by default end is new line

char_list = ['p','q','r','s']
for char in char_list:
    print(4*char) # chars will be printed 4 times and will be in new lines
print(char)

n = 5
while n >= 0:
    print(n)
    n -= 1

"""



""" **** break and continue ****"""
"""
for i in range(8):
    if i > 5:
        break
    print(i)

for i in range(8):
    if i == 4:
        continue
    print(i)
print(i)
"""



""" **** Strings ****"""
# are immutable, Ex: st = "abcd", then st[2] = 't' will give error, as string is immutable
# string indexing starts from 0
# imp*, for multi line string, use triple qoutes only,
# can't write multi line string in double quotes, else will get error
fruit = "Apple"
# endexing for fruit from 0 to 4 or from -5 to -1
multi_line_string = """This is 
a multi
line string"""

"""
print(fruit)
print(multi_line_string)

# if endex provided out of range, then will get error
a = fruit[0] # 1st element
print(a)
b = fruit[-3] # 3rd last element
print(b)

# slicing, similar functionalities as of range
name = "JAGMEET"
c = name[0:3] # first included, second excluded
print(c)
d = name[0:6:2] # will skip 1 char
print(d)

# empty strings will be printed if dircn of traverse and dircn of steps are opposite
e = name[0:5:-1]
print(e)
f = name[-1:0:1]
print(f)
print(name[-1:-8]) # by default step is 1, so in opposite dirn

print(name[-1:-8:-1])

# concatination in string
str = fruit + name
print(str)

print(name*3)
for char in fruit:
    print(char*4)

# ** string methods, string will remain unaffected by applying theses methods
print('fruit.isaplha', fruit.isalpha()) # returns true if all chars are alphabets
print('fruit.isdigit', fruit.isdigit()) # returns true if all chars are digits
print('fruit.islower', fruit.islower()) # returns true if all alphabets are lower case
print('fruit.isupper', fruit.isupper()) # returns true if all alphabets are upper case

print('fruit.lower', fruit.lower()) # prints alphabets in lower case
print('fruit.upper', fruit.upper()) # prints alphabets in upper case
"""



""" **** Lists ****"""
"""
# are mutable
ls = 'abc'
ls = 4214
ls = [12,'hey',9.834,'to']
print(ls)
print(ls[2])

# slicing same as of string, no change

ls[0] = 987 # changes element at specified index
print(ls)
del ls[3] # deletes the element of specified index
print(ls)
# del fruits will delete the ls and will give if we will call it after calling del on it

# imp* - List comprehension
# new_list = [expression  for item in list  if condition]
a = [x for x in range(10)]
print(a)
b = [i for i in range(10) if i%2 == 0]
print(b)

# Lists methods
p = [1,2,3]
print(p)
p.append(4) # will insert 4 at the end of list p
print(p)
# note that p[3] = 4 will not work, it will give error
p.insert(1, 9.5) # will insert 9.5 at index 1
print(p)

fruit = ['Kiwi', 'Apple', 'Banana' ]
fruit.sort() # sorts list in increasing aplhabetical order and in integers, sort in increasing order
print(fruit)

fruit.reverse() # reverse the list
print(fruit)
fruit.pop(2) # removes element from index 2 of list
print(fruit)

print(fruit.index('Kiwi')) # gives index of Apple in list fruit
# fruit.index(element) will give error if element doesn't exist in list
print(fruit.count('Banana')) # gives number of occurences in list fruit
fruit.clear() # empty the whole list

# Lists functions
print('length of fruit list is', len(fruit)) # shp=ould be zero as line 233 empty the whole list

q = [6,8,2,6,7,5.2,3,9]
print('q:', q)
print('length of q is', len(q)) # gives length of list
print('max element in q is', max(q)) # gives max element
print('min element in q is', min(q)) # gives min element in q
print('sum of q is', sum(q)) # gives sum of elements in q
name = "JAGMEET"
print(name, type(name))
name = list(name) # converts string name to list name
print(name, type(name))
# print(sum(name)) will give error
for char in name:
    print(char)
"""



""" **** Tuples ****"""
# same functionalities as of lists, but are immutable like strings
tp = (7,3,2,6,9) # a tuple
print(tp)



""" **** Dictionary & Sets ****"""
"""
# sets
# sets are like lists, tuples
# sets don't have any indexing and all elements in sets are unqique, means no repition of elements
st = {3,6,8,7,4,1,4,6} # a set, elemnts are in randomm fashion, there's no indexing of elements
print(st)
for x in st:
    print(x**2)


# Dictionary
# stores (key,value) pair
grading_stats_BMC = {'AA':8, 'AB':12, 'BB':10, 'BC':9, 'CC':2, 'CD':4}
print('AA',grading_stats_BMC['AA'])
print('AB',grading_stats_BMC['AB'])

for grade in grading_stats_BMC: # grades iterates over keys and dict[grades] gives it's corresponding value
    print(grade, grading_stats_BMC[grade])

grading_stats_BMC['AP'] = 1 # will insert new key pair('AP',1)
grading_stats_BMC['AA'] = 10 # will modify value of key 'AA' to 10

for grade in grading_stats_BMC:
    print(grade, grading_stats_BMC[grade])
"""



""" **** Functions ****"""
# ** modules: math, random, string
# import math as m
from math import cos

print(cos(3.14159))
# print(pi) will give error


# ** user-defined
# def function_name(parameters):
#     body

def greet(names):
    for name in names:
        print('Hello', name)

names = ['Aditya','Deep','Jagmeet']
greet(names)



""" **** Files Handling ****"""
"""
f = open('Machine Learning/area.csv', 'r') # by default write mode

# print(f.readline()) # prints first line
# print(f.readline()) # prints second line
# f.readline() will read third line

for line in f:
    print(line)

# ** imp., don't forget to close file when you open it
# also note if there's any error in program before this line,
# then the below line will not execute, hence not recomended with this method
f.close()
"""
# with open, it will gaurantee to close, even if there's any error in program
with open('Machine Learning/area.csv') as f:
    # for line in f:
    #     print(line)
    # print(f.read()) # reads entire file
    print(f.read(3)) # reads first 3 chars
    print(f.read(10)) # reads next 10 chars 
    # here f is maintaining courser, which have access to the last locn of f.read()
    # f.seek(20) will cause courser to move to 20th char position 