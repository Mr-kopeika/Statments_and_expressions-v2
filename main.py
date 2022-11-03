#Task 1
import random

print('Task 1')
first = random.randint(0, 100)
second = random.randint(0, 100)
third = random.randint(0, 100)
print(f'numbers: {first}, {second}, {third}')
print('Average: ', int((first + second + third)/3))

input('Press "Enter" to continue!')

#Task 2
print('Task 2')
first = random.randint(0, 100)
second = random.randint(5, 20)
print(f'numbers: {first}, {second}')
print(f'Result: {int(first/second)}  {first % second}')

input('Press "Enter" to continue!')

#Task 3
print('Task 3')
stringNumber = input('Write a float number: ')
number = float(stringNumber)
while(len(stringNumber) < 11):
    stringNumber = "0" + stringNumber

print(f' 1. {round(number, 2)}\n 2. {round(number)}\n 3. {stringNumber}')

#Task 4
print('Task 4')
n1 = int(input("Введите целое число: "))
n2 = 0

if n1 < 0:
    negative = 1
    n1= -n1

while n1 > 0:
    digit = n1 % 10
    n1 = n1 // 10
    n2 = n2 * 10
    n2 = n2 + digit

if negative == 1:
    n2 = -n2

print('"Обратное" ему число:', n2)