"""
Remove duplicate characters from a string while keeping the first occurrence
each character.
Example: input: "programming"
         output: "progamin"

"""
text="programming"
result=""
seen=set()

for char in text:
    if char not in seen:
        result+=char
        seen.add(char)

print("After removing duplicates:",result)