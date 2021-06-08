#去掉excel中的重复项重复的视频
import pandas as pd
df1=pd.read_csv('av2.csv')
df2=pd.DataFrame(columns=list(df1.columns))
df2.append(df1.iloc[0])
for i in range(1,len(df1)):
    if df1.iloc[i,0]==df1.iloc[i-1,0]:
        continue
    else:
        df2=df2.append(df1.iloc[i])
df2.to_excel('real_final_bilibili_vlog.xlsx')

