#!/usr/bin/env python3
"""Amazon  Company | AMorales
   Conditionals - TESTING"""

def main():

    score  = input (int ("What is your test score"))

    if (score <= 100 and score >= 90):
        print ("Your grade is: A")
    elif(score < 90 and score >=80):
        print ("Your grade is: B")
    else:
        print("Failed the test")
main()
