"""
Question: Reverse a string without using a built-in reverse function.

Example: input: "python"
         output: "nohtyp"
"""
text="python"
reversed_text=""

for char in text:
    reversed_text=char+reversed_text

print("Reversed string:", reversed_text)

