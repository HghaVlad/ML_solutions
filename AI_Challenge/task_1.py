A = int(input())
x = A
z = ''
i = 1
if x == 1:
    print(1)
    exit()

for i in range(9, 1, -1):
    while x % i == 0:
        x //= i
        z = str(i) + z

if x == 1:
    print(z)
else:
    print("лимитированная партия")