import datetime
import time
import winsound

h =0
m=0
s=0
while True:
    try:
        h = int(input("Nhập giờ: "))
        if h > 23 or h < 0:
            continue
        else:
            try:
                m = int(input("Nhập phút: "))
                if m >60 or m < 0:
                    continue
                else:
                    try:
                        s = int(input("Nhập giây: "))
                        if s >60 or s < 0:
                            continue   
                        else:
                            break
                    except ValueError:
                        continue
            except ValueError:
                continue
    except ValueError:
        continue

time_alarm = f"{h:02d}:{m:02d}:{s:02d}"
print(f"Báo thức lúc: {time_alarm}")

while True:
    now = datetime.datetime.now()
    curr = now.strftime("%H:%M:%S")
    print(curr, end= "\r")
    if curr == time_alarm:
        print("Wake upppppppp")
        winsound.Beep(2500, 1000)
        break
    time.sleep(1)