from random import randint

def guess_number(n = 10, min = 1, max = 100):
    print(f"Угадай число от {min} до {max} за {n} раз.")
    num = randint(min, max)
    for i in range(n):
        print("Введи число. Попытка № ", i + 1)
        while True: # бесконечный цикл, пока введено не число.
            try:
                guess = int(input())
                break
            except ValueError as e:
                print("Вы ввели не число. Попробуйте снова")
        if guess == num:
            print("Угадал! ", num)
            break
        if i == n-1:
            print("Не угадал. Ответ: ", num)
            break
        elif guess < num:
            print("Больше ;)")
        elif guess > num:
            print("Меньше ;)")

if __name__ == "__main__":
    guess_number(10, 1, 50)