num = int(input("Enter number: "))

limitMax = 2 ** 31
limitMin = limitMax * -1
flag = False
reversed_num = 0

if num < 0:
    num *= -1

while num > 0:
    reversed_num *= 10
    reversed_num += num % 10
    num //= 10

if flag:
    reversed_num *= -1

if limitMin < reversed_num < limitMax:
    print(reversed_num)
else:
    print(0)