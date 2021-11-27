#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ��Ÿ���
���ڣ�2021/11/27
"""

import random



# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��

def name_to_number(name):
    """
    ����Ϸ�����Ӧ����ͬ������
    """
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        return 1
    elif name=="ֽ":
        return 2
    elif name=="����":
        return 3
    elif name=="����":
        return 4
    else:
        print("Error: NoCorrectName")

def number_to_name(comp_number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if comp_number==0:
        return "ʯͷ"
    elif comp_number==1:
        return "ʷ����"
    elif comp_number==2:
        return "ֽ"
    elif comp_number==3:
        return "����"
    elif comp_number==4:
        return "����"


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    print("----------------")
    print("����ѡ��Ϊ:%s"%player_choice)
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    computer_result=number_to_name(comp_number)
    print("�������ѡ��Ϊ:%s"%computer_result)
    numbers=player_choice_number-comp_number
    if numbers==1 or numbers==2 or numbers==-3 or numbers==-4:
        print("��Ӯ�ˣ�")
    elif numbers==0:
        print("���ͼ��������һ����!")
    else:
        print("����Ӯ�ˣ�")
    '''
    �ɡ�������ն���棻����Ե�ֽ��ֽ����ʷ���ˣ�ʷ��������ʯͷ��
        �����ü�ֽ�����涾��ʷ���ˣ�ֽ����ʯͷ��
        ʯͷ�������棻ʷ���˴��������
        ʯͷ������������ã�
    ���û�Ӯ��������10�������(�û����������)
    ���Ϊ1�ģ�����(4)��������(3)������(3)����ֽ(2)��ֽ(2)����ʷ����(1)��ʷ����(1)����ʯͷ(0);
    ���Ϊ2�ģ�����(4)����ֽ(2)������(3)����ʷ����(1)��ֽ(2)����ʯͷ(0);
    ���Ϊ-3�ģ�ʯ(0)��������(3)��ʷ(1)��������(4);
    ���Ϊ-4�ģ�ʯͷ(0)��������(4);
    ��֮�����Ӯ(������Ϊ0����ʾ�����ͼ��������һ���أ���)
    '''


print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)

