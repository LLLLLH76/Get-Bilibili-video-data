#calculate total length
import pandas as pd 
df2=pd.read_csv('final_bilibili_vlog.csv')
lenlist=list(df2['length'])
_lenlist=[]
for x in lenlist:
    second=x%100
    minute=x//100%100
    hour=x//10000%100
    _lenlist.append(hour*60*60+minute*60+second)
print(sum(_lenlist)/60)

#6615 hours