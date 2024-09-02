while True:
    try:
        a= int(input("Введите первое число: "))
        b= int(input("Введите второе число: "))
        act = input("Выберите дальнейшее действие: (+, -, *, /, **, S):")
    except:
        print("Ошибка")
    if act == '+':
        print(a+b)
        break
    elif act == '-':
        print(a-b)
        break
    elif act == '*':
        print(a*b)
        break
    elif act == '/':
        print(a/b)
        break
    elif act == '**':
        print(a**b)
        break
    elif act == 'S':
         s = int(a)**(0.5)
         answe = (b)**(0.5)
         print(s,answe)
         break
