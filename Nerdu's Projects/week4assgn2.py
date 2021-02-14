c = 9
b = 9
a = 9

while c>0:
    rem = (c*3)%10
    if c == rem:
        break
    else: 
        c -= 1
    continue

carry1 = (c * 3)//10

while b > 0:
    rem1 = (b * 3) % 10
    if c == rem1 + carry1:
        break
    else:
        b-=1
    continue

carry2 = (b * 3)//10
while a > 0:
    rem2 = (a * 3) % 10
    if c == rem2 + carry2:
        break
    else:
        a-=1
    continue

print (f"The solution is {a}{b}{c}")