"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user_dict():

    user_ask = None
    dictionary = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Почему небо голубое?": "Потому что"}
    list_dict_keys = list(dictionary.keys())

    try:
        user_ask = input("\nПрограмма: Задай мне вопрос\nПользователь: ")
    except KeyboardInterrupt:
        print ("Пока!")

    for key in list_dict_keys:
        if user_ask == key:
            print(f"Программа: {dictionary[key]}")

def ask_user():
    
    user_say = None

    while user_say != "Хорошо":
        try:    
            user_say = input("\nПрограмма: Как дела?\nПользователь: ")
        except KeyboardInterrupt:
            print ("Пока!")
            break

    if user_say == "Хорошо":        
        ask_user_dict()    
    
if __name__ == "__main__":
    ask_user()

