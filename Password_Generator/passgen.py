import string
import random
total_char = string.ascii_letters + string.digits + string.punctuation
print(f"Total chars: {total_char}, lens is: {len(total_char)}")

password = "" 
lens = 0
while True:
    try:
        lens= int(input("Length: "))
        break
    except ValueError:
        print(f"Input number!!")
        continue
for i in range(0,lens):
    ran_char= random.choice(total_char)
    password += ran_char
print(f"password is {password}")