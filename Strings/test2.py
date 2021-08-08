def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
          
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    con = []
    for i, n in enumerate(doc_list):
        tmp = n.split()
        tmp2 = [u.rstrip('.,').lower() for u in tmp]
        if keyword.lower() in tmp2:
            con.append(i)
    return con

def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    con = {}
    n = 0
    while n < len(keywords):
        con[keywords[n]] = word_search(doc_list, keywords[n])
        n += 1
    return con
    
doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
keywords = ['casino', 'they']

print(multi_word_search(doc_list, keywords))

