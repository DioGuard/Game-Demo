#escape-последовательность \t, \n, \a, \r
import random

print("Моя закадать число, твоя должно отгадать! Отгадай!\n")

num = random.randrange(100) + 1
guess = int(input("Введи число: "))
cou = 1

while guess != num:

    if guess > num:
        print("Твоя число больши моей!")
    else:
        print("Твоя число менче моей!")

    guess = int(input("Опять введи число: "))
    cou += 1
print("Твоя отгодать моя число! Твоя потребоваться", cou, "попыток\n")

for _ in range(10):
    print("Молодец", end=" ")