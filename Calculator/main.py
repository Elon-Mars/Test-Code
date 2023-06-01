import math
import numpy as np


def get_help():
    print('\n\tКалькулятор может выполнять следующие математические операции:\n\tДеление (/), умножение (*), '
          'вычитание (-), сложение (+), возведение в квадрат (**), возведение в степень n - (**n).\n\tКалькулятор '
          'способен выполнить следующие тригонометрические функции:\n\tТангенс n - (tgn), синус n - (sinn), '
          'косинус n - (cosn), а также извлекать корень - (sqrtn)')
    print('\n\tВарианты записи: \n\t1. 5+5+n, за место "+" можете подставить любое математическое действие\n\t1.1 '
          '5(n), за место 5и(n) можете подставить любое числовое значение\n\t2. cos90, за место "cos" можете подставить'
          'любое тригонометрическое действие\n')


def calculate(user):
    # Create containers for user request filters by component
    container_words, container_numbers, container_func = '', '', ''
    # Creating parameters to filter a user request
    func_list = np.array(['+', '-', '*', '/', '**'])
    command_list = np.array(['cos', 'sin', 'tg', 'sqrt'])
    # Create a variable to store the filter values to determine the logic for further calculations
    bool_list = [0, 0, 0]
    # Break down the user query into its components: symbols, numbers, words
    for obj in user.replace(' ', ''):
        if obj.isalpha():
            container_words += obj
        elif obj.isnumeric():
            container_numbers += obj
        elif obj.isascii():
            container_func += obj

    # Check the query against the set filter parameters and apply the value settings to the filter. Lines 26 - 39
    # Checking a mathematical function in a request
    for item in container_func:
        if item in func_list:
            bool_list[0] = 1

    # Checking the word and its correctness in the query
    if container_words in command_list:
        bool_list[1] = 1
    # Without this condition, print(5+5) and other queries will be correct and bypass the basic program logic
    elif container_words not in command_list and container_words != '':
        bool_list[1] = -1

    # Checking for numbers
    if container_numbers.isalnum():
        bool_list[2] = 1

    # Calculate according to the values applied to the filter
    match bool_list:
        # Mathematical calculations
        case 1, 0, 1:
            try:
                result = eval(user.replace(' ', ''))
                print(f'\tРезультат вычисления: {result}')
            except:
                if container_func == func_list[4]:
                    print(f'\tРезультат вычисления: {float(container_numbers) ** 2}')
                else:
                    print('\tНекорректно указано значение')
        # Trigonometric calculations
        case 0, 1, 1:
            if container_words == command_list[0]:
                print(f'\t{round(math.cos(float(container_numbers)), 3)}')
            elif container_words == command_list[1]:
                print(f'\t{round(math.sin(float(container_numbers)), 3)}')
            elif container_words == command_list[2]:
                print(f'\t{round(math.tan(float(container_numbers)), 3)}')
            elif container_words == command_list[3]:
                print(f'\t{round(math.sqrt(float(container_numbers)), 3)}')
        case 1, -1, 1:
            # This "Case" deals with the condition of filtering expressions that work around the basic logic of the
            # programme
            print('\tНекорректно указано значение')
        case _:
            print('\tНекорректно указано значение')


def main():
    while True:
        user_request = input('\tВведите запрос: ')
        match user_request.lower():
            case 'exit':
                break
            case 'help':
                get_help()
            case _:
                calculate(user_request)


if __name__ == '__main__':
    print('\n\tДля выхода введите - "exit"\n\tДля вызова меню помощи введите - "help"')
    main()
