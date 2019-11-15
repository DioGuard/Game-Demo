import random

enemyHP = 10
damage = random.randint(1, 6)
s = ("sas",)

print("О нет! На вас напал грязный бомж!\nБейте его, пока он не отстанет!")
input("Дальше?\n")

while enemyHP > 0:
    enemyHP -= damage

    print("Ну и что ты мне сделаешь, а?")
    print("Чёрт, больно!")
    print("[Получает ", damage, " урона]")

    if damage == 6:
        print("Ай! Только не по носу!")

    damage = random.randint(1, 6)
    input("Дальше?\n")

print("Ладно-ладно, всё ухожу. Только не стукай.")