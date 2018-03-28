"""
  Program to print Fibonacci sequence
  Programmed by : Ryan Mehra
  Date : 27 March 2018

"""

# This function takes input argument as
# length of fibonacci sequence, further
# computes fibonacci sequence.
def fibSequence():

    numloops = input("Gimme Size of Fibonacci Sequence : ")
    oldNum1 = 0
    oldNum2 = 1
    newNum = 0

    print(oldNum1)
    print(oldNum2)

    for x in range (1,numloops):
        newNum = oldNum1 + oldNum2

        print(newNum)

        oldNum1 = oldNum2
        oldNum2 = newNum

# Call fibonacci sequence function
fibSequence()
