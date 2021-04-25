import re
import os

def is_rare_name(string):
    pattern=re.compile(u'[~!@#$%^&* ]')
    match=pattern.search(string)
    if match:
        return True
    try:
        string.encode('gb2312')
    except UnicodeEncodeError:
        return True
    return False
def judge1(sen):
    symbol=['，','。','？','！','·']
    for i in sen:
        for j in i:
            if j not in symbol and is_rare_name(j):
                return False
    return True
def judge2(sen):
    symbol=['。','？','！','、','：','；']
    num=0
    for i in sen:
        if i in symbol:
            return False
        elif i=='，':
            num+=1
    if num==1:
        return True
    return False
f=open('诗词1.txt','r',encoding='UTF-8-SIG')
f1=open('诗词2.txt','w',encoding='UTF-8-SIG')
cnt=0
unique=set()
while True:
    line=f.readline()
    if line=='':
        break 
    line=line[:len(line)-1]
    sen=line.split(',')
    #print(sen)
    flag=True
    for i in sen:
        if i=='':
            flag=False
    if flag:
        if sen[0].endswith(('。','？','！','；')):
            sen[0]=sen[0].rstrip('。？！；')
        if judge1(sen) and judge2(sen[0]) and sen[0] not in unique and len(sen[0])<=15 and len(sen[1])<=5 and len(sen[2])<=15:
            unique.add(sen[0])
            f1.write(str(cnt)+','+','.join(sen[0].split('，'))+','+sen[1]+','+sen[2]+'\n')
            cnt+=1
f.close()  
f1.close()
print('共收集名句：',cnt)