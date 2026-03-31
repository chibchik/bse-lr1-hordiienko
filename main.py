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
    return math.sqrt(x)

print("Виберіть операцію:")
print("1. Сума")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")
print("5. Піднесення до степені")
print("6. Добуток квадратного кореня")

вибір = input("Ваш вибір: ")

число_1 = float(input("Введіть перше число: "))
число_2 = float(input("Введіть друге число: "))

if вибір == '1':
    print(число_1, "+", число_2, "=", add(число_1, число_2))
elif вибір == '2':
    print(число_1, "-", число_2, "=", subtract(число_1, число_2))
elif вибір == '3':
    print(число_1, "*", число_2, "=", multiply(число_1, число_2))
elif вибір == '4':
    print(число_1, "/", число_2, "=", divide(число_1, число_2))
elif вибір == '5':
    print(число_1, "^", число_2, "=", power(число_1, число_2))
elif вибір == '6':
    print("Квадратний корінь", число_1, "=", square_root(число_1))
else:
    print("Невірний вхід")