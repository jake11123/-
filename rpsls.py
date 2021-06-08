#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：周健
日期：2021年6月8日
"""
print("欢迎使用RPSLS游戏")
print("----------------")
print("石头/史波克/纸/蜥蜴/剪刀")
player_choice = input("请输入您的选择:")
print(player_choice)  # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice
print("----------------")
choice_name = input()
if player_choice == '石头':
    player_choice_number = 0      # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number
    print('您的选择为：石头')
elif player_choice == '史波克':   # 利用if/elif/else 语句，根据 RPSLS 规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果
    player_choice_number = 1
    print('您的选择为：史波克')
elif player_choice == '纸':
    player_choice_number = 2
    print('您的选择为：纸')
elif player_choice == '蜥蜴':
    player_choice_number = 3
    print('您的选择为：蜥蜴')
elif player_choice == '剪刀':
    player_choice_number = 4
    print('您的选择为：剪刀')
else:
    print('Error: No Correct Name')

from random import randrange       # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number
comp_number = int(randrange(0,4))    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象
if comp_number == 0:
    print('计算机的选择为：石头')      # 在屏幕上显示计算机选择的随机对象
if comp_number == 1:
    print('计算机的选择为：史波克')
if comp_number == 2:
    print('计算机的选择为：纸')
if comp_number == 3:
    print('计算机的选择为：蜥蜴')
if comp_number == 4:
    print('计算机的选择为：剪刀')

# 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”
if player_choice_number != comp_number:
    if (player_choice_number == 0 and (comp_number == 3 or comp_number == 4)) or (player_choice_number == 1 and (comp_number == 0 or comp_number == 4)) or (player_choice_number == 2 and (comp_number == 0 or comp_number == 1)) or (player_choice_number == 3 and (comp_number == 2 or comp_number == 1)) or (player_choice_number == 4 and (comp_number == 3 or comp_number == 2)):
        print("您赢了")
    else:
        print("计算机赢了")
else:
    print('您和计算机出的一样呢')
