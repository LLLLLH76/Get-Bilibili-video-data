import pandas as pd
import requests
import re
import time
import xlsxwriter
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

data=pd.read_csv('超级无敌vlog6.csv')
#data['comment']=['0']*len(data)
for i in range(1012,2000):
    av=data.iloc[i,1]
    r=requests.get('https://api.bilibili.com/x/v2/reply?17208250316650699887_1590632569872&jsonp=jsonp&pn=1&type=1&oid='+str(av)+'&sort=2',headers=headers)
    print(r.status_code,'  ',i,'  ',len(data))
    if r.status_code!=200:
        time.sleep(330)
        r=requests.get('https://api.bilibili.com/x/v2/reply?17208250316650699887_1590632569872&jsonp=jsonp&pn=1&type=1&oid='+str(av)+'&sort=2',headers=headers)
    num_re=re.compile(',"count":(.*?),"acount":')
    if len(re.findall(num_re,r.text))>0 and int(re.findall(num_re,r.text)[0])//20>1:
        num=int(re.findall(num_re,r.text)[0])//20
        comment=[]
        for page in range(1,num):
            r=requests.get('https://api.bilibili.com/x/v2/reply?17208250316650699887_1590632569872&jsonp=jsonp&pn='+str(page)+'&type=1&oid='+str(av)+'&sort=2',headers=headers)
            print(r.status_code,'  ',page,'  ',num)
            comment_re=re.compile('"content":{"message":"(.*?)"')
            comment.extend(re.findall(comment_re,r.text))

        for j in range(len(comment)):    
            with open(str(i)+".txt","a+",encoding='utf-8') as f:
                f.write(comment[j])
                f.write('\n')
    #data.iloc[i,12]=[[comment]]
#data.to_excel('终极超级无敌牛牛牛vlog.csv',engine='xlsxwriter')
