"""Игра угадай число
Компьютер сам загадывает и сам угадывает число, 
но должен это сделать меньше чем за 20 попыток
"""

import numpy as np


def fast_predict(number: int = 1) -> int:
    """ Компьютер сам угадывает случайное число за минимальное количество попыток.

    Args:
        number (int, optional): Случайное число которое мы загадали. Defaults to 1.

    Returns:
        int: Количество сделанных попыток
    """

    min = 1
    max = 101
    count = 0  # начальное количество попыток

    while True:
        count+=1
        mid = (min+max) // 2  # mid постоянно уменьшается вдвое, чтобы угадывание произошло быстрее
    
        if mid > number:
          max = mid
    
        elif mid < number:
          min = mid

        else:
            print(f"Компьютер угадал число за {count} попыток. Это число {number}")
            break  # выход из цикла, если число угадано
    return count


def score_game(fast_predict) -> int:
    """ Компьютер вычисляет, за какое среднее количество попыток он сможет угадать число при 1000 повторений алгоритма

    Args:
        fast_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []  # список в котором будут все количества попыток на каждом повторении алгоритма
    
    np.random.seed(1)  # сид для воспроизводимости
    
    random_array = np.random.randint(1, 101, size=(1000))  # загадывается массив случайных чисел

    for array_number in random_array:
        count_ls.append(fast_predict(array_number))

    score = int(np.mean(count_ls))  # собственно среднее значение
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")


if __name__ == "__main__":
    # RUN
    score_game(fast_predict) 