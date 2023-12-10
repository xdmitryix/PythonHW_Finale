import logging
import argparse
from time import time

# Добавьте к ним логирование ошибок и полезной информации. Также реализуйте возможность запуска из командной строки с передачей параметров.
# Данная промежуточная аттестация оценивается по системе "зачет" / "не зачет" "Зачет" ставится, если Слушатель успешно выполнил задание.
# "Незачет" ставится, если Слушатель не выполнил задание. Критерии оценивания:
# 1 - Слушатель написал корректный код для задачи, добавил к ним логирование ошибок и полезной информации.

# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем. На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.

# Пример использования На входе:
# date_to_prove = 15.4.2023

# На выходе:
# True

# На входе:
# date_to_prove = 31.6.2022

# На выходе:
# False


def func_one(dta) -> bool:
    """
    Функция определяет корректна ли дата.
    :param dta:
    :return: True/False
    """
    try:
        day, month, year = map(int, dta.split('.'))
    except ValueError as e:
        print(f'Ввод данных пользователя привел к ошибке {e}')
        logging.critical(f"Ввод данных пользователя привел к ошибке {e}. Введено значение: {dta}")
        return False
    if year in range(1, 10000) and month in range(1, 13):
        if month in [1, 3, 5, 7, 8, 10, 12] and day in range(1, 32):
            logging.info(f'год {dta} является корректным.')
            return True
        elif month in [4, 6, 9, 11] and day in range(1, 31):
            logging.info(f'год {dta} является корректным.')
            return True
        elif month == 2:
            if year % 4 == 0 and year % 100 != 0:
                if day <= 29:
                    logging.info(f'год {dta} является корректным.')
                    return True
            elif year % 400 and year % 100 == 0:
                if day <= 29:
                    logging.info(f'год {dta} является корректным.')
                    return True
            else:
                if day <= 28:
                    logging.info(f'год {dta} является корректным.')
                    return True
    logging.error(f'год {dta} НЕ является корректным!')
    return False

if __name__ == '__main__':
    dta = input('введите дату в формате: день.месяц.год\n')
    logging.basicConfig(filename='my_log.log',
                        format= "%(levelname)s - %(asctime)s - ФУНКЦИЯ: %(funcName)s. СТРОКА: %(lineno)d. СООБЩЕНИЕ: %(message)s",
                        filemode='a',
                        encoding='utf-8',
                        level=logging.INFO)
    parser = argparse.ArgumentParser(description='argument date')
    parser.add_argument('-date', type=str, help='Here are the days, the month and the year')
    args = parser.parse_args()
    print(args)
    print(func_one(dta))
