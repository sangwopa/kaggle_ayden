c = 'it\'s ok'

print(c)
print(len(c))

d = """hey"""

print(d)
print(len(d))

e = '\n'

print(e)
print(len(e))

def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    if len(zip_code) == 5 and str.isdigit(zip_code):
        return True
    else:
        return False

zip_code = '12345'

def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices
    
    

doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
word_search(doc_list, 'casino')
