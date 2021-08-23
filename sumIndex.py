def find_two_sum(numbers, target_sum):
    """
    :param numbers: (list of ints) The list of numbers.
    :param target_sum: (int) The required target sum.
    :returns: (a tuple of 2 ints) The indices of the two elements whose sum is equal to target_sum
    """
   
    d = {}
    for i, number in enumerate(numbers):
        key = target_sum - number
        if key in d.keys():
            return d[key], i
        else:
            d[number] = i
    
    return None

        
    
if __name__ == "__main__":
    print(find_two_sum([3, 1, 5, 7, 5, 9], 10))

    #s1=None
    #s2=None
    #for i in range(0, len(numbers)):
    #    s1=i
    #    for j in range(0,len(numbers)):
    #        if(numbers[s1]+numbers[j]==target_sum and s1!=j ):
    #            s2=j
    #        if(s2)!=None:
    #            return s1,s2
    #if s2==None:
    #    return None