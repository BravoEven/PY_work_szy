import requests
import re
import  json
import pickle

def  get():
    CityNameDict={}

    url = 'http://v.juhe.cn/weather/citys?key=43ecc84eecddd574aa7fb3ccd7287079'

    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        CityNameDict=r.json()

    except:
        print("异常")

    with open('CityName.txt','wb') as f:
        pickle.dump(CityNameDict,f)
    f.close()
    print('写入完成')
    with open('CityName.txt','rb') as f1:
        TestDict=pickle.load(f1)

    f1.close()
    print(TestDict)

def Pr(Mes='',Command=0):#遍历重组地区拓扑列表
    with open('CityName.txt', 'rb') as f1:
        TestDict = pickle.load(f1)

    f1.close()

    num=2574  #0--2573
    MainList=TestDict['result']

    ProvincesList=['']
    citiList=[]
    diQulist=[]
    for i in range(2574):
        if MainList[i]['province']  not in ProvincesList:
            ProvincesList.append(MainList[i]['province'])
        if MainList[i]['city']  not in citiList:
            citiList.append(MainList[i]['city'])
        if MainList[i]['district']  not in diQulist:
            diQulist.append(MainList[i]['district'])

    if Command is 0:
        return ProvincesList
    if Command is 1:
        LinList=['']
        for i in range(2574):

            if MainList[i]['province'] == Mes:
                if  MainList[i]['city'] not in LinList:
                    LinList.append(MainList[i]['city'])

        return LinList

    if Command is 2:
            LinList = ['']

            for i in range(2574):

                if MainList[i]['city'] == Mes:
                    if MainList[i]['district'] not in LinList:
                        LinList.append(MainList[i]['district'])

            return LinList
    if Command is 3:

        f1=open('Test.txt','w')
        for i in range(2574):
            f1.write(MainList[i]['city']+''+MainList[i]['district']+'\n')






if __name__ == '__main__':
    Pr('',3)