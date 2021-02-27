some_string = str(input("Введите строку, нечетной длины больше 7 символов:"))

if len(some_string) < 7 or len(some_string) % 2 ==0:
    print("Введите другое слово!")
    
else:
    a = len(some_string) // 2 
    print(some_string[a-1:a+2])


