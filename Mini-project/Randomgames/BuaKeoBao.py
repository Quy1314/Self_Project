import string
import random

def play(user_c, com_c):
    result =""
    if user_c == com_c:
        result = "hòa"
    elif user_c == "bua" and com_c == "keo" or user_c == "bao" and com_c == "bua" or user_c == "keo" and com_c == "bao":
        result = "thắng"
    else:
        result = "thua"
    return result


options = ["bua", "keo", "bao"]
com_c = random.choice(options)
usr_c = ""

while True:
    print(f"Đưa ra lựa chọn \n 1.bua\n 2.keo\n 3.bao")
    try:
        choice = int(input("Lựa chọn của bạn: "))
        usr_c = options[choice-1]
        break
    except ValueError:
        print(f"Nhập lại")
        continue

print(f"Lựa chọn của bạn: {usr_c}\n Lựa chọn của máy: {com_c} ")
print(f"Kết quả: {play(usr_c, com_c)}")