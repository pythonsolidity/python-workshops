#!/usr/bin/env python
# coding: utf-8

# # Introduction to Python Statements

# Let's create a simple statement that says:
# "If a is greater than b, assign 2 to a and 4 to b"
# 
#     if a>b:
#         a = 2
#         b = 4

# ## Indentation    

# Note how Python is so heavily driven by code indentation and whitespace. This means that code readability is a core part of the design of the Python language.
# 
# Now let's start diving deeper by coding these sort of statements in Python!

# # if, elif, else Statements
# 
# <code>if</code> Statements in Python allows us to tell the computer to perform alternative actions based on a certain set of results.
# 
# Verbally, we can imagine we are telling the computer:
# 
# "Hey if this case happens, perform some action"
# 
# We can then expand the idea further with <code>elif</code> and <code>else</code> statements, which allow us to tell the computer:
# 
# "Hey if this case happens, perform some action. Else, if another case happens, perform some other action. Else, if *none* of the above cases happened, perform this action."
# 
# Let's go ahead and look at the syntax format for <code>if</code> statements to get a better idea of this:
# 
#     if case1:
#         perform action1
#     elif case2:
#         perform action2
#     else: 
#         perform action3

# ## First Example
# 
# Let's see a quick example of this:

# In[ ]:


var = 1

if var == 1:
    print('It was true!')


# Let's add in some else logic:

# In[ ]:


x = 10

if x < 5:
    print('Ignore x!')
else:
    print('Cannot ignore x')


# Note how the nested <code>if</code> statements are each checked until a True boolean causes the nested code below it to run. You should also note that you can put in as many <code>elif</code> statements as you want before you close off with an <code>else</code>.
# 
# Let's create two more simple examples for the <code>if</code>, <code>elif</code>, and <code>else</code> statements:

# In[ ]:


person = 'Alice'

if person == 'Alice':
    print('Welcome Alice!')
else:
    print("Welcome, what's your name?")


# In[ ]:


person = 'Bob'

if person == 'Alice':
    print('Welcome Alice!')
elif person =='Bob':
    print('Welcome Bob!')
else:
    print("Welcome, what's your name?")


# # for Loops
# 
# A <code>for</code> loop acts as an iterator in Python; it goes through items that are in a *sequence* or any other iterable item. Objects that we've learned about that we can iterate over include strings, lists, tuples, and even built-in iterables for dictionaries, such as keys or values.
# 
# We've already seen the <code>for</code> statement a little bit in past lectures but now let's formalize our understanding.
# 
# Here's the general format for a <code>for</code> loop in Python:
# 
#     for item in object:
#         statements to do stuff
#     

# The variable name used for the item is completely up to the coder, so use your best judgment for choosing a name that makes sense and you will be able to understand when revisiting your code. This item name can then be referenced inside your loop, for example if you wanted to use <code>if</code> statements to perform checks.
# 
# Let's go ahead and work through several example of <code>for</code> loops using a variety of data object types. We'll start simple and build more complexity later on.
# 
# ## Example 1
# Iterating through a list

# In[ ]:


# We'll learn how to automate this sort of list in the next lecture
list1 = [1,2,3,4,5,6,7,8,9,10]


# In[ ]:


for num in list1:
    print(num)


# Great! Hopefully this makes sense. Now let's add an <code>if</code> statement to check for even numbers. We'll first introduce a new concept here--the modulo.
# ### Modulo
# The modulo allows us to get the remainder in a division and uses the % symbol. For example:

# In[ ]:


17 % 5


# This makes sense since 17 divided by 5 is 3 remainder 2. Let's see a few more quick examples:

# In[ ]:


# 2 no remainder
4 % 2


# Notice that if a number is fully divisible with no remainder, the result of the modulo call is 0. We can use this to test for even numbers, since if a number modulo 2 is equal to 0, that means it is an even number!
# 
# Back to the <code>for</code> loops!
# 
# ## Example 3
# Let's print only the even numbers from that list!

# In[ ]:


for num in list1:
    if num % 2 == 0:
        print(num)


# We could have also put an <code>else</code> statement in there:

# In[ ]:


for num in list1:
    if num % 2 == 0:
        print(num)
    else:
        print('Odd number')


# ## Example 3
# Another common idea during a <code>for</code> loop is keeping some sort of running tally during multiple loops. For example, let's create a <code>for</code> loop that sums up the list:

# In[ ]:


# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum = list_sum + num

print(list_sum)


# Great! Read over the above cell and make sure you understand fully what is going on. Also we could have implemented a <code>+=</code> to perform the addition towards the sum. For example:

# In[ ]:


# Start sum at zero
list_sum = 0 

for num in list1:
    list_sum += num

print(list_sum)


# ## Example 4
# We've used <code>for</code> loops with lists, how about with strings? Remember strings are a sequence so when we iterate through them we will be accessing each item in that string.

# In[ ]:


for letter in 'This is a string.':
    print(letter)


# ## Example 5: Dictionaries

# In[ ]:


d = {'k1':1,'k2':2,'k3':3}


# In[ ]:


for item in d:
    print(item)


# Notice how this produces only the keys. So how can we get the values? Or both the keys and the values? 
# 
# We're going to introduce three new Dictionary methods: **.keys()**, **.values()** and **.items()**
# 
# In Python each of these methods return a *dictionary view object*. It supports operations like membership test and iteration, but its contents are not independent of the original dictionary – it is only a view. Let's see it in action:

# In[ ]:


# Create a dictionary view object
d.items()


# Since the .items() method supports iteration, we can perform *dictionary unpacking* to separate keys and values just as we did in the previous examples.

# In[ ]:


# Dictionary unpacking
for k,v in d.items():
    print(k)
    print(v) 


# If you want to obtain a true list of keys, values, or key/value tuples, you can *cast* the view as a list:

# In[ ]:


list(d.keys())


# Remember that dictionaries are unordered, and that keys and values come back in arbitrary order. You can obtain a sorted list using sorted():

# In[ ]:


sorted(d.values())


# # while Loops
# 
# The <code>while</code> statement in Python is one of most general ways to perform iteration. A <code>while</code> statement will repeatedly execute a single statement or group of statements as long as the condition is true. The reason it is called a 'loop' is because the code statements are looped through over and over again until the condition is no longer met.
# 
# The general format of a while loop is:
# 
#     while test:
#         code statements
#     else:
#         final code statements
# 
# Let’s look at a few simple <code>while</code> loops in action. 

# In[ ]:


x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1


# Notice how many times the print statements occurred and how the <code>while</code> loop kept going until the True condition was met, which occurred once x==10. It's important to note that once this occurred the code stopped. Let's see how we could add an <code>else</code> statement:

# # break, continue, pass
# 
# We can use <code>break</code>, <code>continue</code>, and <code>pass</code> statements in our loops to add additional functionality for various cases. The three statements are defined by:
# 
#     break: Breaks out of the current closest enclosing loop.
#     continue: Goes to the top of the closest enclosing loop.
#     pass: Does nothing at all.
#     
#     
# Thinking about <code>break</code> and <code>continue</code> statements, the general format of the <code>while</code> loop looks like this:
# 
#     while test: 
#         code statement
#         if test: 
#             break
#         if test: 
#             continue 
#     else:
# 
# <code>break</code> and <code>continue</code> statements can appear anywhere inside the loop’s body, but we will usually put them further nested in conjunction with an <code>if</code> statement to perform an action based on some condition.
# 
# Let's go ahead and look at some examples!

# In[ ]:


x = 0

while x < 10:
    print('x is currently: ',x)
    print(' x is still less than 10, adding 1 to x')
    x+=1
    if x==3:
        print('Breaking because x==3')
        break
    else:
        print('continuing...')
        continue


# Note how the other <code>else</code> statement wasn't reached and continuing was never printed!
# 
# After these brief but simple examples, you should feel comfortable using <code>while</code> statements in your code.
# 
# **A word of caution however! It is possible to create an infinitely running loop with <code>while</code> statements. For example:**

# In[ ]:


# DO NOT RUN THIS CODE!!!! 
while True:
    print("I'm stuck in an infinite loop!")


# A quick note: If you *did* run the above cell, click on the Kernel menu above to restart the kernel!

# # Useful Operators
# 
# There are a few built-in functions and "operators" in Python that don't fit well into any category, so we will go over them in this lecture, let's begin!

# ## range
# 
# The range function allows you to quickly *generate* a list of integers, this comes in handy a lot, so take note of how to use it! There are 3 parameters you can pass, a start, a stop, and a step size. Let's see some examples:

# In[ ]:


range(0,11)


# Note that this is a **generator** function, so to actually get a list out of it, we need to cast it to a list with **list()**. What is a generator? Its a special type of function that will generate information and not need to save it to memory. We haven't talked about functions or generators yet, so just keep this in your notes for now, we will discuss this in much more detail in later on in your training!

# In[ ]:


# Notice how 11 is not included, up to but not including 11, just like slice notation!
list(range(0,11))


# In[ ]:


list(range(0,12))


# In[ ]:


# Third parameter is step size!
# step size just means how big of a jump/leap/step you 
# take from the starting number to get to the next number.

list(range(0,11,2))


# In[ ]:


list(range(0,101,10))


# ## For Loop with range( )

# In[ ]:


for i in range(0,11):
    print(i**2)


# ## in operator
# 
# We've already seen the **in** keyword durng the for loop, but we can also use it to quickly check if an object is in a list

# In[ ]:


'x' in ['x','y','z']


# In[ ]:


'x' in [1,2,3]


# ## min and max
# 
# Quickly check the minimum or maximum of a list with these functions.

# In[ ]:


mylist = [10,20,30,40,100]


# In[ ]:


min(mylist)


# In[ ]:


max(mylist)


# ## input ( )

# In[ ]:


input('Enter Something into this box: ')


# In[ ]:


# finding area of a rectangle 
length = input('Enter the length: ')
width = input('Enter the width: ')
area = length * width
print('The area is: ', area)


# # List Comprehensions
# 
# In addition to sequence operations and list methods, Python includes a more advanced operation called a list comprehension.
# 
# List comprehensions allow us to build out lists using a different notation. You can think of it as essentially a one line <code>for</code> loop built inside of brackets. For a simple example:
# ## Example 1

# In[ ]:


# Creating a list of odd numbers between 7 and 200 - The Long Way
lst = []
for x in range(7, 200, 2):
    lst.append(x)
print(lst)


# In[ ]:


# Creating a list of odd numbers between 7 and 200 - The Short Way
lst = [x for x in range(7, 200, 2)]
print(lst)


# ## Example 2

# In[ ]:


# Grab every letter in string
lst = [x for x in 'word']


# In[ ]:


# Check
lst


# This is the basic idea of a list comprehension. If you're familiar with mathematical notation this format should feel familiar for example: x^2 : x in { 0,1,2...10 } 
# 
# Let's see a few more examples of list comprehensions in Python:
# ## Example 3

# In[ ]:


# Square numbers in range and turn into list
lst = [x**2 for x in range(11)]


# In[ ]:


lst


# ## Example 4
# Let's see how to add in <code>if</code> statements:

# In[ ]:


# Check for even numbers in a range
lst = [x for x in range(11) if x % 2 == 0]


# In[ ]:


lst


# ## Example 5
# Can also do more complicated arithmetic:

# In[ ]:


# Convert Celsius to Fahrenheit
celsius = [0,10,20.1,34.5]

fahrenheit = [((9/5)*temp + 32) for temp in celsius ]

fahrenheit

