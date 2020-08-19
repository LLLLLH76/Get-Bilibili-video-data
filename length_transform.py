#将excel中 1:23:45 的时长形式变为 12345 方便排序
import pandas as pd
data=pd.read_csv('bilibili_vlog click 1 2.csv')
length=data['length']
length_list=[]
for x in length:
    length_list.append(int(''.join(x.split(':'))))
data['length']=length_list
data.to_excel('bilibili_vlog click 1 and 2.xlsx')