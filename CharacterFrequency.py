"""
Question: Count the frequency of every character in a string.

Example: input: "programming"

         output:
         p: 1
         r: 2
         o: 1
         g: 2
         a: 1
         m: 2
         i: 1
         n: 1
"""

text = "programming"

frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) + 1

for char, count in frequency.items():
    print(char, ":", count)