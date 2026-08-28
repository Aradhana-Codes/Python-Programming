"""
Move all zeros to the end of a list while keeping 
the order of the non-zero elements unchanged.
Example: input: [0,1,0,3,12]
         output: [1,3,12,0,0]
"""
numbers=[0,1,0,3,12]
result=[]

zero_count=0

for number in numbers:
    if number==0:
        zero_count+=1

    else:
        result.append(number)

for i in range(zero_count):
    result.append(0)

print("After moving zeroes:",result)