score =0
question = []
with open("questions.txt",encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        data = line.split("|")
        question.append(data)
for i, ques in  enumerate(question, start=1):
    choice = -2
    print(f"{i}. {ques[0]}")
    print(f"1. {ques[1]}")
    print(f"2. {ques[2]}")
    print(f"3. {ques[3]}")
    while True:
        try: 
            choice = int(input("Nhập đáp án của bạn (1|2|3): "))
        except ValueError:
            print(f"Nhập số từ 1-3!!")
        if 1 <=choice <=3:
            if ques[choice] == ques[4]:
                score+=100
                print(f"Your point: {score}")
                break
            else:
                print("False answer!")
                break
        else:
            print("Nhập số từ 1-3!!")
            continue

print(f"Your final point: {score}")