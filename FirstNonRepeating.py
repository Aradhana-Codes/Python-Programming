"""
Find the first character that appears only once in a given string.
Example: input:"aabbcddee"
         output:"c"
 """

text="aabbcddee"

frequency={}

for char in text:
    frequency[char]=frequency.get(char,0)+1
print(frequency)

for char in text:
    if frequency[char]==1:
        print("First non-repeating character:",char)
        break

