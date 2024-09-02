while True:
    try:
        a= int(input("Введите первую циферку: "))
        b= int(input("Введите вторую циферку: "))
        act = input("Выберите дальнейшее действие: (+, -, *, /,):")
    except:
        print("Упс, что-то не так")
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
   
