##Write a method that, efficiently with respect to time used, finds the
## n-th lowest selling book in the list. Each element of the sales list represent
## a single sale of a book with that book's id. The n-th lowest
## selling book is the book that has more sales than n-1 books. 
## Assume that book sales counts are unique.

##For example, nth_lowest_selling(5,4,3,2,1,5,4,3,2,5,4,3,5,4,5],2) 
## should return 2. In the list, the book with the id 1 was sold once, id 2 twice,
## id 3 three times, id 4 four times and id 5 five times, making the 
## book with the id 1 the lowest selling book in the array and id 2 the 
## second lowest selling book

from collections import Counter

def nth_lowest_selling(sales, n):
    """
    :param elements: (list) List of book sales.
    :param n: (int) The n-th lowest selling element the function should return.
    :returns: (int) The n-th lowest selling book id in the book sales list.
    """
    s=set(sales)
    if(len(s)==0 or len(s)<n or n==0):return ("Wrong Input")
    c = Counter(sales)
    com=c.most_common()
    return com[-n][0]

print(nth_lowest_selling([5, 4, 3, 2, 1, 5, 4, 3, 2, 5, 4, 3, 5, 4, 5], 2))