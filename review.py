import random

print("Добро пожаловать в игру 'Угадай число'!")
print("Попробуй угадать число от 1 до 100.")
user_guess = None
secret = random.randint(1, 100)  
attempt = 0 

while user_guess != secret:
    user_guess = input("Введите ваше число: ") 
    attempt += 1
    
    if user_guess > secret:  
        print("Ваше число больше загаданного. введите число меньше")
    elif user_guess < secret:  
        print("Ваше число меньше загаданного. введите число больше")
print(f"Поздравляем, вы угадали число! Количество попыток {attempt} было использовано")
