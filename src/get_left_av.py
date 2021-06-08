import pandas as pd
import requests
import re
import time
import xlsxwriter
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}
data=pd.read_csv('超级无敌vlog3.csv')
for i in range(6396,6420):
    try:
        bv=data.iloc[i,0]
        r=requests.get('https://www.bilibili.com/video/'+bv,headers=headers)
        print(r.status_code,'  ',i,'  ',1359)
        if r.status_code!=200:
            #time.sleep(430)
            #r=requests.get('https://www.bilibili.com/video/'+x,headers=headers)
            break

        av_re=re.compile('itemprop="url" content="https://www.bilibili.com/video/av(.*?)/"><meta data-vue-meta=')
        av=re.findall(av_re,r.text)[0]
        data.iloc[i,1]=av
    except ConnectionError:
        break

data.to_excel('超级无敌vlog5.xlsx',engine='xlsxwriter')


