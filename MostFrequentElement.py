"""
Find the element that appears most frequently in a list.
Example: input: [1,1,1,2,2,3,3]
         output: 1
"""
numbers=[1,1,1,2,2,3,3]

frequency={}

for number in numbers:
    frequency[number]=frequency.get(number,0)+1

most_frequent=None
highest_count=0

for number, count in frequency.items():
    if count>highest_count:
        highest_count=count
        most_frequent=number

print("Most frequent element:", most_frequent)