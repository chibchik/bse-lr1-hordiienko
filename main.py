import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Помилка: ділення на нуль"

def power(x, y):
    return x ** y

def square_root(x):
    if x >= 0:
        return math.sqrt(x)
    else:
        return "Помилка: квадратний корінь від від'ємного числа"

def percentage(number, percent):
    """Обчислює введений відсоток від введеного числа"""
    return (number * percent) / 100
    

print("Виберіть операцію:")
print("1. Сума")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Піднесення до степені")
print("6. Добуток квадратного кореня")
print("7. Відсоток від числа")

вибір = input("Ваш вибір: ")

number_1 = float(input("Введіть перше число: "))
number_2 = float(input("Введіть друге число: "))

if вибір == '1':
    print(number_1, "+", number_2, "=", add(number_1, number_2))
elif вибір == '2':
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
elif вибір == '3':
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
elif вибір == '4':
    print(number_1, "/", number_2, "=", divide(number_1, number_2))
elif вибір == '5':
    print(number_1, "^", number_2, "=", power(number_1, number_2))
elif вибір == '6':
    print("Квадратний корінь", number_1, "=", square_root(number_1))
elif вибір == '7':
    print(number_2, "% від", number_1, "=", percentage(number_1, number_2))
else:
    print("Невірний вхід")