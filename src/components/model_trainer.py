import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression,Lasso,Ridge, ElasticNet
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object,evaluate_model

from dataclasses import dataclass
import os,sys

@dataclass
class modeltrainerconfig:
    trained_model_file_path=os.path.join('artifacts','model.pkl')

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=modeltrainerconfig()

    def initiate_model_training(self,train_array,test_array):
        try:
            logging.info('splitting dependent and independent variables from train and test data')
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )

            models={
                'linear regression':LinearRegression(),
                'lasso':Lasso(),
                'ridge':Ridge(),
                'elastic net':ElasticNet()
            }
            model_report:dict=evaluate_model(X_train,y_train,X_test,y_test,models)
            print('\n',model_report,'\n','='*70)
            logging.info(f'MODEL REPORT : {model_report}')

            ##get max r2scored model from dictionary
            best_model_score=max(sorted(model_report.values()))

            ##get model name of maximum r2score
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model=models[best_model_name]
            print(f'\nbest model found , model name :{best_model_name} ,R2-score : {best_model_score}\n')
            print("="*70,'\n')
            logging.info(f'best model found, model name : {best_model_name} ,r2-Score : {best_model_score}')
            logging.info('Hyperparameter tuning started for catboost')

            save_object(
                    file_path=self.model_trainer_config.trained_model_file_path,
                    obj=best_model
            )
        except Exception as e:
            logging.info('Error occured in model training')
            raise CustomException(e,sys)