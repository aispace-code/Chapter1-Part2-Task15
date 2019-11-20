num = int(input('Enter your age '))

for age in range(2, num, 2):
    if num % 2 == 0:
        print(age)
for age in range(1, num, 2):
    if num % 2 != 0:
        print(age)