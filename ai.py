while True:
    s=input("C:\WINDOWS\>")
    if s.find("吗？")!=-1:
        ss=s.replace("吗？","！")
    else:
        ss=s+"！"
    print(ss)
