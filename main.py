start = int(input("Введіть початкове число - "))
end = int(input("Введіть кінцеве число - "))
if start < 7:
    start += (7 % start)
elif start > 7:
    start = (start - (start % 7))+7
number = start
while number <= end:
    print(f"{number}")
    number += 7