"""
Find the largest and second largest elements in a list.
Example: input: [10,25,7,45,18]
         output: 
         Largest element: 45
         Second largest element: 25
"""

numbers=[10,25,7,45,18]

largest=numbers[0]
second_largest=numbers[0]

for number in numbers:
    if number>largest:
        second_largest=largest
        largest=number
    elif number>second_largest and number!=largest:
        second_largest=number
print("Largest element:",largest)
print("Second largest element:",second_largest)
