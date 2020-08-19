#爬的时候只爬了bv 但爬评论要用av 心里苦啊 还好这里没有反爬
import pandas as pd
import requests
import re
import time
import xlsxwriter
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}
data=pd.read_csv('超级无敌vlog.csv',usecols=['BV'])
bv_list=list(data.BV)

bv_av_list=[]
for i in range(4169,4395):
    try:
        x=bv_list[i]
        r=requests.get('https://www.bilibili.com/video/'+x,headers=headers)
        print(r.status_code,'  ',i,'  ',4395)
        if r.status_code!=200:
            #time.sleep(430)
            #r=requests.get('https://www.bilibili.com/video/'+x,headers=headers)
            break

        av_re=re.compile('itemprop="url" content="https://www.bilibili.com/video/av(.*?)/"><meta data-vue-meta=')
        av=re.findall(av_re,r.text)
        bv_av_list.append((x,av))
    except ConnectionError:
        break
temp_bv_list=[x[0] for x in bv_av_list]
av_list=[x[1] for x in bv_av_list]
av_data=pd.DataFrame({'bv':temp_bv_list,'av':av_list})
av_data.to_excel('av5.xlsx',engine='xlsxwriter')


