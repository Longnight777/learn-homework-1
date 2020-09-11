"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def Average(scores): # функция нахождения среднего арифметического суммы значений списка
        return sum(scores) / len(scores)

def main():
    
    list_of_dictionaries = [ 
        {'school_class': '1a', 'scores': [3,4,4,5,2]}, 
        {'school_class': '1b', 'scores': [4,4,3,5,5]}, 
        {'school_class': '1c', 'scores': [5,2,5,4,3]}, 
        {'school_class': '2a', 'scores': [3,2,3,4,2]},
        {'school_class': '2b', 'scores': [5,5,4,5,5]},
        {'school_class': '2c', 'scores': [4,3,4,5,3]}]

    average_score_for_the_class = 0 # начальное значение переменной для класса
    average_score_for_the_school = 0 # начальное значение переменной для школы

    print()

    for dictionary in list_of_dictionaries: # в цикле идем по словарям в списке
        average_score_for_the_class = Average(dictionary['scores']) #  на каждой итерации в словаре берем список с оценками класса по ключу "scores", кидаем его в функцию "Average", результат записываем в переменную
        average_score_for_the_school = average_score_for_the_school + average_score_for_the_class # на каждой итерации прибавляем среднюю оценку очередного класса к имеющейся сумме
        print(f"Средняя оценка учеников класса '{dictionary['school_class']}': {average_score_for_the_class}") # выводим результат для очередного класса

    print(f"\nСредняя оценка учеников школы {round(average_score_for_the_school / len(list_of_dictionaries), 1)}") # выводим результат для школы целиком, как частное суммы средних оценок всех классов
                                                                                                               # и кол-ва классов (кол-ва словарей в исходном списке)
    
if __name__ == "__main__":
    main()
