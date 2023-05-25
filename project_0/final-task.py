import numpy as np

def lion_catching_predict(number:int=1) -> int:
    """Угадываем число методом "ловли льва в пустыне" (Больцано—Вейерштрасса)

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
        
    """
    lst = list(range(1,101))
    count = 0    # Счетчик

    while True:    # Бесконечный цикл
        count += 1
        # Определяем predict_number как середину списка lst
        predict_number = lst[len(lst)//2]
                
        # Если угадали - останавливаем цикл,
        # если загаданное число меньше — переносим нижнюю границу списка на загаданное число,
        # если загаданное число больше — переносим верхнюю границу списка на загаданное число 
        if number == predict_number:
            break
        elif number > predict_number:
            lst = lst[(len(lst)//2):]
        else:
            lst = lst[:(len(lst)//2)]
            
    return(count)

print(f'Количество попыток: {lion_catching_predict()}')


def score_game(lion_catching_predict) -> int:
    """За какое количество попыток в среднем из 1000 алгоритм угадает загаданное число

    Args:
        lion_catching_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
        
    """
    count_ls = []    # Список для сохранения количества попыток
    np.random.seed(1)    # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))    # Список загаданных чисел

    # С помощью цикла добавляем в список count_ls количество попыток
    for number in random_array:
        count_ls.append(lion_catching_predict(number))

    score = int(np.mean(count_ls))    # Среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# Запуск
score_game(lion_catching_predict)    # Аргумент - функция
