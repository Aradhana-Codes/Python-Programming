"""
Check whether a given string is a palindrome or not.
A palindrome reads the same from left to right and right to left.

Example: input: "madam"
        output: True
"""
from numpy import character


text="madam"
reversed_text=""

for char in text:
    reversed_text=char+reversed_text

if text==reversed_text:
    print("Palindrome:",True)
else:
    print("Palindrome:",False)