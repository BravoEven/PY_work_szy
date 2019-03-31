import requests
import re
import  json



def  pick(code):

    url = 'http://v.juhe.cn/weather/index?format=2&cityname='+code+'&key=43ecc84eecddd574aa7fb3ccd7287079'

    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        dict=r.json()

        return  dict

    except:
        print("异常")
