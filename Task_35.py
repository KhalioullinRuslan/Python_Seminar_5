# Задача №35. 
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

n = int(input('Введите число: '))

def checkDel(value, oldCheck):
    if (value >= n):
        return oldCheck
    oldCheck = oldCheck and (n % value != 0)
    return checkDel(value +1, oldCheck)

check = checkDel(2, True)
print(check)
