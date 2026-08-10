"""
Question: Check whether two strings are anagrams of each other.
Two strings are anagrams if they contain the same characters with
the same frequency.

Example: input: "listen"
                "silent"

        output: True
"""

text1="listen"
text2="silent"
frequency1={}
frequency2={}

for char in text1:
    frequency1[char]=frequency1.get(char,0)+1

for char in text2:
    frequency2[char]=frequency2.get(char,0)+1

if frequency1==frequency2:
    print("Valid Anagram:",True, frequency1,frequency2)
else:
    print("Valid Anagram:",False)