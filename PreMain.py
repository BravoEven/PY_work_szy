from tkinter import *
from tkinter import messagebox #as msgbox
from tkinter import ttk
from S import MianWindow


class StartWindow(object):
    def __init__(self):
        self.Top=Tk()
        self.Top.title('主窗口')
        self.TestBut=Button(self.Top,text='测试',bg='pink',command=self.Go).pack()



    def Go(self):
        d=MianWindow()





if __name__ == '__main__':
     d=StartWindow()
     mainloop()