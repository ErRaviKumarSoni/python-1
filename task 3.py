'''
    Узнайте у пользователя число n.
    Найдите сумму чисел n + nn + nnn.
'''

n = 0
while  not((n > 0) and (n < 10)):
    n = abs(int(input('Введите положительное число от 1 до 9: ')))  # можно конечно еще на строку проверить не будем заморачиваться

lines = 3  # количество nnnnnn...
i = 2  # n уже знаем 
m = str(n)
while i <= lines:
    n +=  int(m * i)    
    i += 1

s = f'Получаем сумму: {n}'
print(s)
