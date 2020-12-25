#!/usr/bin/env python
# coding: utf-8

# # Numbers in Python!
# 
# Here, we will learn about numbers in Python and how to use them.

# ## Types of numbers
# 
# Python has various "types" of numbers (numeric literals). We'll mainly focus on integers and floating point numbers.
# 
# ### Integers 
# are just whole numbers, positive or negative. For example: 2 and -2 are examples of integers.
# 
# ### Floating point numbers 
# in Python are notable because they have a decimal point in them, or use an exponential (e) to define the number. 
# 
# For example 2.0 and -2.1 are examples of floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating point number in Python.

# ## Comments
# Any line starting with a hash character '#' is a comment and is ignored by the Python interpreter.

# ### Basic Arithmetic

# In[ ]:


# Addition
2+1


# In[ ]:


# Subtraction
2-1


# In[ ]:


# Multiplication
2*2


# In[ ]:


# Division
3/2


# In[ ]:


# Modulo
7%4


# 4 goes into 7 once, with a remainder of 3. The % operator returns the remainder after division.

# In[ ]:


# Powers
2**3


# In[ ]:


# Order of Operations followed in Python
2 + 10 * 10 + 3


# In[ ]:


# Can use parentheses to specify orders
(2+10) * (10+3)


# ## Variable Basics
# 
# Variables hold data. Data can be assigned using the '=' operator.

# In[ ]:


# Let's create an object called "a" and assign it the number 5
x = 5


# Now if I call *a* in my Python script, Python will treat it as the number 5.

# In[ ]:


# Adding the objects
x+x


# What happens on reassignment? Will Python let us write it over?

# In[ ]:


# Reassignment
x = 10.1


# In[ ]:


# Check
x


# In[ ]:


# Use A to redefine A
x = x + x


# In[ ]:


# Check 
x


# The names you use when creating these labels need to follow a few rules:
# 
#     1. Names can not start with a number.
#     2. There can be no spaces in the name, use _ instead.
#     3. Can't use any of these symbols :'",<>/?|\()!@#$%^&*~-+
#     4. It's considered best practice that names are lowercase.
#     5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), 
#        or 'I' (uppercase letter eye) as single character variable names.
#     6. Avoid using words that have special meaning in Python like "list" and "str"
# 
# 
# Using variable names can be a very useful way to keep track of different variables in Python. For example:

# In[ ]:


# Use object names to keep better track of what's going on in your code!
my_income = 100

tax_rate = 0.1

my_taxes = my_income*tax_rate


# In[ ]:


# Show my taxes!
my_taxes


# # Strings

# Strings are used in Python to record text information, such as names. Python understands the string "hello' to be a sequence of letters in a specific order. This means we will be able to use indexing to grab particular letters (like the first letter, or the last letter).

# ## Creating a String
# To create a string in Python you need to use either single quotes or double quotes. For example:

# In[ ]:


# Single word
'hello'


# In[ ]:


# Be careful with quotes!
' I'm using single quotes, but this will create an error'


# The reason for the error above is because the single quote in <code>I'm</code> stopped the string. You can use combinations of double and single quotes to get the complete statement.

# In[ ]:


"Now I'm ready to use the single quotes inside a string!"


# ## Printing a String
# 
# Using Jupyter notebook with just a string in a cell will automatically output strings, but the correct way to display strings in your output is by using a print function.

# In[ ]:


# We can simply declare a string
'Hello World'


# We can use a print statement to print a string.

# In[ ]:


print('Hello World')
print('Hello \n World')


# In[ ]:


# print should be used when displaying any variable
x = "Python"
y = 3.7
print(x)
print(y)
print(x, y)


# ## String Basics

# We can also use a function called len() to check the length of a string!

# In[ ]:


len('Hello World')


# Python's built-in len() function counts all of the characters in the string, including spaces and punctuation.

# ## String Indexing
# We know strings are a sequence, which means Python can use indexes to call parts of the sequence. Let's learn how this works.
# 
# In Python, we use brackets <code>[]</code> after an object to call its index. We should also note that indexing starts at 0 for Python. Let's create a new object called <code>s</code> and then walk through a few examples of indexing.

# In[ ]:


# Assign s as a string
s = 'Hello World'


# In[ ]:


# Print the object
print(s) 


# Let's start indexing!

# In[ ]:


# Show first element (in this case a letter)
s[0]


# In[ ]:


s[1]


# In[ ]:


s[2]


# We can use a <code>:</code> to perform *slicing* which grabs everything up to a designated point. For example:

# In[ ]:


# Grab everything past the first term all the way to the length of s which is len(s)
s[1:]


# In[ ]:


# Note that there is no change to the original s
s


# In[ ]:


# Grab everything UP TO the 3rd index
s[:3]


# Note the above slicing. Here we're telling Python to grab everything from 0 up to 3. It doesn't include the 3rd index. You'll notice this a lot in Python, where statements and are usually in the context of "up to, but not including".

# In[ ]:


#Everything in between including 0 index but not 5
s[0:5]


# ## String Properties
# It's important to note that strings have an important property known as *immutability*. This means that once a string is created, the elements within it can not be changed or replaced. For example:

# In[ ]:


# Let's try to change the first letter to 'x'
s[0] = 'x'


# In[ ]:


s


# In[ ]:


# Concatenate strings!
s + ' concatenate me!'


# In[ ]:


# We can reassign s completely though!
s = s + ' concatenate me!'


# In[ ]:


print(s)


# In[ ]:


s


# We can use the multiplication symbol to create repetition!

# In[ ]:


letter = 'z'


# In[ ]:


letter*10


# ## Basic Built-in String methods
# 
# Objects in Python usually have built-in methods. These methods are functions inside the object (we will learn about these in much more depth later) that can perform actions or commands on the object itself.
# 
# We call methods with a period and then the method name. Methods are in the form:
# 
# object.method(parameters)
# 
# Where parameters are extra arguments we can pass into the method. Don't worry if the details don't make 100% sense right now. Later on we will be creating our own objects and functions!
# 
# Here are some examples of built-in methods in strings:

# In[ ]:


s


# In[ ]:


# Upper Case a strings.upper()
s.upper()


# In[ ]:


# Lower case
s.lower()


# In[ ]:


# Split a string by blank space
s.split()


# In[ ]:


# Split a string by another character
s.split('o')


# In[ ]:


# Identify a number in a string
string = "3582"
string.isdigit()


# # Variable Types

# ## Dynamic Typing
# 
# Python uses *dynamic typing*, meaning you can reassign variables to different data types. This makes Python very flexible in assigning data types; it differs from other languages that are *statically typed*.

# ### Pros and Cons of Dynamic Typing
# #### Pros of Dynamic Typing
# * very easy to work with
# * faster development time
# 
# #### Cons of Dynamic Typing
# * may result in unexpected bugs!
# * you need to be aware of `type()`

# ## Determining variable type with `type()`
# You can check what type of object is assigned to a variable using Python's built-in `type()` function. Common data types include:
# * **int** (for integer)
# * **float**
# * **str** (for string)
# * **list**
# * **tuple**
# * **dict** (for dictionary)
# * **set**
# * **bool** (for Boolean True/False)

# In[ ]:


type(s)


# # Lists
# 
# Earlier when discussing strings we introduced the concept of a *sequence* in Python. Lists can be thought of the most general version of a *sequence* in Python. Unlike strings, they are mutable, meaning the elements inside a list can be changed!
# 
# Lists are constructed with brackets [] and commas separating every element in the list.

# In[ ]:


# Assign a list to an variable named my_list
my_list = [1,2,3]


# We just created a list of integers, but lists can actually hold different object types. For example:

# In[ ]:


my_list = ['A string',23,100.232,'o']


# Just like strings, the len() function will tell you how many items are in the sequence of the list.

# In[ ]:


len(my_list)


# ### Indexing and Slicing
# Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:

# In[ ]:


my_list = ['one','two','three',4,5]


# In[ ]:


# Grab element at index 0
my_list[0]


# In[ ]:


# Grab index 1 and everything past it
my_list[1:]


# In[ ]:


# Grab everything UP TO index 3
my_list[:3]


# We can also use + to concatenate lists, just like we did for strings.

# In[ ]:


my_list + ['new item']


# Note: This doesn't actually change the original list!

# In[ ]:


my_list


# You would have to reassign the list to make the change permanent.

# In[ ]:


# Reassign
my_list = my_list + ['add new item']


# In[ ]:


my_list


# We can also use the * for a duplication method similar to strings:

# In[ ]:


# Make the list double
my_list * 2


# ## Basic List Methods
# 
# If you are familiar with another programming language, you might start to draw parallels between arrays in another language and lists in Python. Lists in Python however, tend to be more flexible than arrays in other languages for a two good reasons: they have no fixed size (meaning we don't have to specify how big a list will be), and they have no fixed type constraint (like we've seen above).
# 
# Let's go ahead and explore some more special methods for lists:

# In[ ]:


# Create a new list
list1 = [1,2,3]


# Use the **append** method to permanently add an item to the end of a list:

# In[ ]:


# Append
list1.append('append me!')


# In[ ]:


# Show
list1


# Use **pop** to "pop off" an item from the list. By default pop takes off the last index, but you can also specify which index to pop off. Let's see an example:

# In[ ]:


# Pop off the 0 indexed item
list1.pop(0)


# In[ ]:


# Show
list1


# In[ ]:


# Assign the popped element, remember default popped index is -1
popped_item = list1.pop()


# In[ ]:


popped_item


# In[ ]:


# Show remaining list
list1


# It should also be noted that lists indexing will return an error if there is no element at that index. For example:

# In[ ]:


list1[100]


# We can use the **sort** method and the **reverse** methods to also effect your lists:

# In[ ]:


new_list = ['a','e','x','b','c']


# In[ ]:


#Show
new_list


# In[ ]:


# Use reverse to reverse order (this is permanent!)
new_list.reverse()


# In[ ]:


new_list


# In[ ]:


# Use sort to sort the list (in this case alphabetical order, but for numbers it will go ascending)
new_list.sort()


# In[ ]:


new_list


# ## Nesting Lists
# A great feature of of Python data structures is that they support *nesting*. This means we can have data structures within data structures. For example: A list inside a list.
# 
# Let's see how this works!

# In[ ]:


# Let's make three lists
lst_1=[1,2,3]
lst_2=[4,5,6]
lst_3=[7,8,9]

# Make a list of lists to form a matrix
matrix = [lst_1,lst_2,lst_3]


# In[ ]:


# Show
matrix


# We can again use indexing to grab elements, but now there are two levels for the index. The items in the matrix object, and then the items inside that list!

# In[ ]:


# Grab first item in matrix object
matrix[0]


# In[ ]:


# Grab second item of the first item in the matrix object
matrix[0][1]


# ## Booleans
# 
# Python  comes with Booleans (with predefined True and False displays that are basically just the integers 1 and 0). It also has a placeholder object called None. Let's walk through a few quick examples of Booleans (we will dive deeper into them later in this course).

# In[ ]:


# Set object to be a boolean
a = True


# In[ ]:


#Show
print(a)


# We can also use comparison operators to create booleans. We will go over all the comparison operators later on in the course.

# In[ ]:


# Output is boolean
1 > 2


# We can use None as a placeholder for an object that we don't want to reassign yet:

# In[ ]:


# None placeholder
b = None


# In[ ]:


# Show
print(b)


# Thats it! You should now have a basic understanding of Python objects and data structure types. Next, go ahead and do the assessment test!

# # Files
# 
# Python uses file objects to interact with external files on your computer. These file objects can be any sort of file you have on your computer, whether it be an audio file, a text file, emails, Excel documents, etc. Note: You will probably need to install certain libraries or modules to interact with those various file types, but they are easily available. (We will cover downloading modules later on in the course).
# 
# Python has a built-in open function that allows us to open and play with basic file types. First we will need a file though. 
# 
# You could run the following command to create a file in the same folder as this notebook. 

# In[ ]:


get_ipython().run_cell_magic('writefile', 'test.txt', 'Hello, this is a quick test file.')


# ## Python Opening a file
# 
# Let's being by opening the file test.txt that is located in the same directory as this notebook. For now we will work with files located in the same directory as the notebook or .py script you are using.
# 
# It is very easy to get an error on this step:

# In[ ]:


myfile = open('not_here.txt')


# To avoid this error,make sure your .txt file is saved in the same location as your notebook, to check your notebook location, use **pwd**:

# In[ ]:


pwd


# **Alternatively, to grab files from any location on your computer, simply pass in the entire file path. **
# 
# For Windows you need to use double \ so python doesn't treat the second \ as an escape character, a file path is in the form:
# 
#     myfile = open("C:\\Users\\YourUserName\\Home\\Folder\\myfile.txt")
# 
# For MacOS and Linux you use slashes in the opposite direction:
# 
#     myfile = open("/Users/YouUserName/Folder/myfile.txt")

# In[ ]:


# Open the text.txt we made earlier
my_file = open('test.txt')


# In[ ]:


# We can now read the file
my_file.read()


# In[ ]:


# But what happens if we try to read it again?
my_file.read()


# This happens because you can imagine the reading "cursor" is at the end of the file after having read it. So there is nothing left to read. We can reset the "cursor" like this:

# In[ ]:


# Seek to the start of file (index 0)
my_file.seek(0)


# In[ ]:


# Now read again
my_file.read()


# You can read a file line by line using the readlines method. Use caution with large files, since everything will be held in memory. We will learn how to iterate over large files later in the course.

# In[ ]:


# Readlines returns a list of the lines in the file
my_file.seek(0)
my_file.readlines()


# When you have finished using a file, it is always good practice to close it.

# In[ ]:


my_file.close()


# ## Writing to a File
# 
# By default, the `open()` function will only allow us to read the file. We need to pass the argument `'w'` to write over the file. For example:

# In[ ]:


# Add a second argument to the function, 'w' which stands for write.
# Passing 'w+' lets us read and write to the file

my_file = open('test.txt','w+')


# ### <strong><font color='red'>Use caution!</font></strong> 
# Opening a file with `'w'` or `'w+'` truncates the original, meaning that anything that was in the original file **is deleted**!

# In[ ]:


# Write to the file
my_file.write('This is a new line')


# In[ ]:


# Read the file
my_file.seek(0)
my_file.read()


# In[ ]:


my_file.close()  # always do this when you're done with a file


# ## Appending to a File
# Passing the argument `'a'` opens the file and puts the pointer at the end, so anything written is appended. Like `'w+'`, `'a+'` lets us read and write to a file. If the file does not exist, one will be created.

# In[ ]:


my_file = open('test.txt','a+')
my_file.write('\nThis is text being appended to test.txt')
my_file.write('\nAnd another line here.')


# In[ ]:


my_file.seek(0)
print(my_file.read())


# In[ ]:


my_file.close()


# # Comparison Operators 
# 
# In this lecture we will be learning about Comparison Operators in Python. These operators will allow us to compare variables and output a Boolean value (True or False). 
# 
# If you have any sort of background in Math, these operators should be very straight forward.
# 
# 

# Let's now work through quick examples of each of these.
# 
# #### Equal

# In[ ]:


2 == 2


# In[ ]:


'Python' == 'Snake'


# Note that <code>==</code> is a <em>comparison</em> operator, while <code>=</code> is an <em>assignment</em> operator.

# #### Not Equal

# In[ ]:


2 != 1


# In[ ]:


2 != 2


# #### Greater Than

# In[ ]:


2 > 1


# In[ ]:


2 > 4


# #### Less Than

# In[ ]:


2 < 4


# In[ ]:


2 < 1


# #### Greater Than or Equal to

# In[ ]:


2 >= 2


# In[ ]:


2 >= 1


# #### Less than or Equal to

# In[ ]:


2 <= 2


# In[ ]:


2 <= 4


# **Great! Go over each comparison operator to make sure you understand what each one is saying. But hopefully this was straightforward for you.**
# 
# Next we will cover chained comparison operators

# # Chained Comparison Operators
# 
# An interesting feature of Python is the ability to *chain* multiple comparisons to perform a more complex test. You can use these chained comparisons as shorthand for larger Boolean Expressions.
# 
# In this lecture we will learn how to chain comparison operators and we will also introduce two other important statements in Python: **and** and **or**.
# 
# Let's look at a few examples of using chains:

# In[ ]:


1<2 and 2<3


# The **and** is used to make sure two checks have to be true in order for the total check to be true. Let's see another example:

# In[ ]:


1<3 and 2>3


# It's important to note that Python is checking both instances of the comparisons. We can also use **or** to write comparisons in Python. For example:

# In[ ]:


1==2 or 2<3


# Note how it was true; this is because with the **or** operator, we only need one *or* the other to be true. Let's see one more example to drive this home:

# In[ ]:


1==1 or 100==1

