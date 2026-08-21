"""
Remove duplicate elements from a list while 
keeping the first occurrence of each element.

Example:input: [1,2,2,3,4,4]
        output: [1,2,3,4]
"""
numbers=[1,2,2,3,4,4]
result=[]
seen=set()

for number in numbers:
    if number not in result:
        result.append(number)
        #seen.add(number)

print("After removing duplicates:",result)