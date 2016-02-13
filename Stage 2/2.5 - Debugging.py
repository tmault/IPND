# A small change will fix the crashing bug in printInches.

def printExample(a, b):
    print a + b
    
def printInches(n):
    print str(n) + " inches" #added to convert n to a string, can't concatenate a string and integer.

# Don't change the function calls on lines 10 - 12.
printExample(17, 23)
printExample('long', 'word')
printInches(42)



#We went over 5 debugging strategies in this lesson.

#Examine error messages when programs crash

#The last line of Python Tracebacks will tell you what went wrong. Reading backwards from there will tell you more about where the problem occurred.

#Work from example code

#If your modified code doesn't work, comment it out and do step-by-step modifications to the example code until it does what you want.

#Make sure examples work

#Just because you find example code doesn't mean it will work in your system. Check the example code you're using to make sure it behaves the way you expect.

#Check (print) intermediate results

#When your code doesn't crash, but doesn't behave as expected, add print statements to your program to see where in the code things stop behaving correctly.

#Keep and compare old versions

#When you have a working version of your code, save it before you add to the code. This will give you something to go back to if you introduce too many new bugs.