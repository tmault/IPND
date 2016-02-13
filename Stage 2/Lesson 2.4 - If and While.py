# Lesson 2.4: Making Decisions - If Statements

# We'll often write programs that need to make comparisons between values.
# We can do comparisons just like we do in math with the < and > signs.
# We can also do equality comparisons with != (not equal) and ==.
# Comparisons always return a Boolean value (either True or False).

# https://www.udacity.com/course/viewer#!/c-nd000/l-4196788670/e-48727556/m-48724313

print 2 < 3 #True
print 21 < 3 #False
print 7 * 3 < 21
print 7 * 3 != 21
print 7 * 3 == 21

# Add your own code and notes here

# A boolean value is output as either True or False.



# Define a procedure, is_friend, that
# takes a string as its input, and
# returns a Boolean indicating if
# the input string is the name of
# a friend. Assume I am friends with
# everyone whose name starts with D
# and no one else. You do not need to
# check for the lower case 'd'


def is_friend(a):
    if a[:1] == 'D':
        return True
    else:
        return False





print is_friend('Diane')
#>>> True

print is_friend('Fred')
#>>> False



# Define a procedure, is_friend, that takes
# a string as its input, and returns a
# Boolean indicating if the input string
# is the name of a friend. Assume
# I am friends with everyone whose name
# starts with either 'D' or 'N', but no one
# else. You do not need to check for
# lower case 'd' or 'n'

def is_friend(a):
    if a[0] == 'D':
        return True
    if a[0] == 'N':
        return True
    else:
        return False



print is_friend('Diane')
#>>> True

print is_friend('Ned')
#>>> True

print is_friend('Moe')
#>>> False





# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def biggest(a, b, c):
    
    if a > b and a > c:
        return a 
    
    if b > c and b > a:
        return b

    if c > a and c > b:
        return c
    
    else:
        if a == b or b == c:
            return b


    



print biggest(2, 2, 1)
#>>> 9

print biggest(6, 9, 3)
#>>> 9

print biggest(9, 3, 6)
#>>> 9

print biggest(3, 3, 9)
#>>> 9

#print biggest(9, 3, 9)
#>>> 9


# Procedures, simple arithmetic (comparisons) and if statements can build anything.