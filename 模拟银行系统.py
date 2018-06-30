"""

用户： 属性：名字 手机号 身份证 卡

卡 ：属性 卡号 密码 余额 是否锁定m

ATM ：属性： 用户列表（存储开卡人信息）

     行为 ：开户 查询 存款 取款 转账 改密码 锁定 解锁 销户


管理员： 属性： 用户名 密码

        行为： 登录
"""
import random
import sys
import time
class User:
    def __init__(self,name,phone,id_card,card):
        self.name=name
        self.phone=phone
        self.id_card=id_card
        self.card=card

class Card:
    def __init__(self,card_number,password,yu):
        self.car_number=card_number
        self.password=password
        self.yu=yu
        self.islock=False

class Atm:
    def __init__(self):
        self.user_list={}
    def public(self):
        search = int(input("请输入卡号:"))
        object = self.user_list.get(search)
        if object.card.islock == True:  # 查询输入的卡号是否与存入字典的键匹配
            print("此卡已锁定，无法操作")
            return False

        if object == None:
            print("卡号不存在")
            return False
        for i in range(3):
            pwd = input("请输入密码")
            if pwd != object.card.password:
                print("密码错误，你还有%d次机会" % (2 - i))
                continue
            else:
                break
        else:
            print("三次机会已经用完，卡已锁定")
            object.card.islock = True
            return False
        return object

    def show(self):
        print(" ********************************** ")
        print("*  1.开户         2.查询            *")
        print("*  3.存款         4.取款            *")
        print("*  5.转账         6.改密            *")
        print("*  7.锁卡         8.解锁            *")
        print("*  9.销户         t.退出            *")
        print(" ********************************** ")
    def kaihu(self):
        name=input("请输入开户名:")
        phone=input("请输入电话号码:")
        id_card=input("请输入身份证号:")
        card_number=random.randint(1000000,99999999)
        password=input("请输入开户密码:")
        password1=input("请再次确认密码:")
        if password!=password1:
            print("两次密码输入不一样,开户失败")
            return False
        yu=int(input("请输入存入金额不能低于10元:"))
        if yu <10:
            print("账户余额少于十开户失败")
            return False
        card=Card(card_number,password,yu)
        user=User(name,phone,id_card,card)
        self.user_list[card_number]=user#将卡号作为键，用户对象作为有一个整体作为值，存入字典中。
        print("开户成功，您的卡号是",card_number)
        print("余额为:",yu)
        return False

    def chaxun(self):
        object1=self.public()
        if object1!=False:
            print("余额为:",object1.card.yu)

        pass
    def cunkuan(self):
        object1 = self.public()
        if object1 != False:
            a=int(input("请输入存款金额"))
            object1.card.yu+=a
            print("存款成功余额为",object1.card.yu)

    def qukuan(self):
        object1 = self.public()
        if object1 != False:
            a = int(input("请输入取款金额"))
            object1.card.yu -= a
            print("取款成功余额为", object1.card.yu)

    def zhuanzhang(self):
        object1 = self.public()
        if object1 != False:
            a=int(input("请输入转账卡号"))
            card2 = self.user_list.get(a)
            if card2.card.islock == True:  # 查询输入的卡号是否与存入字典的键匹配
                print("此卡已锁定，无法操作")
                return False
            if card2 == None:
                print("卡号不存在")
                return False
            b=int(input("请输入转账金额"))
            if b>object1.card.yu:
                print("余额不足无法转账")
                return False
            d=object1.card.yu-b
            e=card2.card.yu+b
            print("转账成功,转账%d当前余额为%d"%(b,d))

    def gaimi(self):
        object1 = self.public()
        if object1 != False:
            a=input("请输入旧密码")
            b=input("请输入新密码")
            c=input("请确认密码")
            if a!=object1.card.password:
                print("输入旧密码错误")

            if a==b:
                print("旧密码不能与新密码相同")
                return False
            if b!=c:
                print("两次输入新密码不一致")
                return False


    def suoding(self):
        object1 = self.public()
        if object1 != False:
            object1.card.islock = True
            print("卡已手动锁定")


    def jiesuo(self):
        object1 = self.public()
        if object1 != False:
            object1.card.islock = False
            print("卡已手动解锁")
    def xiaohu(self):
        object1 = self.public()
        if object1 != False:
            self.user_list.clear()



class Admin:
    def __init__(self,username,password):
        self.usernmae=username
        self.password=password
    def login(self):
        loginName = input("请输入用户名:")
        loginPassword = input("请输入密码:")
        if loginName==self.usernmae and loginPassword==self.password:
            print(">>>>>>>>登录成功请稍后>>>>>>>")
            sys.exit()

def main():
    print("——————————————————欢迎进入平安银行————————————————————")
    admin=Admin("cbk","123")
    admin.login()
    atm =Atm()
    while True:
        atm.show()
        choice=input("请按提示操作")

        if choice=="1":
            atm.kaihu()


        if choice=="2":
            atm.chaxun()

        if choice == "3":
            atm.cunkuan()

        if choice == "4":
            atm.qukuan()

        if choice == "5":
            atm.zhuanzhang()

        if choice == "6":
            atm.gaimi()

        if choice == "7":
            atm.suoding()

        if choice == "8":
            atm.jiesuo()

        if choice == "9":
            atm.xiaohu()

        if choice == "t":
            print("退出")
            sys.exit()
main()
