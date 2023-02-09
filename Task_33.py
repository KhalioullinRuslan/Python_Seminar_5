# Задача №33. 
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

from random import randint

n = int(input('Введите количество оценок: '))

grades = [randint(1, 5) for _ in range(n)]
print(grades)
max_grade = max(grades)
min_grade = min(grades)

i = 0
def change_grades(max_grade, min_grade, i):
    if i == len(grades):
        return grades
    else:
        if max_grade == grades[i]:
            grades[i] = min_grade
    return change_grades(max_grade, min_grade, i + 1)

print(change_grades(max_grade, min_grade, i))