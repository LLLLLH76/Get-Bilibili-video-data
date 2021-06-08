import requests
import re
import xlsxwriter
import pandas as pd
import time
length_list=[]#shipinchangdu
title_list=[]#biaoti
view_list=[]#bofangliang
danmu_list=[]
pubdate_list=[]
up_list=[]
favorites_list=[]#shoucang
bv_list=[]
tag_list=[]#biaoqian
review_list=[]#pinglun

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
}

for i in range(1,5):
    for j in range(1,51):
        if j == 1:
            r = requests.get('https://search.bilibili.com/all?keyword=vlog&from_source=nav_search&spm_id_from=333.6.b_696e7465726e6174696f6e616c486561646572.9&order=totalrank&duration='+str(i)+'&tids_1=0',headers=headers)
        else:
            r=requests.get('https://search.bilibili.com/all?keyword=vlog&from_source=nav_search&spm_id_from=333.6.b_696e7465726e6174696f6e616c486561646572.9&order=totalrank&duration='+str(i)+'&tids_1=0&page='+str(j),headers=headers)
        print(r.status_code,'  ',i,'  ',j)
        if r.status_code!=200:
            time.sleep(330)
            if j == 1:
                r = requests.get('https://search.bilibili.com/all?keyword=vlog&from_source=nav_search&spm_id_from=333.6.b_696e7465726e6174696f6e616c486561646572.9&order=click&duration='+str(i)+'&tids_1=0',headers=headers)
            else:
                r=requests.get('https://search.bilibili.com/all?keyword=vlog&from_source=nav_search&spm_id_from=333.6.b_696e7465726e6174696f6e616c486561646572.9&order=click&duration='+str(i)+'&tids_1=0&page='+str(j),headers=headers)
        length_title_re=re.compile('" target="_blank" class="img-anchor"><div class="img"><div class="lazy-img"><img alt="" src=""></div><span class="so-imgTag_rb">(.*?)</span><div class="watch-later-trigger watch-later"></div><span class="mask-video"></span></div><!----></a><div class="info"><div class="headline clearfix"><!----><!----><span class="type hide">(.*?)</span><a title="(.*?)" href="//www.bilibili.com/video/')
        length_title=re.findall(length_title_re,r.text)
        length_list.extend([int(''.join(x[0].split(':'))) for x in length_title])
        title_list.extend([x[2] for x in length_title])
        alot_re=re.compile('{"type":"video","id":(.*?),"author":"(.*?)","mid":(.*?),"typeid":"(.*?)","typename":"(.*?)","arcurl":"(.*?)","aid":(.*?),"bvid":"(.*?)","title":"(.*?)","description":"(.*?)","arcrank":"0","pic":"(.*?)","play":(.*?),"video_review":(.*?),"favorites":(.*?),"tag":"(.*?)","review":(.*?),"pubdate":(.*?),"senddate":(.*?),"duration":"(.*?)"')
        alot=re.findall(alot_re,r.text)
        view_list.extend([int(x[11]) for x in alot])#bofang
        danmu_list.extend([int(x[12]) for x in alot])
        up_list.extend([x[1] for x in alot])
        bv_list.extend([x[7] for x in alot])
        pubdate_list.extend([time.ctime(int(x[16])) for x in alot])
        favorites_list.extend([int(x[13]) for x in alot])#shoucang
        tag_list.extend([x[14] for x in alot])
        review_list.extend([int(x[15]) for x in alot])


data=pd.DataFrame({'BV':bv_list,'title':title_list,'pubtime':pubdate_list,'tag':tag_list,'up':up_list,'length':length_list,'view':view_list,'danmu':danmu_list,'review':review_list,'favorite':favorites_list})

data.to_excel('real_bilibili_vlog2.xlsx',engine='xlsxwriter')
