import pickle
from tkinter import messagebox #as msgbox


def Do(name,code_1,code_2):


    with open('UserData.txt','rb') as f:
        Dict=pickle.load(f)
        if name in Dict:
            messagebox.showwarning(title='警告',message='用户名已存在！')

            return

        print('测试 读取到')
        print(Dict)
    f.close()


    Dict[name]=code_1
    print('测试 添加后')
    print(Dict)

    with open('UserData.txt','wb') as f:
        pickle.dump(Dict,f)

    f.close()
    return 1