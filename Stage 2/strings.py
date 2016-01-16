# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4192698630/m-48700403

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Add your own code and notes here

# A string is just a sequence of characters surrounded by quotes. We can use 'single' or "double quotes". 
# The only requirement is that the start quote must be that same as the end quote.
# It doesn't matter if you use single or double quotes.
# We don't want variables to start with capital letters, it's just a convention.


# Lesson 2.2: Hello!!!

# Define a variable, name, and assign to it a string that is your name.

name = 'Tom Mault'
print 'Hello' + name + '!'

# You cannot concatenate (add) a string and a number. You can multiply a string by a number. This will replicate the string X times.


# Lesson 2.2.: Indexing Strings

# Write Python code that prints out Udacity (with a capital U), 
# given the definition of s below.

s = 'audacity'
u = s[1]
print u.upper() + s[2:] 


# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

print "Example 1: Finding substrings in a string"
print "test".find("te")
print "test".find("st")
print "test"[2:]

print "Example 2: Finding substrings in a string which is stored as a variable"
my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

print "Example 3: Printing out everything after a certain substring"
my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color # oops, this line prints out 'color: ' as well...
print favorite_color[7:] # this fixes it!

print "Example 4: Other interesting things about string.find()..."
print "text".find("text") # prints 0
print "text".find("Text") # prints -1
print "text".find("")     # prints 0
print "text".find(" ")    # prints -1  



# This segment is just a chance for you to play around with 
# finding strings within strings. Read through the code and 
# press Test Run to see what it does. Is there anything 
# interesting or unexpected?

print "Example 1: using find to print the second occurrence of a sub-string"
print "test".find("t") # I expect this to print 0
print "test".find("t", 1) # I expect this to print 3

print "Example 2: using a variable to store first location"
first_location = "test".find("t") # here we store the first location of "t"
print "test".find("t", first_location+1) # then we use that location to find the second occurrence.

print "Example 3: using find to get rid of exclamation marks!!"
example = "Wow! Python is great! Don't you think?"
first = example.find('!')
second = example.find('!', first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string # oops, I should probably replace the !s with periods
new_string = example[:first] +'.'+ example[first+1:second] +'.'+ example[second+1:]
print new_string