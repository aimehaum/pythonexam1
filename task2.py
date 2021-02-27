import random
a = random.randint(1, 20) 
n = 1

while n <= 5:
    numb = int(input("Введите какое-нибудь число: "))
    if numb < a:
        print("Слишком мало")
    elif numb > a:
        print("Слишком много")
    else:
        print("Класс! Вы угадали")
        break    
    n += 1
if numb != a:
    print("Все, вы не выиграли. Игра завершилась")
