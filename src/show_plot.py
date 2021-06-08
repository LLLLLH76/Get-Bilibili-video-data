import pandas as pd 
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']
data=pd.read_csv(r'C:\Users\apple-pc\Desktop\python\超级无敌vlog6.csv',encoding='gbk')

#按时长爬取饼状图：
lst1=[]
for i in range(len(data['length'])):
    if data['length'][i]/1000<1:
        lst1.append('0-10min')
    elif (data['length'][i]/1000>=1 and data['length'][i]/1000<3):
        lst1.append('10-30min')
    elif (data['length'][i]/1000>=3 and data['length'][i]/1000<10):
        lst1.append('30-60min')
    else:
        lst1.append('>60min')
data['length_']=lst1
data0=data.groupby('length_')
data0.length_.count().plot(kind='pie',autopct='%.2f')
plt.show()

#粉丝前十up主：
data1=data[['up','fans']].groupby('up').fans.mean().sort_values(ascending=False)
pic=data1[:10].plot(kind='bar',title='粉丝数排名前十up主',color='#87CEFA')
pic.set(xlabel='up',ylabel='fans')
plt.xticks(rotation=30)
plt.show()

#播放量、弹幕、评论、收藏前十：
for i,j,k in [['view','播放量','#FF8C00'],['danmu','弹幕数','#32CD32'],['review','评论数','#FF6347'],['favorite','收藏量','#7B68EE']]:
    data2=data[['title',i]].groupby('title')[i].mean().sort_values()
    pic2=data2[-10:].plot(kind='barh',title=j+'前十排行',color=k)
    pic2.set(xlabel=i,ylabel='title')
    plt.show()

#粉丝数与平均播放量，弹幕数，评论数，收藏量的关系：
lst2=[]
for i in range(len(data['fans'])):
    if data['fans'][i]/10000<1:
        lst2.append(' 0-1')
    elif (data['fans'][i]/10000>=1 and data['fans'][i]/10000<10):
        lst2.append(' 1-10')
    elif (data['fans'][i]/10000>=10 and data['fans'][i]/10000<50):
        lst2.append(' 10-50')
    elif (data['fans'][i]/10000>=50 and data['fans'][i]/10000<100):
        lst2.append(' 50-100')
    elif (data['fans'][i]/10000>=100 and data['fans'][i]/10000<200):
        lst2.append('100-200')
    elif (data['fans'][i]/10000>=200 and data['fans'][i]/10000<500):
        lst2.append('200-500')
    else:
        lst2.append('>500')
data['fans/万']=lst2
data3=data.groupby('fans/万')
fig,axes=plt.subplots(2,2)
data3.view.mean().plot(kind='bar',ax=axes[0,0],color='#87CEFA',title='粉丝数与平均播放量的关系')
data3.danmu.mean().plot(kind='bar',ax=axes[0,1],color='#FF8C00',title='粉丝数与平均弹幕数的关系')
data3.review.mean().plot(kind='bar',ax=axes[1,0],color='#32CD32',title='粉丝数与平均评论数的关系')
data3.favorite.mean().plot(kind='bar',ax=axes[1,1],color='#FF6347',title='粉丝数与平均收藏量的关系')
plt.tight_layout()
plt.show()

#播放量与平均弹幕数，评论数，收藏量的关系：
lst3=[]
for i in range(len(data['view'])):
    if data['view'][i]/10000<1:
        lst3.append('  0-1')
    elif (data['view'][i]/10000>=1 and data['view'][i]/10000<5):
        lst3.append('  1-5')
    elif (data['view'][i]/10000>=5 and data['view'][i]/10000<10):
        lst3.append('  5-10')
    elif (data['view'][i]/10000>=10 and data['view'][i]/10000<50):
        lst3.append(' 10-50')
    elif (data['view'][i]/10000>=50 and data['view'][i]/10000<100):
        lst3.append(' 50-100')
    elif (data['view'][i]/10000>=100 and data['view'][i]/10000<200):
        lst3.append('100-200')
    else:
        lst3.append('>200')
data['view/万']=lst3
data4=data.groupby('view/万')
fig,axes=plt.subplots(1,3)
data4.danmu.mean().plot(kind='bar',ax=axes[0],color='#87CEFA',title='播放量与平均弹幕数的关系')
data4.review.mean().plot(kind='bar',ax=axes[1],color='#32CD32',title='播放量与平均评论数的关系')
data4.favorite.mean().plot(kind='bar',ax=axes[2],color='#FF8C00',title='播放量与平均收藏量的关系')
plt.show()

#时长与平均播放量的关系：
lst4=[]
for i in range(len(data['length'])):
    if data['length'][i]/100<5:
        lst4.append(' 0-5')
    elif (data['length'][i]/100>=5 and data['length'][i]/100<10):
        lst4.append(' 5-10')
    elif (data['length'][i]/100>=10 and data['length'][i]/100<15):
        lst4.append('10-15')
    elif (data['length'][i]/100>=15 and data['length'][i]/100<30):
        lst4.append('15-30')
    elif (data['length'][i]/100>=30 and data['length'][i]/100<40):
        lst4.append('30-40')
    elif (data['length'][i]/100>=40 and data['length'][i]/100<60):
        lst4.append('40-60')
    elif (data['length'][i]/100>=100 and data['length'][i]/100<200):
        lst4.append('60-120')
    else:
        lst4.append('>120')
data['length/min']=lst4
data5=data.groupby('length/min')
data5.view.mean().plot(kind='line',title='时长与平均播放量的关系')
plt.xlabel('时长/min')
plt.show()

#弹幕数与评论数的比较（截取其中500个数据）：
data6=data.sort_values(by='danmu',ascending=False)[300:800]
X=[item for item in data6.danmu]
Y=[item for item in data6.review]
plt.scatter(X,Y,color='#7B68EE',marker='.')
plt.plot(X,X,label='1:1',color='#FF8C00')
plt.title('弹幕数与评论数的比较')
plt.xlabel('弹幕数')
plt.ylabel('评论数')
plt.legend()
plt.show()

#标签分类及十大热门标签排行
taglist=[['校园','大学'],['美食','早餐','一人食','吃播','吃货'],['搞笑','恶搞','沙雕','搞笑视频','逗比'],['学习'],['旅行','旅游'],['情侣','恋爱','爱情'],['韩国','韩国vlog','韩国VLOG','韩语'],['日本','日语','日本文化'],['欧美','美国','欧洲','北欧','英语'],['明星'],['美妆','化妆'],['宠物','萌宠','动物','动物圈'],['摄影'],['留学'],['购物','购物分享'],['健身','运动','减肥'],['吐槽']]
dic_num,dic_view={},{}
tag1=list(data['tag'])
view1=list(data['view'])
for item in taglist:
    viewlist=[]
    for i in range(len(tag1)):
        for t in tag1[i].split(','):
            if t in item:
                viewlist.append(view1[i])
                break
    dic_num[item[0]]=len(viewlist)
    dic_view[item[0]]=int(np.mean(viewlist))
dic={'num':list(dic_num.values()),'view':list(dic_view.values())}
data7=pd.DataFrame(dic,index=list(dic_view.keys()))
data7.num.plot.pie(autopct='%.2f',title='各标签所占比例')
plt.show()
data7.sort_values(by='view',ascending=False).view[:10].plot(kind='bar',color='#87CEFA',title='十大热门标签排行')
plt.show()

#总播放量前十up：
for i,j in [['view','播放量'],['favorite','收藏量']]:
    data8=data[['up',i]].groupby('up')
    data8[i].sum().sort_values(ascending=False)[:10].plot(kind='bar',color='#FF8C00',title='总'+j+'前十up')
    plt.xticks(rotation=20)
    plt.show()
    data8[i].mean().sort_values(ascending=False)[:10].plot(kind='bar',color='#87CEFA',title='平均'+j+'前十up')
    plt.xticks(rotation=20)
    plt.show()

