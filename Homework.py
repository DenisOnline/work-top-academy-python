import random


def game(choice, result):
    computer_choice = random.choice("кнб")
    print("Твой выбор – ", str.capitalize(choice))
    print("Компюьтер выбрал —", str.capitalize(computer_choice))
    if str.lower(choice) == computer_choice:
        print("Ничья")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")
    elif str.lower(choice) == "к" and computer_choice == "н":
        result["player"] += 1
        print("------Игрок победил------")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")
    elif str.lower(choice) == "к" and computer_choice == "б":
        result["computer"] += 1
        print("------Компьютер победил------")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")
    elif str.lower(choice) == "н" and computer_choice == "к":
        result["computer"] += 1
        print("------Компьютер победил------")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")
    elif str.lower(choice) == "н" and computer_choice == "б":
        result["player"] += 1
        print("------Игрок победил------")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")
    elif str.lower(choice) == "б" and computer_choice == "к":
        result["player"] += 1
        print("------Игрок победил------")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")
    elif str.lower(choice) == "б" and computer_choice == "н":
        result["computer"] += 1
        print("------Компьютер победил------")
        print("Счёт, Компьютер", result["computer"], "—", result["player"], "Игрок")


print("------Добро пожаловать------")
print("------Вы зашли в игру \"Камень, Ножницы, Бумага\"------")
print("------Давай вспомним правила------")
print("------Камень побеждает ножницы ------")
print("------Ножницы побеждают бумагу------")
print("------Бумага побеждает камень------")
print("------Да начнется игра------")
print("------Удачи!------")

result = {"computer": 0, "player": 0}
while True:
    choise = input("Выбери К/Н/Б – ")
    game(choice=choise, result=result)