##Write the function to slice the tuple between the given start (inclusive) and end (exclusive) indexes,
## and join the resulting range of values as a comma delimited string.
##For example tuple_slice(1,4(76,34,13,64,12)) should return "34,13,64"


def tuple_slice(start,end,list):
    if(len(list)==0):
        return "Empty List"
    if(start<0 or end>len(list)):
        return "Wrong Index Selection"
    
    fs=""
    sep=","
    for i in range(start,end):
        if i==end-1:
            fs=fs+str(list[i])
        else:    
            fs=fs+str(list[i])+sep
    return(fs)

    
print(tuple_slice(1,4,(76,34,13,64,12)))