"""
Find the missing number from a list containing numbers 
from 1 to n.
Example: input: [1,2,3,5,6]
         output: 4
"""
numbers=[1,2,3,5,6]
n=len(numbers)+1

expected_sum=n*(n+1)//2
actual_sum=0

for number in numbers:
    actual_sum+=number

missing_number=expected_sum-actual_sum

print("Missing number:",missing_number)

"""
numbers=[1,2,3,5,6] -> len(numbers)=5 -> n=5+1=6 -> Expected numbers: 1 to 6 -> expected_sum=21 -> Calculate actual sum -> 1+2+3+5+6 -> actual_sum=17 -> 21-17=4 -> missingnumber=4
"""