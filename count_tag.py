import pandas as pd
data=pd.read_csv('vlog.csv')
d={}
tag1=list(data['tag'])#original tag list
for x in tag1:
    temptag=x.split(',')
    for y in temptag:
        y=y.lower()
        if y not in d:
            d[y]=1
        else:
            d[y]+=1
tag_list1=list(d.items())
tag_list2=[]           #tag list without only-1 tags
for x in tag_list1:
    if x[1]!=1:
        tag_list2.append(x)
    else:
        continue
tag_list3=[]            #tag list without only-1 and only-2 tags
for x in tag_list2:
    if x[1]!=2:
        tag_list3.append(x)
    else:
        continue
tag_list3.sort(key=lambda x:x[1],reverse=True)
for x in tag_list3:
    data[x]=[0]*len(data)

#tag_list1:8103   tag_list2:2872   tag_list3:1812

