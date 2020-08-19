import jieba.posseg as psg
import wordcloud
import matplotlib.pyplot as plt
import pandas as pd

data=pd.read_csv('超级无敌vlog6.csv')
taglist=[['校园','大学'],['美食','早餐','一人食','吃播','吃货'],['搞笑','恶搞','沙雕','搞笑视频','逗比'],['学习'],['旅行','旅游'],['情侣','恋爱','爱情'],['韩国','韩国vlog','韩国VLOG','韩语'],['日本','日语','日本文化'],['欧美','美国','欧洲','北欧','英语'],['明星'],['美妆','化妆'],['宠物','萌宠','动物','动物圈'],['摄影'],['留学'],['购物','购物分享'],['健身','运动','减肥'],['吐槽']]
dic_index={}
tag_list=list(data['tag'])
for item in taglist:
    viewlist=[]
    for i in range(len(tag_list)):
        for t in tag_list[i].split(','):
            if t in item:
                viewlist.append(data.iloc[i:i+1,8:9])
                break
    dic_index[item[0]]=[x.index.start for x in viewlist]
    
one_tag_list=dic_index['校园']

#with open(r'E:\ClassifiedDocuments\NJU\code\chineseStopWords.txt','r') as fp:
    #stopwords=set(line for line in fp.readlines())
stopwords={'回复','n','\n','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
word_list=[]
for i in one_tag_list:
    f=open('comment//'+str(i)+'.txt','r',encoding='utf-8')
    word_list.extend(f.readlines())
dict={}
for i in range(0,len(word_list),3):
    if word_list[i].isspace():
        continue
    fenci=psg.cut(word_list[i])
    for word,flag in fenci:
        if word not in stopwords and 'n' in flag:
            dict[word]=dict.get(word,0)+1
lst=list(dict.items())
lst.sort(key=lambda x:x[1],reverse=True) 
font=r'C:\Windows\Fonts\Simhei.ttf'
wordc=wordcloud.WordCloud(font_path=font,max_words=40,height=3000,width=2500).generate_from_frequencies(dict)
plt.imshow(wordc,interpolation='bilinear')
plt.axis('off')
wordc.to_file('校园.png')
plt.show()