import random
pai=[]
for i in range(4,56):
    pai.append(i)
def choupai():
    bianhao=random.choice(pai)
    pai.remove(bianhao)
    dianshu=int(bianhao/4)
    if dianshu==1:
        paidian="A"
    elif dianshu==11:
        paidian="J"
    elif dianshu==12:
        paidian="Q"
    elif dianshu==13:
        paidian="K"
    else:
        paidian=str(dianshu)
    if bianhao%4==0:
        huase="黑桃"
    elif bianhao%4==1:
        huase="红桃"
    elif bianhao%4==2:
        huase="梅花"
    else:
        huase="方块"
    if dianshu>10:
        dianshu=10
    print("抽到的牌是",huase,paidian,"，点数为",dianshu)
    return dianshu
print("21点游戏正式开始")
wj=0
while True:
    dianshu=choupai()
    wj+=dianshu
    print("玩家当前点数为",wj)
    if wj>=21:
        break
    tingpai=input("是否继续抽牌？(y/n)")
    if tingpai=="n" or tingpai=="N":
        break
print("玩家总点数为",wj,end="")
if wj>21:
    print("，爆了！")
input("按回车键结束")
