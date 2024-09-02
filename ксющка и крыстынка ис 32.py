while True:
    try:
        a= int(input("Введите первое число: "))
        b= int(input("Введите второе число: "))
        act = input("Выберите дальнейшее действие: (+, -, *, /, **):")
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
