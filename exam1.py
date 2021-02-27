#task1
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31, 55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]

dictionary = {}

for i in range(len(lst)):
    dictionary[i] = lst[i]
print(dictionary)

#task2
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

#task3
some_string = str(input("Введите строку, нечетной длины больше 7 символов:"))

if len(some_string) < 7 or len(some_string) % 2 ==0:
    print("Введите другое слово!")
    
else:
    a = len(some_string) // 2 
    print(some_string[a-1:a+2])


#task4
str1 = "Aidana"
str2 = "Adilet"
i = 0
new_str = ""

while i < len(str1):
    new_str = new_str + str1[i]+str2[i]
    i += 1
print(new_str)