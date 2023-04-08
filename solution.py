import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest

chat_id = 543286418 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  
    alpha = 0.02
    counts = np.array([x_success, y_success])
    nobs = np.array([x_cnt, y_cnt])
    stat, pval = proportions_ztest(counts, nobs, alternative = 'larger')
    
    return pval < alpha 
