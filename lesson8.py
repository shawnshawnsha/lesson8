n  = input("幾顆蘋果?")
m = input("一顆幾塊?")
o = 0
x = ("選擇")
i = m 
while x != "d":
    print("進貨(a)") 
    print("--------")
    print("出貨(b)")
    print("--------")
    print("營業額(c)")
    print("--------")
    print("退出 (d)")
    print("--------")
    x = input("選擇")
    if x == "a":
        y = input("進多少顆?")
        n = int(n)+int(y)
        print("你有" , n , "蘋果")
        print("----------------")
    elif x == "b":
        z = input("賣多少顆")
        n = int(n)-int(z)
        o = int(z)*int(m)+int(o)
        print("你還有", n ,"蘋果")
        print("你有" ,int(z)*int(m) , "塊錢")
        print("----------------")
    elif x == "c":
        print("你有" ,o, "塊錢")
        print("-----------------")
    elif x == "d":
        print("謝謝使用!")
    else:
        print("錯誤")
        print("--------------")

