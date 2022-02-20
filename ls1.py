#задание 1
name = 'Anna'
age = 24
sex = 'female'
print('name:', name , 'age:', age , 'sex:', sex, )
name = input('Введите имя')
age = int(input('Введите возраст'))
sex = input('Введите пол')
print( name, age, sex)

# # #задание2
time = int(input('Введите время в секунды'))
hour = time // 3600
sec = time % 3600
min = sec // 60
sec =  sec % 60
print(f'чч : {hour} мм: {min} сс: {sec}')

# #задача 3
n = int(input("Введите число:"))
n0 = str(n)
n1 = n0 + n0
n2 = n0 + n0 + n0
s = n + int(n1) + int(n2)
print('Сумма чисел n+nn+nnn', s)

# #Задание 4
n = int(input('Введите число:'))
m = n % 10
print(m)
while n >= 1:
    n = n//10
    print(n)
    if n % 10 > m:
        print(n)
        print(m)
        m = n % 10
        print(m)
    elif n > 9:
        break
print('Максимальная цифра в числе:', m)

#Задание 5
a = float(input('Введите выручку:'))
b = float(input('Введите издержки:'))
if a > b:
    print('Выручка больше издержек')
elif a < b:
    print('Выручка больше издержек')

