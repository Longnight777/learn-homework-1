"""

Домашнее задание №1
Цикл while: ask_user
* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
*Доработайте ask_user() так, чтобы когда пользователь вводил 
  вопрос который есть в словаре, программа давала ему 
  соответствующий ответ. Например: 

  Пользователь: Что делаешь?
  Программа: Программирую

"""

def ask_user():
    
    user_say = None

    ASK_QUESTION = {"как дела": "Хорошо!", 
    "что делаешь": "Программирую", 
    "почему небо голубое": "Потому что"}

    KEYS_ASK_QUESTION = list(ASK_QUESTION.keys())

    while user_say != "хорошо":
        user_say = input("\nПрограмма: Как дела?\nПользователь: ").lower()

    user_ask = input("\nПрограмма: Задай мне вопрос\nПользователь: ").lower()

    for key in KEYS_ASK_QUESTION:
        if user_ask == key:
            print(f"Программа: {ASK_QUESTION[key]}")   
    
if __name__ == "__main__":
    ask_user()
    