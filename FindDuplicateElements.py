"""
Find all duplicate elements in a list.
Example: input: [1,2,2,3,4,4,5,5]
         output: [2,4,5]
"""
numbers=[1,2,2,3,4,4,5,5]

seen=set()
duplicates=[]

for number in numbers:
    if number in seen:
        if number not in duplicates:
            duplicates.append(number)
    else:
        seen.add(number)

print("Duplicate elements:",duplicates)

