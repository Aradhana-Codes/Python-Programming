"""Find the longest word in a given sentence.
Example: input: "Python is powerful"
         output: "powerful"
"""

text="Python is powerful"

words=text.split()
print(words)

longest_word=""

for word in words:
    if len(word)>len(longest_word):
        longest_word=word

print("Longest word:",longest_word)