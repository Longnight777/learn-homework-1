"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def string_comparison(string_1_def, string_2_def): #функция

    if not (isinstance(string_1_def, str) and isinstance(string_2_def, str)):
        return 0        
    if string_1_def == string_2_def:
        return 1   
    if string_1_def != string_2_def and len(string_1_def) > len(string_2_def):
        return 2
    if string_1_def != string_2_def and string_2_def == "learn":
        return 3   

def main():
   
    print(string_comparison("2", 4))
    print(string_comparison("python", "python"))
    print(string_comparison("learning", "python"))
    print(string_comparison("Hi", "learn"))

if __name__ == "__main__":
    main()
    