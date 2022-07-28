import pandas as pd
import numpy as np
import dask.dataframe as dd
import re
import psutil
import gc
from collections import Counter

#범주화 판별
def categorical_validation(data):
    data_tmp = Counter(data)
    
    if len(data_tmp) >= (len(data)/2):
        return 'non_category'
    else:
        return 'category'

#데이터 메모리 소모 최소화
def mem_min(data_path):
    data = dd.read_csv(data_path)
    data_dtypes = data.dtypes.apply(lambda x: x.name).to_dict()
    
    for i, e in data_dtypes.items():
        data_tmp = pd.read_csv(data_path, usecols=[i])
        if 'int' in e or 'float' in e:
            tmp_max = data_tmp.max()[0]
            tmp_min = data_tmp.min()[0]
            if 'int' in e:
                if tmp_min >= 0 and tmp_max <= 255:
                    data_dtypes[i] = 'uint8'
                elif tmp_min >= 0 and tmp_max <= 65535:
                    data_dtypes[i] = 'uint16'
                elif tmp_min >= 0 and tmp_max <= 4294967295:
                    data_dtypes[i] = 'uint32'
                elif tmp_min >= 0 and tmp_max <= 18446744073709551615:
                    data_dtypes[i] = 'uint64'
                elif tmp_min >= -128 and tmp_max <= 127:
                    data_dtypes[i] = 'int8'
                elif tmp_min >= -32768 and tmp_max <= 32767:
                    data_dtypes[i] = 'int16'
                elif tmp_min >= -2147483648 and tmp_max <= 2147483647:
                    data_dtypes[i] = 'int32' 
                else:
                    continue
            else:
                continue
        elif (e == 'bool') or ('dataetime' in e) or (e == 'timedelta'):
            continue
        else:
            if categorical_validation(data_tmp[i]) == 'non_category':
                data_dtypes[i] = 'object'
            else:
                data_dtypes[i] = 'category'
        del [[data_tmp]]
        gc.collect()

    return data_dtypes