num = int(input("Enter number: "))
num_copy = num

# 1 способ
reversed_num = 0

while num > 0:
    reversed_num *= 10
    reversed_num += num % 10
    num //= 10

print(reversed_num)

# 2 способ
reversed_num1 = int(str(num_copy)[::-1])
print(reversed_num1)