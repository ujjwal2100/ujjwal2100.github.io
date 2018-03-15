#importing the math function
#import math
#print(math.pi)
#text="I am doing good"
#print (text)
#number=10
#number_dec=10.2
#result=number+number_dec
#print(result)

#Strings
dedication ="Your planet, love."
dedication[0:4]
st= "hello"
together=dedication+st
print(together)
together.find("love")
together[together.find("love")]

# F String: It adds the two strings together including your comments
msg=f"I wrote {dedication} then it goes {st}"
print(msg)

#Boolean
reality = True
non_reality = False
print(reality and not non_reality)
h=7
k=8
print(h==k)
o=1
l=1.0
print(o==l)

#LIST
#Object Literal
l_one = []
x=5
l_two = [1, 2.0, "a", "ancd", True, x]
print(l_two)
l_three = ["a", "b", "c"]
l_two.append(l_three)
print(l_two)

square = []
for i in range(5):
    square.append(i*i)
print(square)

#Dictionaries: Also what is the difference between list and dictionaries
#Key value pairs
d_one = {'key1': 1, 'key2': "moose", 'key3': 4}
print(d_one)
d_one['key1']
d_one[6] = 'six'
d_one[6]
print(d_one)

#Python tinks in objects

### Branches

You can think of branches as decisions based on criteria you provide. If-elif-else statements execute a block of code if a given condition is true, and a different block of code if a given condition is false. Take note of the syntax in the below example: `if [statement]:` is followed by a line break, then a tab. If you do not follow this syntax, your code will not work correctly! Python is somewhat distinctive in that it reads meaning into levels of indentation; it *interprets* some types of *whitespace*. The code that is indented one level (one tab) below an if-elif-else statement will be executed when that statement's condition is true. The same holds true for loops and function calls, as we'll see below.

flag = False
if flag:
    x = 1
    print("Flag is True.")
else:
    x = 2
    print("Flag is False.")
print(x)

### Loops

Loops allow us to automate repetitive tasks (hooray!). Repeatedly executing a set of statements is called *iteration*. There are a number of way to iterate in Python. We can use `for` loops or `while` loops. The syntax is like the syntax of if-statements---notice the indentations! The `for` loop loops over each of the elements of a list or iterator, assigning the current element to the variable name given. A `while` loop repeats a sequence of statements until some condition becomes false.

x = range(5)
#x=(1,2,3,4,5,6,7,8,9,10)
#print(x)

for i in x:
    print(i)

for i in x:
    # doubles the list element
    print(i*2)

    for i in range(10):
        if (i > 5):
            break # breaks out of the loop when it gets a number higher than five
        print(i)

#FUNCTIONS

x = 0
for i in range(100):
    #x += i
    x=x+i
print(x)

# What if we want to do this for a new initial value for x? What if we use a different number instead of 100? We don't want to rewrite this for loop every time, so let's define a function!
def for_sum(x, y):
    for i in range(y):
        x += i
    # "return" indicates what values to output
    return x
for_sum(0,100)


# NumPy is the fundamental package for scientific computing with Python
# import the numpy package
import numpy as np

# without vectorized numpy arrays
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
c = []
for i, j in zip(a, b):
  c.append(i + j)
print(c)

# with vectorized numpy arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
c = a + b
print(c)

import numpy as np
c=np.zeros((3,4))
print(c)
