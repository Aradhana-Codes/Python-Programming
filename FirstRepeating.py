"""
Find the first character that appears more than once in a given 
string.
Example: input: "pythonprogrammig"
         output: "p"
"""
text="pythonprogramming"

seen=set()

for char in text:
    if char in seen:
        print("First repeating character:",char)
        break

    seen.add(char)