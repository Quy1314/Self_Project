import random
def makeQuestion(secret):
    lens = len(secret) // 2
    result = ""
    guessed_list = []
    for i in range(0, len(secret)):
        guessed_list.append("_")
    for i in range(0,lens,1):
        while True:
            ran_num = random.randint(0,len(secret)-1)
            if secret[ran_num] != "_":
                temp = secret[ran_num]
                guessed_list[ran_num] = temp
                break
    for i in range(0, len(guessed_list)):
        result+=guessed_list[i]
    return result

def play(question,stages,secret):
    question_list = list(question)
    life_point = 6
    while life_point>0:
        if secret == "".join(question_list):
            print(f"Congratultion, your secret is: {secret}")
            break
        guess_w =""
        while True:
            print(" ".join(question_list))
            print(f"Your heart left: {life_point}")
            guess_w = input("Nhập kí tự dự đoán: ").upper()
            if len(guess_w) != 1:
                print("Đoán 1 kí tự!!")
                continue
            correct = False
            for i in range(0,len(secret)):
                if guess_w == secret[i] and question_list[i] == "_":
                    question_list[i] = guess_w
                    correct = True
            if correct == True:
                break
            else:
                life_point -= 1
                print(stages[6 - life_point])
                break

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', r'''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
wordlist= []
with open("wordlist.txt", encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        line = line.upper()
        wordlist.append(line)
secret = random.choice(wordlist)
question = makeQuestion(secret)
play(question, stages, secret)
