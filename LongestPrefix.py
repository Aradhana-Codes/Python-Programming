"""Find the longest common prefix among a list of strings.
   Example: input: ["flower", "flow", "flight"]
            output: "fl"
"""
words=["flower","flow","flight"]
prefix=words[0]


for word in words[1:]:
    print("For checking with",word,":","\nPrefixes:")
    while not word.startswith(prefix):
        prefix=prefix[:-1]
        print(prefix)

        if prefix=="":
            break

print("The longest common prefix:", prefix)



"""
step   word   prefix             startswith()       Action             prefix
              before check                                             after

start   -      flower             -                  Initial prefix     flower

1      flow    flower             false              Remove last char   flowe

2      flow    flowe              false              Remove last char   flow

3      flow    flow               true               Stop while         flow

4      flight  flow               false              Remove last char   flo

5      flight  flo                false              Remove last char   fl   

6      flight  fl                 true               Stop while          fl


"""