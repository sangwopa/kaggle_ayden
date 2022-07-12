from scipy.stats import chisquare
from collections import Counter
from datetime import datetime
import pandas as pd

def get_frequencies(real, synthetic):
    
    f_obs, f_exp = [], []
    real, synthetic = Counter(real), Counter(synthetic)

    for value in real:
        f_obs.append(synthetic[value] / sum(synthetic.values()))  
        f_exp.append(real[value] / sum(real.values()))

    return f_obs, f_exp

def is_datetime(data):

    return (
        pd.api.types.is_datetime64_any_dtype(data)
        or isinstance(data, pd.Timestamp)
        or isinstance(data, datetime)
    )

#카이 제곱 검정
def cs_compute(real_data, synthetic_data):

    f_obs, f_exp = get_frequencies(real_data, synthetic_data)
    if len(f_obs) == len(f_exp) == 1:
        pvalue = 1.0
    else:
        _, pvalue = chisquare(f_obs, f_exp)

    return pvalue