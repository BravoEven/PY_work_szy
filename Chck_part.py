import  pickle

def Check(name,password):#接受  用户名和密码 返回数字形式的判断结果
    with open('UserData.txt','rb') as f:
        Dict=pickle.load(f)
        print(Dict)
    f.close()
    if name in Dict:
        if password == Dict[name]:
            return 1
        else:
            return 2
    else:
        return 3