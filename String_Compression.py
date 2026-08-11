"""
Compress a string by replacing consecutive repeated characters 
with the character followed by its count.

Example: input: "aaabbcccc"
         output: "a3b2c4"
"""
text="aaabbcccc"

compressed=""
count=1

for i in range(1,len(text)):
    if text[i]==text[i-1]:
        count+=1
    else:
        compressed+=text[i-1]+str(count)
        count=1
compressed+=text[-1]+str(count)
print("Compressed string:",compressed)

"""
character positions:
character: a a a b b c c c c
index:     0 1 2 3 4 5 6 7 8

compressed=""
count=1 because we start with the first character "a".

Step   current  previous  same?  count   compresssed
start   a                          1      ""
1       a         a        yes     2      ""
2       a         a        yes     3      ""
3       b         a        No      1       a3
4       b         b        yes     2       a3
5       c         b        No      1       a3b2
6       c         c        yes     2       a3b2
7       c         c        yes     3       a3b2
8       c         c        yes     4       a3b2
End                                4       a3b2c4


"""