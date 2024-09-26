number1 = int(input("Введите первое число: "))
number2 = int(input("Введите второе число: "))
result = (f"Числа равны: {number1} = {number2}" if number1 == number2
          else f"Наименьшее число: {min(number1, number2)}")
print(result) 