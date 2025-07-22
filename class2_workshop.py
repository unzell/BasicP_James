def unicorn(val):
    if val >= 5:
        if val <= 50:
            print("10บาท")
        elif val <= 100:
            print("15บาท")
        elif val <= 300:
            print("25บาท")
        elif val <= 500:
            print("35บาท")
        else:
            print("45บาท")
    else:
        print("your order got canceled")

distance = int(input("ระยะทาง : "))
unicorn(distance)