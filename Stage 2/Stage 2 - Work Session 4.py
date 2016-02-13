# Stage 2 - Work Session 4

# Define a procedure weekend which takes a string as its input, and
# returns the boolean True if it's 'Saturday' or 'Sunday' and False otherwise.

def weekend(day):
    while day == 'Saturday' or day == 'Sunday':
        return True
    else: 
        return False
    
print weekend('Monday')
#>>> False

print weekend('Saturday')
#>>> True

print weekend('July')
#>>> False