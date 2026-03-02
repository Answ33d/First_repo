import time

for num in range(1000, 0, -7):
    print(num)
    time.sleep(0.05)

status = input("Ты долбоеб? ").lower()

while status != "да":
    print("Неправильный ответ. Пошел нахуй")
    time.sleep(0.5)
    status = input("Попробуем еще раз. Ты гуль? ").lower()

print("Ты настоящий гуль.")