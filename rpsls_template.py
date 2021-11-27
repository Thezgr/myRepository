#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：张高荣
日期：2021/11/27
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """
    if name=="石头":
        return 0
    elif name=="史波克":
        return 1
    elif name=="纸":
        return 2
    elif name=="蜥蜴":
        return 3
    elif name=="剪刀":
        return 4
    else:
        print("Error: NoCorrectName")

def number_to_name(comp_number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if comp_number==0:
        return "石头"
    elif comp_number==1:
        return "史波克"
    elif comp_number==2:
        return "纸"
    elif comp_number==3:
        return "蜥蜴"
    elif comp_number==4:
        return "剪刀"


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    print("----------------")
    print("您的选择为:%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    computer_result=number_to_name(comp_number)
    print("计算机的选择为:%s"%computer_result)
    numbers=player_choice_number-comp_number
    if numbers==1 or numbers==2 or numbers==-3 or numbers==-4:
        print("您赢了！")
    elif numbers==0:
        print("您和计算机出的一样呢!")
    else:
        print("机器赢了！")
    '''
    由”剪刀腰斩蜥蜴；蜥蜴吃掉纸；纸反驳史波克；史波克蒸发石头；
        剪刀裁剪纸；蜥蜴毒死史波克；纸包裹石头；
        石头砸死蜥蜴；史波克打碎剪刀；
        石头砸碎剪刀；“得：
    若用户赢，有以下10种情况：(用户——计算机)
    相减为1的，剪刀(4)——蜥蜴(3)、蜥蜴(3)——纸(2)、纸(2)——史波克(1)、史波克(1)——石头(0);
    相减为2的，剪刀(4)——纸(2)、蜥蜴(3)——史波克(1)、纸(2)——石头(0);
    相减为-3的，石(0)——蜥蜴(3)、史(1)——剪刀(4);
    相减为-4的，石头(0)——剪刀(4);
    反之计算机赢(如果相减为0则显示”您和计算机出的一样呢！“)
    '''


print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
player_choice=input()
rpsls(player_choice)

