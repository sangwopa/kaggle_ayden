import pandas as pd
import pickle

def load(path):
    """Load a SDV instance from a given path.
    Args:
        path (str):
            Path from which to load the SDV instance.
    """
    with open(path, 'rb') as f:
        model = pickle.load(f)

        return model

file_path = r"C:\Users\user\Documents\data_generation\program\\"
file_name = "testing_file.csv"
save_name = "testing_file_model.pkl"

data = load(file_path + save_name)



print(data)