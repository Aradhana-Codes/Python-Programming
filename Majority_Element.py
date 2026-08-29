"""
Find the element that appears more then n/2 times in 
a list.

Example: input: [2,2,1,1,1,2,2]
         output: 2
"""
numbers=[2,2,1,1,1,2,2]

frequency={}

for number in numbers:
    frequency[number]=frequency.get(number,0)+1

majority_element=None

for number, count in frequency.items():
    if count>len(numbers)//2:
        majority_element=number
        break

print("Majority element:",majority_element)