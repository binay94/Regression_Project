import os
import sys
import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
from src.exception import CustomException
from src.logger import logging


def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb') as fp:
            pickle.dump(obj,fp)
            
    except Exception as e:
        raise CustomException(e,sys)
