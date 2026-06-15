import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Попробуй угадать число от 1 до 100.")

secret = random.randint(1, 100)  
attempt = 0 

while True:
    user_guess = input("Введите ваше число: ") 
    attempt += 1

    if user_gess == secret:  
        print("Поздравляем, вы угадали число!")
        break
    elif user_guess > secret:  
        print("Ваше число больше загаданного.")
    elif user_guess < secret:  
        print("Ваше число меньше загаданного.")
