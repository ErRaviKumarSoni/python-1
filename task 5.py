'''
    Запросите у пользователя значения выручки и издержек фирмы. 
    Определите, с каким финансовым результатом работает фирма 
    (прибыль — выручка больше издержек, или убыток — издержки 
    больше выручки). Выведите соответствующее сообщение. 
    Если фирма отработала с прибылью, вычислите рентабельность выручки 
    (соотношение прибыли к выручке).
    Далее запросите численность сотрудников фирмы и определите прибыль фирмы
    в расчете на одного сотрудника.
'''

r = int(input("Пожалуйста, введите значения выручки: "))  # r - revenue
c = int(input("Пожалуйста, введите значения издержек фирмы: "))  # c - cost

if r >= c:
    p = r - c  # p - profit
    s = f'Прибыль фирмы будет: {p}'
    if r > c:
        pb = c / r  # pb - profitability
        s = s + '\n' + f'Рентабельность фирмы будет: {pb:5g}'
        size = int(input("Пожалуйста, введите численость сотрудников: "))
        p_size = p / size
        s = s + '\n' + f'Прибыль на одного сотрудника: {p_size:5g}'

else:
    l = c - r  # l - loss
    s = f'Убыток фирмы будет: {l}'
    
print(s)