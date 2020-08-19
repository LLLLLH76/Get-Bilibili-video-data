import pandas as pd
import xlsxwriter
original_data=pd.read_csv('vlog.csv')
fans_data=pd.read_csv('fans.csv')
d=dict(zip(list(fans_data.up),list(fans_data.number)))
original_data['fans']=[0]*len(original_data)
for i in range(len(original_data)):
    if original_data.iloc[i,4] in d:
        original_data.iloc[i,10]=d[original_data.iloc[i,4]]
original_data.to_excel('超级无敌vlog.xlsx',engine='xlsxwriter')
