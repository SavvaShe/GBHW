a = float(input("Enter start: "))
b = float(input("Enter finish: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)