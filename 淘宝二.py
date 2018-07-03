s1="——————————————欢迎进入手机淘宝————————————————"
s2="*******1 登录 ********"
s3="*******2 注册 ********"
s4="*******3 退出 ********"
s5="*******1 今日服装特卖 *********\n ******** 2 女士服装 *********\n ********3 男士服装 *********\n*******4 美食茶酒 *********\n *******5 结算 *********\n"
s6="******1 毛衫连衣裙 59元********\n ******2 运动鞋 69元********\n ******3 风衣 99元********\n"
s7="******1 咖啡 50元********\n ******2 零食大礼包 49元********\n ******3 柠檬 99元********\n"
def login():#定义登录函数
    i=1
    while i<=3:
        name=input("请输入用户名:")
        if name not in dict1.keys():
            print("用户名不存在，请先注册")
            shouye()
        password=input("请输入密码:")
        if name in dict1.keys() and dict1[name]==password:
            print("登录成功")
            xz()
            break
        else:
            print("密码或账户名错误，重新输入:")
        i=i+1
        if i==3:
            print("账户锁定")
            break

def register():#定义注册函数
    print("欢迎来到注册界面")
    username=input("请输入注册名:")
    if username in dict1.keys():
        print("用户名已存在，重新输入")
    else:
        password1=input("请输入注册密码:")
        dict1[username]=password1
        print("注册成功:")
        shouye()
        
    

def temai():
    print(s6)
    a=input("请输入购买编号:")
    if a=="1":
        dict["毛衫连衣裙"]=59
    if a=="2":
        dict["运动鞋"]=69
    if a=="3":
        dict["风衣"]=99
    print('购买成功，是否继续：y/n')
    bb=input()
    if bb=="y":
        women()
    elif bb=="n":
        print('当前加入购物车的商品是：')
        for i in dict.keys():
            print(i)
        xz()
def women():
    print(s6)
    a=input("请输入购买编号:")
    if a=="1":
        dict["裙子"]=29
    if a=="2":
        dict["内衣"]=59
    if a=="3":
        dict["裤子"]=89
    print('购买成功，是否继续：y/n')
    bb=input()
    if bb=="y":
        women()
    elif bb=="n":
        print('当前加入购物车的商品是：')
        for i in dict.keys():
            print(i)
        xz()
def man():
    print(s6)
    a=input("请输入购买编号:")
    if a=="1":
        dict["皮鞋"]=59
    if a=="2":
        dict["衬衫"]=79
    if a=="3":
        dict["休闲裤"]=159
    print('购买成功，是否继续：y/n')
    bb=input()
    if bb=="y":
        women()
    elif bb=="n":
        print('当前加入购物车的商品是：')
        for i in dict.keys():
            print(i)
        xz()
def meishi():
    print(s6)
    a=input("请输入购买编号:")
    if a=="1":
        dict["咖啡"]=50
        
    if a=="2":
        dict["零食大礼包"]=49
    if a=="3":
        dict["柠檬"]=99
    print('购买成功，是否继续：y/n')
    bb=input()
    if bb=="y":
        women()
    elif bb=="n":
        print('当前加入购物车的商品是：')
        for i in dict.keys():
            print(i)
        xz()
def jiesuan():
    
    for k,v in dict.items():
        print(k,v)
    print("本次消费金额为%d:"%sum(dict.values()))
    cc=input("谢谢使用淘宝，继续购物请按 W ,退出请按 0 ")
    dict.clear()
    if cc=="w":
        xz()
    elif cc=="0":
        shouye()
def xz ():
    print(s1)
    print(s5)
    c=input("请输入编号:")
    if c=="1":
        temai()
    if c=="2":
        women()
    if c=="3":
        man()
    if c=="4":
        meishi()
    if c=="5":
        jiesuan()
        
def shouye():
    while True:
        print(s1)
        print(s2)
        print(s3)
        print(s4)
        b=input("请输入功能编号:")
        if b=="1":
            login()
        if b=="2":
            register()
        if b=="3":
            print("退出淘宝")
        break    
dict1={}
dict={}
shouye()















    
