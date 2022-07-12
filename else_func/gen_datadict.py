import pandas as pd

file_path = ""

data = pd.read_csv(file_path)

dtypes = data.dtypes.apply(lambda x: x.name).to_dict()

for i, e in dtypes.items(): 
    if (e == 'object') or (e == 'bool'):
        dtypes[i] = 'category'
    elif 'int' in e:
        dtypes[i] = 'int'
    elif 'float' in e:
            dtypes[i] = 'float'
    else:
        dtypes[i] = 'category'
