import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Timer Complete.')

t = input("Enter the time in seconds: ")

countdown(int(t))

## Commentary
"""
Line 1:
    Because this is a countdown program, the required time library is imported. 

line 3:
    A function is defined to hold the syntax of the block of code that would hold
    the time syntax.
    
Line 5-9:
    I do not understand much of the code used in the area, I get that it's part of
    the syntax required to successfully run the program. If you need to understand
    this, I recommend you read about the time python library online. I'll be doing 
    same after this. 

Line 10:
    The print statement emphasizes that the program is done. This is optional. 

Line 12:
    The user input for the time countdown function is collected here. 
    
Line 14: 
    The countdown function is called, the input from the user is passed as an argument
    to the function. But it is first parsed as an integer since user inputs are always
    captured as strings. 
"""