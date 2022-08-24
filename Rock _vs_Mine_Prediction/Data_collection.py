from email.header import Header
import pandas as pd
import os
import sys

class read_data():

    def read_data_file(self,header):
        for i in os.listdir('./Rock _vs_Mine_Prediction'):
            if i.endswith('.csv'):
                data = pd.read_csv(os.path.join('./Rock _vs_Mine_Prediction',i),header=header)
                return data
                break
            elif i.endswith('xlsx'):
                data = pd.read_excel(os.path.join('./Rock _vs_Mine_Prediction',i))
                return data

            



