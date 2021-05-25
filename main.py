import random 
import os


def check(letter,word):
    i = 0
    #
    for c in word:
        if c == letter:
            return i
        else:
            i+=1
    return -1
    #Функция находящия позицию буквы в слове


tries = 9 
#Количетсво попыток
errors = 0
#Кол-во ошибок
hits = 0
#Кол-во угаданных букв
words = ['харомы','топар','апеляцией','личность','водяный']
#Словарь слов
word = random.choice(words)
#Слово, выбирающеся из словоря слов с помощью функции random
guess = []
#Интерфейс
for i in range(len(word)):
    guess.append('_')
used = []
#Буквы, которые были использованы


while errors<tries:
 #Повтрояем следующие действия, пока кол-во ошибок не превысит кол-во попыток   
    
    os.system('cls')
    #Команда, очищающая консоль
    print(*guess)
    #Вывод интерфейса
    print(f"U have {tries-errors} tries of {tries} left")


    letter = input()
    #Буква, которую вводит игрок
    if not letter in used:
        #Проверяемя,есть ли буква в использованых словах 
        used.append(letter)
        #Запоминаем, что использовали букву
        if letter in word:
            #Провереям,есть ли буква в слове
            print("Right!")
            index = check(letter,word)
            #Находим позицию буквы в слове
            guess[index] = letter
            #Выводим букву в интерфейсе
            hits+=1
            #Увеличиваем кол-во угаданных букв на 1 
            if hits == len(word):
                os.system('cls')
                print(*guess)
                print("U won the game!!!")
                break
                #Ломает цикл
            #Если кол-во угаданных букву равно кол-ву букв в слове, то мы выйграли
        
        
        else:
            errors+=1
            #Если игрок ошибся увеличиваем кол-во допущенных ошибок
            print("Wrong!")
    
    
    else:
        #Если игрок использова букву выодит:
        print("U already used this letter!")
        input("press Enter!")
else:
    #Если игрок проигрыл выводит
    print("u lose")
    input("press Enter!")
    