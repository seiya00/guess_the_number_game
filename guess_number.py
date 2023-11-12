import random
import sys

print("このゲームではユーザーが最小値と最大値を設定し、その中から生成されるランダムな数字を当てます")

min = int(input("最小値を設定してください\n"))
max = int(input("最大値を設定してください\n"))

while min >= max:
    print("最小値は最大値より必ず低く設定してください")
    min = int(input("最小値を設定してください\n"))
    max = int(input("最大値を設定してください\n"))

random_num = random.randint(min, max)
left = 5

while left > 0:
    user_input = int(input(f"数字を予測してください。制限回数は{left}回です。\n"))
    if user_input != random_num:
        if(left == 1):
            print("失敗！やり直してね")
        else:
            print("惜しい！")
        left -= 1
    else:
        print("正解です！")
        break



