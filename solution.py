import pandas as pd
import numpy as np
import scipy.stats as stats
from statsmodels.stats.proportion import proportions_ztest

chat_id = 5991293770

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:   
    count = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    z_score, p_value = proportions_ztest(count, nobs, alternative = 'smaller')
    # print(z_score, p_value)
    return p_value < 0.02
