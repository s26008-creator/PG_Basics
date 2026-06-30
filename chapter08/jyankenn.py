"""
   1...グー　2...チョキ　3...パー
"""

import random

rsp = ["","グー","チョキ","パー"]
you = int(input("じゃんけんぽん！(グー:1,チョキ:2,パー:3)->" )) 
computer = random.randint(1,3)
print("cpuの手",rsp[computer])
if you == 1:
    if computer == 1:
        print("あいこです")
    elif computer == 2:
        print("あなたの勝ちです")
    else:
        print("あなたの負けです")

elif you == 2:
    if computer == 1:
        print("あなたの負けです")
    elif computer == 2:
        print("あいこです")
    else:
        print("あなたの勝ちです")

elif you ==3:
    if computer == 1:
        print("あなたの勝ちです")
    elif computer == 2:
        print("あなたの負けです")
    else:
        print("あいこです")
else:
    print("1,2,3を入力")
