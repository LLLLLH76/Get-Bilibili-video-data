import pandas as pd
import requests
import re
import time
import xlsxwriter
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}
data=pd.read_csv('vlog.csv',usecols=['up'])
up_list=sorted(list(set(data.up)))
fans_list=[]
i=0
for up in up_list:
    r=requests.get('https://search.bilibili.com/upuser?keyword='+up,headers=headers)
    print(r.status_code,'  ',i)
    if r.status_code!=200:
        time.sleep(330)
        r=requests.get('https://search.bilibili.com/upuser?keyword='+up,headers=headers)
    #re1=re.compile('共找到(.*?)个用户')
    try:
        re2=re.compile('<span>粉丝：(.*?)</span>')
        fans=re.findall(re2,r.text)[0]
        if '万' in fans:
            fans=int(float(fans[:-1])*10000)
        else:
            fans=int(fans)
        fans_list.append((up,fans))
        i+=1
    except IndexError:
        continue
fans_list_up=[x[0] for x in fans_list]
fans_list_number=[x[1] for x in fans_list]
data=pd.DataFrame({'up':fans_list_up,'number':fans_list_number})
data.to_excel('fans.xlsx',engine='xlsxwriter')
        

