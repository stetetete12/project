def get_number(prompt):
    """Запрашивает у пользователя ввод числа и обрабатывает ошибки ввода."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введено нечисловое значение. Попробуйте снова.")

def addition():
    """Выполняет сложение двух чисел."""
    num1 = get_number("Введите первое число для сложения: ")
    num2 = get_number("Введите второе число для сложения: ")
    print(f"Результат сложения: {num1} + {num2} = {num1 + num2}")

def subtraction():
    """Выполняет вычитание двух чисел."""
    num1 = get_number("Введите первое число для вычитания: ")
    num2 = get_number("Введите второе число для вычитания: ")
    print(f"Результат вычитания: {num1} - {num2} = {num1 - num2}")

def multiplication():
    """Выполняет умножение двух чисел."""
    num1 = get_number("Введите первое число для умножения: ")
    num2 = get_number("Введите второе число для умножения: ")
    print(f"Результат умножения: {num1} * {num2} = {num1 * num2}")

def division():
    """Выполняет деление двух чисел с обработкой деления на ноль."""
    num1 = get_number("Введите первое число для деления: ")
    num2 = get_number("Введите второе число для деления: ")
    try:
        result = num1 / num2
        print(f"Результат деления: {num1} / {num2} = {result}")
    except ZeroDivisionError:
        print("Ошибка: деление на ноль невозможно.")

def main():
    """Основная функция с меню выбора операций."""
    print("Добро пожаловать в консольный калькулятор!")
    while True:
        print("\nВыберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выйти")

        choice = input("Введите номер операции (1-5): ")

        if choice == '1':
            addition()
        elif choice == '2':
            subtraction()
        elif choice == '3':
            multiplication()
        elif choice == '4':
            division()
        elif choice == '5':
            print("Выход из программы. Спасибо за использование калькулятора!")
            break
        else:
            print("Ошибка: неверный выбор. Попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
