import random
def BinarySearch(list, x):
    left =0
    right = len(list)-1
    while left <= right:
        mid = left + (right-left) // 2
        if list[mid] > x:
            right = mid -1
        elif list[mid] == x:
            return mid
        else:
            left = mid +1
    return -1

list = []
for i in range(0,10):
    number = random.randint(1,100)
    list.append(number)
for i in range(0, len(list)):
    print(f"{list[i]}", end=" ")
list.sort()
while True:
    try:
        x = int(input("\nNhập số cần tìm: "))
        ket_qua = BinarySearch(list, x)
        if ket_qua != -1:
            print(f"Tìm thấy tại index: {ket_qua}")
            break
        else:
            print("No found!!")
            continue
    except ValueError:
        print("Nhập số cần tìm!!!")