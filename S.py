from tkinter import *
from tkinter import messagebox #as msgbox
from tkinter import ttk
import pickle
import urllib.parse    #转码包quote
import GetPart
import CityListReady
import Chck_part
import Set_New

class MianWindow(object):


    def __init__(self): # 初始化布局
     #关键变量
        self.Info={}
        self.FuTureDay = 0#未来天气模块

        self.Top=Tk()
        self.Top.title('天气查询系统 v1.0')

        #self.bt1 = Button(self.Top, text='test', command=self.Door).pack()

        self.photo = PhotoImage(file="mmexport1474714477684.png")
        self.PicLable=Label(self.Top,text='     \t\t\tQwQ\n\t\t只要有你  \n  \t\t     便是晴天\n\n\n\n\n\n\n\n\n\n\n\n\n\n',justify=LEFT,image=self.photo,compound=CENTER,fg="black",font=("隶书", 30))
        self.PicLable.pack()




        #定义菜单栏
        self.rootMenu=Menu(self.Top,bg='pink')
        self.menuList_1=Menu(self.Top)

        self.rootMenu.add_command(label='开始', command=self.Door)

        self.menuList_1.add_command(label='测试1',command=self.Door)
        self.menuList_1.add_command(label='未来天气',command=self.Future)
        self.menuList_1.add_command(label='退出',command=self.Top.quit)

        self.Top['menu']=self.rootMenu

    def GoBack(self):
        self.MainFrame.pack_forget()
        self.GoButton.pack_forget()
        self.numberChosen_3.pack_forget()
        self.StepLab.config(text='')
        self.Step_1=''
        self.Step_2 = ''
        self.Step_3 = ''

        self.frame_City.pack(anchor='nw', padx=20, pady=10, ipadx=5, ipady=3)
        self.numberChosen['value']=self.ProvinceList
        self.numberChosen.current(0)
        self.numberChosen.pack(side='left')
        self.ConfirmBut_1.pack(side='left')

    def OK_1(self):#装填城市列表

        self.Step_1=self.name_1.get()
        self.StepLab.config(text=self.Step_1 + self.Step_2 + self.Step_3)



        self.ListReady(self.Step_1,1)



        self.numberChosen.pack_forget()   #更换方框
        self.numberChosen_2.pack(side='left')


        #print('预备列表',self.CityList)
        self.numberChosen_2['values']=self.CityList
        self.numberChosen_2.current(0)  # 设置


        self.lab2.config(text='请选择城市：')

        self.ConfirmBut_1.pack_forget()
        self.ConfirmBut_2.pack(padx=10, pady=5, side='left')

    def OK_2(self):#装填地区列表

        self.Step_2 = self.name_2.get()
        self.StepLab.config(text=self.Step_1 +'：'+ self.Step_2 + self.Step_3)

        self.ListReady(self.Step_2,2)

        self.numberChosen_2.pack_forget()#更换方框
        self.numberChosen_3.pack(side='left')

        self.numberChosen_3['values']=self.DiquList

        self.lab2.config(text='请选择地区：')

        self.ConfirmBut_2.pack_forget()
        self.GoButton.pack(padx=10, pady=5, side='left')

    def ListReady(self,Mes='',Command=0):#准备选择列表

        if Command is 0:
            self.ProvinceList=CityListReady.Pr(Command)
        if Command is 1:
            self.CityList=CityListReady.Pr(Mes,Command)
        if Command is 2:
            self.DiquList=CityListReady.Pr(Mes,Command)

    def Start(self):#登陆后界面布局
        size_0=20

        self.rootMenu.add_cascade(label='操作', menu=self.menuList_1)

        self.lab1 = Label(self.Top, text=' 欢迎进入经典天气查询系统！', bg='pink', font=("隶书", 41))
        self.lab1.pack(fill='x', pady=5, ipadx=5, ipady=3)

        # 创建城市列表选选择区域
        self.ListReady()  # 首先请求省份列表

        self.frame_City = Frame(self.Top, bg='blue')
        self.lab2 = Label(self.frame_City, text='请选择省份： ', bg='red', font=("华文行楷", size_0))
        self.lab2.pack(ipadx=5, side='left')

        self.name_1 = StringVar()
        self.numberChosen = ttk.Combobox(self.frame_City, width=12, textvariable=self.name_1, font=("华文行楷", size_0))

        self.numberChosen['values'] = self.ProvinceList  # 设置下拉列表的值
        self.numberChosen.pack(side='left')
        self.numberChosen.current(0)  # 设置

        self.name_2 = StringVar()
        self.numberChosen_2 = ttk.Combobox(self.frame_City, width=12, textvariable=self.name_2, font=("华文行楷", size_0))

        self.name_3 = StringVar()
        self.numberChosen_3 = ttk.Combobox(self.frame_City, width=12, textvariable=self.name_3, font=("华文行楷", size_0))





        self.ConfirmBut_1 = Button(self.frame_City, text='确定省份', bg='yellow', font=("华文行楷", size_0 ), command=self.OK_1)
        self.ConfirmBut_1.pack(padx=10, pady=5, side='right')

        self.ConfirmBut_2 = Button(self.frame_City, text='确定城市', bg='red', font=("华文行楷",  size_0), command=self.OK_2)

        self.GoButton = Button(self.frame_City, text='查询', bg='green', font=("华文行楷",  size_0), command=self.Go)

        self.frame_City.pack(anchor='nw', padx=20, pady=10, ipadx=5, ipady=3)

        self.Step_1=''
        self.Step_2 = ''
        self.Step_3 = ''
        self.StepLab=Label(self.Top,text=self.Step_1+self.Step_2+self.Step_3, font=("隶书",  size_0))
        self.StepLab.pack(anchor='ne', padx=20, pady=10, ipadx=5, ipady=3)

        # 创建天气信息显示框架
        # 主框架
        self.MainFrame = Frame(self.Top, padx=10, pady=30)
        test_Size = 20  # 主框架内字体大小

        # 定义返回按钮

        self.BackButon = Button(self.MainFrame, text='返回', bg='pink', command=self.GoBack).pack(anchor='nw', ipadx=5,ipady=3)

        # 当前天气框架
        self.nowWeth = Frame(self.MainFrame, padx=2, pady=10)
        self.feng_lx = Frame(self.nowWeth, padx=0, pady=10)
        self.ws_du = Frame(self.nowWeth,  padx=0, pady=10)
        self.wenduLabel = Label(self.ws_du, text='温度   ', font=("Arial", test_Size))
        self.shiduLabel = Label(self.ws_du, text='湿度   ', font=("Arial", test_Size))
        self.fengliLbel = Label(self.feng_lx, text='风力   ', font=("Arial", test_Size))
        self.fengxLbel = Label(self.feng_lx, text='风向   ',  font=("Arial", test_Size))
        self.tit = Label(self.MainFrame, text='当前天气(更新时间为    ', bg='yellow', font=("Arial", 19))

        self.feng_lx.pack(side='top')
        self.ws_du.pack(side='top', anchor='nw')

        self.nowWeth.pack(side='left')
        # 今日天气框架
        self.todayWetherFra = Frame(self.MainFrame, padx=10, pady=10)
        kind='楷书'
        self.baseInfo = Frame(self.todayWetherFra, padx=10, pady=10)
        self.Son1 = Label(self.baseInfo, text='城市:  ', font=(kind, test_Size))
        self.Son2 = Label(self.baseInfo, text='日期:  ', font=(kind, test_Size))
        self.Son3 = Label(self.baseInfo, text='星期:  ', font=(kind, test_Size))
        self.Son4 = Label(self.baseInfo, text='温度:  ', font=(kind, test_Size))
        self.Son5 = Label(self.baseInfo, text='天气:  ', font=(kind, test_Size))
        self.Son5_1 = Label(self.baseInfo, text='风向:  ', font=(kind, test_Size))

        self.OtherIndex = Frame(self.todayWetherFra,  padx=10, pady=10)
        self.Son6 = Label(self.OtherIndex, text='穿衣指数:  ', font=(kind, test_Size))
        self.Son8 = Label(self.OtherIndex, text='舒适度指数:  ', font=(kind, test_Size))
        self.Son9 = Label(self.OtherIndex, text='洗车指数:  ', font=(kind, test_Size))
        self.Son10 = Label(self.OtherIndex, text='晨炼指数:  ', font=(kind, test_Size))
        self.Son11 = Label(self.OtherIndex, text='旅游指数:  ', font=(kind, test_Size))
        self.Son12 = Label(self.OtherIndex, text='干燥指数:  ', font=(kind, test_Size))
        self.Son13 = Label(self.OtherIndex, text='紫外线指数:  ', font=(kind, test_Size))

        self.tit.pack(anchor='nw', ipady=2)
        self.wenduLabel.pack(ipadx=3)
        self.shiduLabel.pack(ipadx=3)
        self.fengxLbel.pack(ipadx=3)
        self.fengliLbel.pack(ipadx=3)
        self.Son1.pack()
        self.Son2.pack()
        self.Son3.pack()
        self.Son4.pack()
        self.Son5.pack()
        self.Son6.pack()
        # self.Son7.pack()
        self.Son8.pack()
        self.Son9.pack()
        self.Son10.pack()
        self.Son11.pack()
        self.Son12.pack()
        self.Son13.pack()

        self.OtherIndex.pack(side='right')
        self.baseInfo.pack(side='left')

        self.todayWetherFra.pack(side='right')





        self.PicLable.pack_forget()

    def Door(self):  #门禁函数
        self.PicLable.pack_forget()

    #初始化后台文件
        Userdict = {'admin': '123'}
        with open('UserData.txt', 'wb') as f:

            pickle.dump(Userdict, f)
        f.close()


        self.photo_2= PhotoImage(file="IMG_20190316_6.png")
        self.PicLable_2 = Label(self.Top,justify=LEFT, image=self.photo_2, compound=CENTER, fg="black", font=("隶书", 30))
        self.PicLable_2.pack()

        Color='white'
        size_1=19
        #定义登陆框架
        self.LogFram=Frame(self.Top,bg=Color)

        self.Son_LogFram_1=Frame(self.LogFram,bg=Color)#子框架 1

        self.Uname_lab = Label(self.Son_LogFram_1,text='Name:', font=("华文行楷", size_1),bg=Color).pack(side='top',pady=5)
        self.Ucode_lab = Label(self.Son_LogFram_1, text='Code:', font=("华文行楷", size_1),bg=Color).pack(side='top',pady=5)
        self.LoginButton = Button(self.Son_LogFram_1,text='登陆',command=self.Login, font=("华文行楷", size_1),bg='green').pack(side='top',padx=20,ipadx=24,ipady=3)

        self.Son_LogFram_1.pack(side='left')

        self.U_name = StringVar()
        self.U_code = StringVar()

        self.Son_LogFram_2 = Frame(self.LogFram,bg=Color)#子框架 2
        self.User_name_in=Entry(self.Son_LogFram_2,textvariable=self.U_name, font=("华文行楷", size_1),bg=Color).pack(side='top',padx=30,pady=5)
        self.User_code_in = Entry(self.Son_LogFram_2, textvariable=self.U_code,show='-', font=("华文行楷", size_1),bg=Color).pack(side='top',padx=30,pady=5)
        self.RigisButton = Button(self.Son_LogFram_2, text='注册', command=self.Rigist, font=("华文行楷", size_1),bg='pink').pack(side='top',ipadx=12,ipady=3)
        self.Son_LogFram_2.pack(side='right')

        self.LogFram.place(x=1100,y=650)

    def Rigist(self):  #注册界面
        size_0=20
        self.LogFram.place_forget()
        self.PicLable_2.pack_forget()

        self.New_name=StringVar()
        self.New_code_1 = StringVar()
        self.New_code_2 = StringVar()

        self.SetFram = Frame(self.Top)

        Fram_1=Frame(self.SetFram)
        RLab_1=Label(Fram_1,text='请输入名字 ：', font=("华文行楷", size_0)).pack(side='left',ipady=17)
        get_1 = Entry(Fram_1, textvariable=self.New_name, font=("华文行楷", size_0)).pack(side='right', pady=17)
        Fram_1.pack(side='top')

        Fram_2 = Frame(self.SetFram)
        RLab_2 = Label(Fram_2, text='请输入密码 ：', font=("华文行楷", size_0)).pack(side='left', ipady=17)
        get_2 = Entry(Fram_2, textvariable=self.New_code_1, font=("华文行楷", size_0)).pack(side='right', pady=17)
        Fram_2.pack(side='top')

        Fram_3 = Frame(self.SetFram)
        RLab_3 = Label(Fram_3, text='请再次输入密码 ：', font=("华文行楷", size_0)).pack(side='left', ipady=17)
        get_3 = Entry(Fram_3, textvariable=self.New_code_2, font=("华文行楷", size_0)).pack(side='right', pady=17)
        Fram_3.pack(side='top')

        Fram_4=Frame(self.SetFram)
        Button_1 = Button(Fram_4, text='注册',bg='green', command=self.rigist, font=("华文行楷", size_0+5)).pack(side='left',pady=20,padx=30)
        Button_2 = Button(Fram_4, text='退出',bg='red', command=self.Back_to_log, font=("华文行楷", size_0-5)).pack(side='right',pady=20,padx=30)
        Fram_4.pack(side='top',pady=15)

        self.SetFram.pack(padx=30,pady=10)

    def Back_to_log(self):
        self.SetFram.pack_forget()
        self.LogFram.place(x=20, y=60)
        self.PicLable_2.pack()

    def rigist(self):
        name=self.New_name.get()
        code_1=self.New_code_1.get()
        code_2 = self.New_code_2.get()
        if code_1 is not code_2:
            messagebox.showwarning(title='警告',message='密码不匹配，请重新输入！')

        else:
            re =Set_New.Do(name,code_1,code_2)
            if re is 1:
                messagebox.showinfo(title='通知',message='注册完成！')
                self.Back_to_log()

    def Login(self):
        name=self.U_name.get()
        code=self.U_code.get()

        result=Chck_part.Check(name,code)
        if  result is 1:
            self.LogFram.destroy()
            self.PicLable_2.pack_forget()
            self.Start()
        elif result is 2:
            messagebox.showwarning(title='警告',message='密码错误，请重新输入！')
        elif result is 3:
            messagebox.showwarning(title='警告', message='用户名错误，请先注册！')

    def Go(self):#得到温度信息后布局
        self.frame_City.pack_forget()
        self.MainFrame.pack_forget()

        self.Step_3=self.name_3.get()
        self.StepLab.config(text=self.Step_1+' ：'+self.Step_2+' ：'+self.Step_3+'  的天气')

        print('ceshi'+self.Step_3)

        self.Key=urllib.parse.quote(self.Step_3)   #得到最后地区级名称
        self.Info=GetPart.pick(self.Key)          #发送命令，返回信息字典


        self.tit.config(text='当前天气(更新时间为    '+self.Info['result']['sk']['time'])
        self.fengliLbel.config(text='风力   '+self.Info['result']['sk']['wind_strength'])
        self.fengxLbel.config(text='风向   '+self.Info['result']['sk']['wind_direction'])
        self.shiduLabel.config(text='湿度   '+self.Info['result']['sk']['humidity'])
        self.wenduLabel.config(text='温度   '+self.Info['result']['sk']['temp'])

        self.Son1.config( text='城市:  ' + self.Info['result']['today']['city'])
        self.Son2.config(text='日期:  ' + self.Info['result']['today']['date_y'])
        self.Son3.config(text='星期:  ' + self.Info['result']['today']['week'])
        self.Son4.config(text='温度:  ' + self.Info['result']['today']['temperature'])
        self.Son5.config(text='天气:  ' +self.Info['result']['today']['weather'])
        self.Son5_1.config(text='风向:  ' + self.Info['result']['today']['wind'])
        self.Son6.config(text='穿衣指数:  ' + self.Info['result']['today']['dressing_index'])
        #self.Son7.config(text='穿衣建议:  ' + self.Info['result']['today']['dressing_advice'])
        self.Son8.config(text='舒适度指数:  ' + self.Info['result']['today']['comfort_index'])
        self.Son9.config(text='洗车指数:  ' + self.Info['result']['today']['wash_index'])
        self.Son10.config(text='晨炼指数:  ' + self.Info['result']['today']['exercise_index'])
        self.Son11.config(text='旅游指数:  ' + self.Info['result']['today']['travel_index'])
        self.Son12.config(text='干燥指数:  ' + self.Info['result']['today']['drying_index'])
        self.Son13.config(text='紫外线指数:  ' + self.Info['result']['today']['uv_index'])


        self.MainFrame.pack(padx=10, pady=30)

    def Back_2(self):
        self.MainFrame.pack()
        self.futureWeaFrame.pack_forget()

    def Future(self):
        test_Size_2=17
        laBelipadx=10
        laBelipady=5
        if not self.Info:
            messagebox.showwarning(title='警告',message='请您选中一个城市并点击查询按钮！')
            return





        self.futureWeaFrame=Frame(self.Top,bg='pink')
        # 定义跳转按钮
        self.butFrame=Frame(self.futureWeaFrame)

        self.BacKbut = Button(self.futureWeaFrame,bg='pink',font=("楷书", 21),text='返回',command=self.Back_2).pack(side='left')

        self.NextDayButton = Button(self.butFrame, text='后一天', bg='pink',font=("隶书", 21),command=self.JumpDate_go)
        self.PreDayButton = Button(self.butFrame, text='前一天', bg='green',font=("隶书", 21),command=self.JumpDate_back)
        self.PreDayButton.pack(ipadx=20, ipady=3, padx=10, pady=6, side='left')
        self.NextDayButton.pack(ipadx=20, ipady=3, padx=10, pady=6, side='left')
        self.butFrame.pack(side='top')

        self.daTe = Label(self.futureWeaFrame,text='星期：'+self.Info['result']['future'][self.FuTureDay]['week'],font=("华文行楷", test_Size_2))
        self.Temperature = Label(self.futureWeaFrame, text='温度：'+self.Info['result']['future'][self.FuTureDay]['temperature'], font=("华文行楷", test_Size_2))
        self.Weath = Label(self.futureWeaFrame, text='日期：'+self.Info['result']['future'][self.FuTureDay]['date'], font=("华文行楷", test_Size_2))
        self.weekDay = Label(self.futureWeaFrame, text='天气：'+self.Info['result']['future'][self.FuTureDay]['weather'], font=("华文行楷", test_Size_2))
        self.wiNd = Label(self.futureWeaFrame, text='风力向：'+self.Info['result']['future'][self.FuTureDay]['wind'], font=("华文行楷", test_Size_2))
        self.daTe.pack(ipadx=laBelipadx,ipady=laBelipady)
        self.Weath.pack(ipadx=laBelipadx, ipady=laBelipady)
        self.weekDay.pack(ipadx=laBelipadx, ipady=laBelipady)
        self.Temperature.pack(ipadx=laBelipadx, ipady=laBelipady)
        self.wiNd.pack(ipadx=laBelipadx, ipady=laBelipady)


        self.MainFrame.pack_forget()
        self.futureWeaFrame.pack()

    def JumpDate_go(self):
        self.FuTureDay+=1
        if self.FuTureDay>6:
            messagebox.showwarning(title='错误',message='错误的星期！您的请求与人类文明现有历法冲突，请返回！')
            self.FuTureDay-=1
        self.futureWeaFrame.pack_forget()
        self.Future()

    def JumpDate_back(self):
        self.FuTureDay-=1
        if self.FuTureDay<0:
            messagebox.showwarning(title='错误',message='错误的星期！您的请求与人类文明现有历法冲突，请返回！')
            self.FuTureDay += 1
        self.futureWeaFrame.pack_forget()
        self.Future()



if __name__ == '__main__':
    d=MianWindow()
    mainloop()