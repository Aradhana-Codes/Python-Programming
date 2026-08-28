"""
Find the maximum difference between two elements
where the larger element comes after the smaller element.
Example: input: [7,1,5,3,6,4]
         output: 5

Explanation:
The maximum difference is 6-1=5.

"""
numbers=[7,1,5,3,6,4]

smallest=numbers[0]
max_difference=0

for number in numbers:
    if number<smallest:
        smallest=number
    difference=number-smallest

    if difference>max_difference:
        max_difference=difference
print("Maximum difference:",max_difference)








"""
Step         number       smallest          Is number        smallest        difference     max_difference
                           before            smaller?        after

 1            7             7                no                7              7-7=0          0

 2            1             7                yes               1              1-1=0          0             

 3            5             1                no                1              5-1=4          4

 4            3             1                no                1              3-1=2          4

 5            6             1                no                1              6-1=5          5

 6            4             1                no                1              4-1=3          5

"""