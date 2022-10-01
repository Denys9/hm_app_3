num1 = int(input('Введіть початкове число - '))
num2 = int(input('Введіть кінечне число - '))



if num1 < 3:
    num1 += (3 % num1)
elif num1 > 3:
    num1 = (num1 - (num1 % 3))+3
number = num1
while number <= num2:
    print(f"{number}")
    number += 3
if num1<5:
    num1 +=(5%num1)
elif num1>5:
    num1 = (num1 - (num1%5))+5
number4 = num1

while number4 <= num2:
    print(f'{number4}')
    number4 +=7