def split(splitable: str, separator: str) -> list[str]:
    """
    разбивает строку на элеметы при помощи разделителя
    """
    lst = []
    buffer = ""
    for symbol in splitable:
        if symbol != separator:
            buffer += symbol
        else:
            lst.append(buffer)
            buffer = ""
    # добавляем последний элемент
    if buffer:
        lst.append(buffer)
    return lst

def equation(user_input: str) -> str: 
    """
    принмает на вход уравнение с тремя элементами и одним неизвестным разделенные пробелами и возвращает ответ
    """
    splitted = split(user_input, " ") # разбивает входное уравнение на элементы возвращая список элементов
    # x + y = z -> ["x", "+", "y", "=", "z"]
    x, y, z = None, None, None # обявляем переменые для хранения элементов

    operartion = splitted[1]

    if not splitted[0].isdigit():
        y = int(splitted[2])
        z = int(splitted[4])
        if operartion == "+":
            x = str(int(z) - int(y))
        elif operartion == "-":
            return "x = " + str(int(z) + int(y))
        elif operartion == "*":
            return "x = " + str(int(int(z) / int(y)))
        elif operartion == "/":
            return "x = " + str(int(z) * int(y))
        return splitted[0] + " = " + x

    if not splitted[2].isdigit():
        x = int(splitted[0])
        z = int(splitted[4])
        if operartion == "+":
            y = str(int(z) - int(x))
        elif operartion == "-":
            y = str(int(x) - int(z))
        elif operartion == "*":
            y = str(int(int(z) / int(x)))
        elif operartion == "/":
            y = str(int(x) // int(z))

        return splitted[2] + " = " + y

    if splitted[4] == "x":
        x = splitted[4]
        y = splitted[2]
        z = splitted[0]

        if operartion == "+":
            return "x = " + str(int(z) + int(y))
        elif operartion == "-":
            return "x = " + str(int(z) - int(y))
        elif operartion == "*":
            return "x = " + str(int(z) * int(y))
        elif operartion == "/":
            return "x = " + str(int(int(z) / int(y)))


if __name__ == "__main__":
    user_input = input("Введите уравнение: \n")
    result = equation(user_input)
    print(result)
    # x + 15 = 18 | 15 + x = 18 | 15 + 3 = x

# что можно улучшить ?
# 1. Сократить
# 2. Больше элементов
# 3. Больше неизвестных (системы уравнений)