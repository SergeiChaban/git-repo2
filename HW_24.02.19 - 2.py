
# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;

userAnswerArr = []
number = ["первое", "второе"]
i = 0
n = 2
print("Последовательно введите два числа")
for i in range(n):
    userAnswerArr.append(int(input(("Введите " + number[i] + " число"),)))
print("Теперь " + number[i-1] + " число", userAnswerArr[1])
print("Теперь " + number[i] + " число", userAnswerArr[0])