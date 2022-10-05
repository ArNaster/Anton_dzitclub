import random
random_number = random.randint(0, 100)
attempt = 0
print("Компьтер загадал число от 0 до 100, у тебя есть 10 попыток, чтобы отгадать его")

for i in range(1, 11):
    x = int(input("Введите число: "))
    if x > random_number:
        print('много')
    elif x < random_number:
        print('мало')
    else:
        print(f"Вы угадали число! Количество попыток - {i}")
        break
    attempt += 1
    print(f"Осталось попыток {10 - attempt}")
else:
    print(f"Вы исчерпали все попытки. Было загадано число {random_number}")