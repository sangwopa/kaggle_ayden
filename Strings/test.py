con = []
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
          
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    for i, n in enumerate(doc_list):
        tmp = n.split()
        tmp2 = [tmp.rstrip('.,').lower() for tmp in tmp]
        if keyword.lower() in tmp2:
            con.append(i)
        return con
    

doc_list=['The Learn Python Challenge Casino', 'They bought a car, and a horse', 'Casinoville?']
print(word_search(doc_list, 'car'))
