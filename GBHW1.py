x = 1
y = 2.5
z = 'bla-bla'
print(x,y,z)
num = int(input('enter num '))
print(num)
string = input('enter string ')
print(string)



a=int(input('enter num: '))
if a<0:
    print('error a<0')
else:
    h=str(a//3600)
    m=(a//60)%60
    s=a%60
    if m<10:
        m='0'+str(m)
    else:
        m=str(m)
    if s<10:
        s='0'+str(s)
    else:
        s=str(s)
    print(h+':'+m+':'+s)


n = int(input("Введите число n: "))
c = str(n)
a1 = c + c
a2 = c + c + c
s = n + int(a1) + int(a2)
print("Результат равен:", s)



i = int(input('Enter num: '))
r = -1
while i > 10:
    d = i % 10
    i //= 10
    if d > r:
        r = d
print(r)


pr = int(input("Enter proceed: "))
ol = int(input("Enter outlay: "))
if pr > ol:
    prof = pr-ol
    rent = prof/pr
    print(f"Great work. You have {prof} profitability.Your profitability is equal to {rent}")
    w = int(input("How many people work: "))
    print(f"{prof/w} for one worker")
elif pr == ol:
    print("You have reached zero")
else:
    print("Your company is operating at a loss")


a = float(input("Enter start: "))
b = float(input("Enter finish: "))
day = 1
if a > b:
    print(day)
while a < b:
    a = a + a/10
    day += 1
print(day)
