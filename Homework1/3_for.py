"""
Домашнее задание №1
Цикл for: Оценки
* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def avg(scores): # функция нахождения среднего арифметического суммы значений списка
    return sum(scores) / len(scores)

def main():
    
    list_of_dictionaries = [ 
        {'school_class': '1a', 'scores': [3,4,4,5,2]}, 
        {'school_class': '1b', 'scores': [4,4,3,5,5]}, 
        {'school_class': '1c', 'scores': [5,2,5,4,3]}, 
        {'school_class': '2a', 'scores': [3,2,3,4,2]},
        {'school_class': '2b', 'scores': [5,5,4,5,5]},
        {'school_class': '2c', 'scores': [4,3,4,5,3]}]

    avg_class_score = 0 
    avg_school_score = 0 

    for dictionary in list_of_dictionaries: # в цикле идем по словарям в списке
        avg_class_score = avg(dictionary['scores']) 
        avg_school_score = avg_school_score + avg_class_score # прибавляем среднюю оценку класса к сумме
        print(f"Средняя оценка учеников класса '{dictionary['school_class']}': {avg_class_score}")

    print(f"\nСредняя оценка учеников школы {round(avg_school_score / len(list_of_dictionaries), 1)}")
    
if __name__ == "__main__":
    main()
