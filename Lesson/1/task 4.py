'''
    Пользователь вводит целое положительное число.
    Найдите самую большую цифру в числе.
    Для решения используйте цикл while и арифметические операции.
'''
n = abs(int(input('Пожалуйста, введите целое положительное число: '))) 
m = n
n_max = 0
while True:    
    remains = m % 10  # 7 % 10 = 7
    m = m // 10  # 32 // 10 = 3
    if remains > n_max:
        n_max = remains
    if remains == 9 or m == 0:
        break

s = f'Самая большая цифра в этом числе {n}, будет {n_max}'
print(s)