def top_n (items,  n):
    """ This is going to return the top items in an array in desc order.

    Args: 
        items (array): List or array-like object
        n (int) : num of items to return

    Return:
        array: top n items, in desc order

    Egs:
        >>> top_n([8,3,2,7,4], 3)
        [8,7,4]        
    """
    for i in range(n): #keep sorting until we know the top n items
        for j in range(len(items)-1-i):
            if items[j] > items[j+1]: # if this item is bigger than the next..
                items[j], items[j+1] = items[j+1], items[j] # swap the two!


    #get  last two items
    top_n = items[-n:]
    #return in desc order
    return top_n[::-1]           
