import tkinter as tk
from tkinter import ttk
import requests
import re
import  json




def showwether(dicta):
    root1=tk.Tk()
    root1.title('城市'+dicta['result']['today']['city']+'的天气信息')

    root1.geometry()

#菜单部分
    MainMenu=tk.Menu(root1)
    barOfMainMenu=tk.Menu(root1)
    root1['menu'] = MainMenu
    MainMenu.add_cascade(label='操作',menu=barOfMainMenu)#加功能
    for item in ['测试1','测试2']:
        barOfMainMenu.add_cascade(label=item)#用于扩展菜单的 接口
    barOfMainMenu.add_command(label='退出',command=root1.quit)#加功能

    #主框架
    MainFrame=tk.Frame(root1,bg='green',padx=10,pady=30)

    #当前天气框架
    nowWeth=tk.Frame(MainFrame,bg='blue',padx=2,pady=10)
    feng_lx=tk.Frame(nowWeth,bg='red',padx=0,pady=10)
    ws_du=tk.Frame(nowWeth,bg='red',padx=0,pady=10)
    wenduLabel=tk.Label(ws_du,text='温度   '+dicta['result']['sk']['temp'],bg='pink',font=("Arial", 12)).pack(ipadx=3)
    shiduLabel=tk.Label(ws_du,text='湿度   '+dicta['result']['sk']['humidity'],bg='pink',font=("Arial", 12)).pack(ipadx=3)
    fengliLbel=tk.Label(feng_lx,text='风力   '+dicta['result']['sk']['wind_strength'],bg='pink',font=("Arial", 12)).pack(ipadx=3)
    fengxLbel =tk.Label(feng_lx, text='风向   '+dicta['result']['sk']['wind_direction'], bg='pink',font=("Arial", 12)).pack(ipadx=3)
    tit=tk.Label(MainFrame,text='当前天气(更新时间为    '+dicta['result']['sk']['time'],bg='purple',font=("Arial",9)).pack(anchor='nw',ipady=2)
    feng_lx.pack(side='top')
    ws_du.pack(side='top',anchor='nw')
    #nowWeth.place(x=30,y=30)
    nowWeth.pack(side='left')
    #今日天气框架
    todayWetherFra=tk.Frame(MainFrame,bg='green',padx=10,pady=10)

    baseInfo = tk.Frame(todayWetherFra, bg='red', padx=10, pady=10)
    Son1 = tk.Label(baseInfo, text='城市:  '+dicta['result']['today']['city'],font=("华文行楷", 15)).pack()
    Son2 = tk.Label(baseInfo, text='日期:  '+dicta['result']['today']['date_y'],font=("华文行楷", 15)).pack()
    Son3 = tk.Label(baseInfo, text='星期:  '+dicta['result']['today']['week'],font=("华文行楷", 15)).pack()
    Son4 = tk.Label(baseInfo, text='温度:  '+dicta['result']['today']['temperature'],font=("华文行楷", 15)).pack()
    Son5 = tk.Label(baseInfo, text='天气:  '+dicta['result']['today']['weather'],font=("华文行楷", 15)).pack()
    Son5_1 = tk.Label(baseInfo, text='风向:  '+dicta['result']['today']['wind'], font=("华文行楷", 15)).pack()

    OtherIndex = tk.Frame(todayWetherFra, bg='pink', padx=10, pady=10)
    Son6 = tk.Label(OtherIndex, text='穿衣指数:  '+dicta['result']['today']['dressing_index'],font=("华文行楷", 15)).pack()
    Son7 = tk.Label(OtherIndex, text='穿衣建议:  '+dicta['result']['today']['dressing_advice'],font=("华文行楷", 15)).pack()
    Son8 = tk.Label(OtherIndex, text='舒适度指数:  '+dicta['result']['today']['comfort_index'],font=("华文行楷", 15)).pack()
    Son9 = tk.Label(OtherIndex, text='洗车指数:  '+dicta['result']['today']['wash_index'],font=("华文行楷", 15)).pack()
    Son10 = tk.Label(OtherIndex, text='晨炼指数:  '+dicta['result']['today']['exercise_index'],font=("华文行楷", 15)).pack()
    Son11 = tk.Label(OtherIndex, text='旅游指数:  '+dicta['result']['today']['travel_index'], font=("华文行楷", 15)).pack()
    Son12 = tk.Label(OtherIndex, text='干燥指数:  '+dicta['result']['today']['drying_index'], font=("华文行楷", 15)).pack()
    Son13 = tk.Label(OtherIndex, text='紫外线指数:  '+dicta['result']['today']['uv_index'], font=("华文行楷", 15)).pack()

    OtherIndex.pack(side='right')
    baseInfo.pack(side='left')


    todayWetherFra.pack(side='right')

    MainFrame.pack()
    root1.mainloop()


def  pick(code):

    url = 'http://v.juhe.cn/weather/index?format=2&cityname=%d&key=43ecc84eecddd574aa7fb3ccd7287079'%code

    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        dict=r.json()


        #print(r.text)
    except:
        print("异常")
    showwether(dict)


def welcome():
    root = tk.Tk()
    root.title('天气查询')

    WelcomeLab = tk.Label(root, text='欢迎进入经典天气查询系统！', bg='pink', font=('隶书', 20)).pack(fill='x', ipady=10, ipadx=20,padx=20, pady=10)

    cityDict = {'苏州': 25, '北京': 2}

    # 创建城市列表选选择区域
    frame_City = tk.Frame(root, bg='blue')

    lab1 = tk.Label(frame_City, text='请选择城市： ', bg='red').pack(ipadx=5, side='left')

    cityname = tk.StringVar()
    numberChosen = ttk.Combobox(frame_City, width=12, textvariable=cityname)
    numberChosen['values'] = ('', '苏州', '北京')  # 设置下拉列表的值
    numberChosen.pack(side='left')  # 设置其在界面中出现的位置  column代表列   row 代表行
    numberChosen.current(0)  # 设置

    frame_City.pack(anchor='nw', padx=20)

    # 按钮查询
    Button_go = tk.Button(frame_City, text=' 查询  ', bg='red', command=lambda: pick(cityDict[cityname.get()])).pack(side='right', padx=20, pady=10)


    root.mainloop()



if __name__ =='__main__':
    welcome()



