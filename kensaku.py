import pandas as pd
import re
x = pd.read_csv('bunruidb.txt', encoding='shift-jis')
kensaku_go = input("検索する語を入力してください：")
kensaku_go = re.split("[　, ]", kensaku_go)

def kensaku(kensaku_go):
    bangou = 0
    print('\n')
    for i in range(len(x)):
        if (x.iloc[i][12] == kensaku_go[0]):
            bangou = bangou + 1
            print("{}番目：{}の検索結果を表示します。\n".format(bangou, kensaku_go[0]))
            print(x.iloc[i], '\n')
        elif (x.iloc[i][13] == kensaku_go[0]):
            bangou = bangou + 1
            print("{}番目：{}の検索結果を表示します。\n".format(bangou, kensaku_go[0]))
            print(x.iloc[i], '\n')

    if (bangou == 0):
        print("！{}は語彙目録には存在しない語です。".format(kensaku_go[0]))

def fukusuu_kensaku(kensaku_hairetu):
    bangou = 0
    print('\n')
    for i in kensaku_hairetu:
        for j in range(len(x)):
            if (x.iloc[j][12] == i):
                bangou = bangou + 1
                print("{}番目：{}の検索結果を表示します。\n".format(bangou, i))
                print(x.iloc[j], '\n')
            elif (x.iloc[j][13] == i):
                bangou = bangou + 1
                print("{}番目：{}の検索結果を表示します。\n".format(bangou, i))
                print(x.iloc[j], '\n')
        bangou = 0

    if (bangou == 0):
        print("！{}は語彙目録には存在しない語です。".format(i))

if (len(kensaku_go) <= 1):
    kensaku(kensaku_go)
else:
    fukusuu_kensaku(kensaku_go)
