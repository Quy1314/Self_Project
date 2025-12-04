def PrintTask(tasks):
    for i, cv in enumerate(tasks, start=1):
        print(f"{i}. {cv}\n")

def InputTask(tasks):
    while True:
        cong_viec = input("Nhập task:")

        if cong_viec == "0":
            break
        tasks.append(cong_viec)

        

tasks = []

while True:
    print("--- MENU ---\n 1. Thêm công việc \n 2. Xem danh sách\n 3. Xóa công việc\n 4. Thoát")
    choice = int(input("Nhập lựa chọn(1-4): "))
    if choice == 1:
        InputTask(tasks)
    elif choice == 2:
        PrintTask(tasks)
    elif choice == 3:
        while True:
            try:
                remove_c = int(input("Chọn index để xóa (0 để dừng xóa): "))
                if 0<remove_c <= len(tasks):
                    cv = tasks.pop(remove_c-1)
                    print(f"Đã xóa công việc: {cv}")
                elif remove_c == 0:
                    break
            except ValueError:
                print("Index lớn hơn số công việc")
                continue
    elif choice == 4:
        print(f"Thoát chương trình!!!")
        break
        
    