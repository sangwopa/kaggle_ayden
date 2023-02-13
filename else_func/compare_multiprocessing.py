import time
import datetime
import pandas as pd
import numpy as np
import seaborn as sns
import multiprocessing
from multiprocessing import Pool

file_path = r'C:\Users\User\Documents\test_data_gen\original_data.csv'

def pandas_read_csv(file_path):
    data = pd.read_csv(file_path)
    
    return data
    

start = time.time()

data1 = pandas_read_csv(file_path)

tmp_time = time.time() - start

print(tmp_time)

num_cores = multiprocessing.cpu_count()

#병렬처리
def parallelize_dataframe(df, func):
    df_split = np.array_split(df, num_cores)
    pool = Pool(num_cores)
    df = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return df

