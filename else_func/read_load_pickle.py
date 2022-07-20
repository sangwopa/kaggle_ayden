import pickle

def save_pickle(dict, path):
    
    with open(path+"_colinfo.pkl", "wb") as output:
        pickle.dump(dict, output)
        
def open_pickle(path):
    
    with open(path, "wb") as output:
        dict = pickle.load(output)
    
    return dict