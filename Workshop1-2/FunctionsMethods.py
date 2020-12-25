#!/usr/bin/env python
# coding: utf-8

# # Methods
# 
# We've already seen a few example of methods when learning about Object and Data Structure Types in Python. Methods are essentially functions built into objects. Later on in the course we will learn about how to create our own objects and methods using Object Oriented Programming (OOP) and classes.
# 
# Methods perform specific actions on an object and can also take arguments, just like a function. This lecture will serve as just a brief introduction to methods and get you thinking about overall design methods that we will touch back upon when we reach OOP in the course.
# 
# Methods are in the form:
# 
#     object.method(arg1,arg2,etc...)
#     
# You'll later see that we can think of methods as having an argument 'self' referring to the object itself. You can't see this argument but we will be using it later on in the course during the OOP lectures.
# 
# Let's take a quick look at what an example of the various methods a list has:

# In[ ]:


# Create a simple list
lst = [1,2,3,4,5]


# Fortunately, with iPython and the Jupyter Notebook we can quickly see all the possible methods using the tab key. The methods for a list are:
# 
# * append
# * count
# * extend
# * insert
# * pop
# * remove
# * reverse
# * sort
# 
# Let's try out a few of them:

# append() allows us to add elements to the end of a list:

# In[ ]:


lst.append(6)


# In[ ]:


lst


# Great! Now how about count()? The count() method will count the number of occurrences of an element in a list.

# In[ ]:


# Check how many times 2 shows up in the list
lst.count(2)


# You can always use Shift+Tab in the Jupyter Notebook to get more help about the method. In general Python you can use the help() function: 

# In[ ]:


help(lst.count)


# Feel free to play around with the rest of the methods for a list. Later on in this section your quiz will involve using help and Google searching for methods of different types of objects!

# Great! By this lecture you should feel comfortable calling methods of objects in Python!

# # Functions
# 
# ## Introduction to Functions
# 
# This lecture will consist of explaining what a function is in Python and how to create one. Functions will be one of our main building blocks when we construct larger and larger amounts of code to solve problems.
# 
# **So what is a function?**
# 
# Formally, a function is a useful device that groups together a set of statements so they can be run more than once. They can also let us specify parameters that can serve as inputs to the functions.
# 
# On a more fundamental level, functions allow us to not have to repeatedly write the same code again and again. If you remember back to the lessons on strings and lists, remember that we used a function len() to get the length of a string. Since checking the length of a sequence is a common task you would want to write a function that can do this repeatedly at command.
# 
# Functions will be one of most basic levels of reusing code in Python, and it will also allow us to start thinking of program design (we will dive much deeper into the ideas of design when we learn about Object Oriented Programming).

# ## def Statements
# 
# Let's see how to build out a function's syntax in Python. It has the following form:

# In[ ]:


def name_of_function(arg1,arg2):
    '''
    This is where the function's Document String (docstring) goes
    '''
    # Do stuff here
    # Return desired result


# We begin with <code>def</code> then a space followed by the name of the function. Try to keep names relevant, for example len() is a good name for a length() function. Also be careful with names, you wouldn't want to call a function the same name as a [built-in function in Python](https://docs.python.org/2/library/functions.html) (such as len).
# 
# Next come a pair of parentheses with a number of arguments separated by a comma. These arguments are the inputs for your function. You'll be able to use these inputs in your function and reference them. After this you put a colon.
# 
# Now here is the important step, you must indent to begin the code inside your function correctly. Python makes use of *whitespace* to organize code. Lots of other programing languages do not do this, so keep that in mind.
# 
# Next you'll see the docstring, this is where you write a basic description of the function. Using iPython and iPython Notebooks, you'll be able to read these docstrings by pressing Shift+Tab after a function name. Docstrings are not necessary for simple functions, but it's good practice to put them in so you or other people can easily understand the code you write.
# 
# After all this you begin writing the code you wish to execute.
# 
# The best way to learn functions is by going through examples. So let's try to go through examples that relate back to the various objects and data structures we learned about before.

# ### Example 1: A simple print 'hello' function

# In[ ]:


def say_hello():
    print('hello')


# Call the function:

# In[ ]:


say_hello()


# ### Example 2: A simple greeting function
# Let's write a function that greets people with their name.

# In[ ]:


def greeting(name):
    print('Hello', name)


# In[ ]:


greeting('Bob')


# ## Using return
# Let's see some example that use a <code>return</code> statement. <code>return</code> allows a function to *return* a result that can then be stored as a variable, or used in whatever manner a user wants.
# 
# ### Example 3: Addition function

# In[ ]:


def add_num(num1,num2):
    return num1+num2


# In[ ]:


add_num(4,5)


# In[ ]:


# Can also save as variable due to return
result = add_num(4,5)


# In[ ]:


print(result)


# Note that because we don't declare variable types in Python, this function could be used to add numbers or sequences together! We'll later learn about adding in checks to make sure a user puts in the correct arguments into a function.
# 
# Let's also start using <code>break</code>, <code>continue</code>, and <code>pass</code> statements in our code. We introduced these during the <code>while</code> discussion.

# ## Example 4: Catching Primes
# Finally let's go over a full example of creating a function to check if a number is prime (a common interview exercise).
# 
# We know a number is prime if that number is only evenly divisible by 1 and itself. Let's write our first version of the function to check all the numbers from 1 to N and perform modulo checks.

# In[ ]:


def is_prime(num):
    '''
    Naive method of checking for primes. 
    '''
    for n in range(2,num):
        if num % n == 0:
            print(num,'is not prime')
            break
    else: # If never mod zero, then prime
        print(num,'is prime!')


# In[ ]:


is_prime(160)


# In[ ]:


is_prime(173)


# Note how the <code>else</code> lines up under <code>for</code> and not <code>if</code>. This is because we want the <code>for</code> loop to exhaust all possibilities in the range before printing our number is prime.
# 
# Also note how we break the code after the first print statement. As soon as we determine that a number is not prime we break out of the <code>for</code> loop.

# # Nested Statements and Scope 
# 
# Now that we have gone over writing our own functions, it's important to understand how Python deals with the variable names you assign. When you create a variable name in Python the name is stored in a *name-space*. Variable names also have a *scope*, the scope determines the visibility of that variable name to other parts of your code.
# 
# Let's start with a quick thought experiment; imagine the following code:

# In[ ]:


x = 25

def printer():
    x = 50
    return x

print(printer())
print(x)


# What do you imagine the output of printer() is? 25 or 50? What is the output of print x? 25 or 50?

# In[ ]:


print(x)


# In[ ]:


print(printer())


# ## Local Variables
# When you declare variables inside a function definition, they are not related in any way to other variables with the same names used outside the function - i.e. variable names are local to the function. This is called the scope of the variable. All variables have the scope of the block they are declared in starting from the point of definition of the name.
# 
# Example:

# In[ ]:


x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)

func(x)
print('x is still', x)


# The first time that we print the value of the name **x** with the first line in the function’s body, Python uses the value of the parameter declared in the main block, above the function definition.
# 
# Next, we assign the value 2 to **x**. The name **x** is local to our function. So, when we change the value of **x** in the function, the **x** defined in the main block remains unaffected.
# 
# With the last print statement, we display the value of **x** as defined in the main block, thereby confirming that it is actually unaffected by the local assignment within the previously called function.
# 
# ## The <code>global</code> statement
# If you want to assign a value to a name defined at the top level of the program (i.e. not inside any kind of scope such as functions or classes), then you have to tell Python that the name is not local, but it is global. We do this using the <code>global</code> statement. It is impossible to assign a value to a variable defined outside a function without the global statement.
# 
# You can use the values of such variables defined outside the function (assuming there is no variable with the same name within the function). However, this is not encouraged and should be avoided since it becomes unclear to the reader of the program as to where that variable’s definition is. Using the <code>global</code> statement makes it amply clear that the variable is defined in an outermost block.
# 
# Example:

# In[ ]:


x = 50

def func():
    global x
    print('This function is now using the global x!')
    print('Because of global x is: ', x)
    x = 2
    print('Ran func(), changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x (outside of func()) is: ', x)


# The <code>global</code> statement is used to declare that **x** is a global variable - hence, when we assign a value to **x** inside the function, that change is reflected when we use the value of **x** in the main block.
# 
# You can specify more than one global variable using the same global statement e.g. <code>global x, y, z</code>.
