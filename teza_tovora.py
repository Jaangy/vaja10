a = int(input("Teža tovora ? "))
b = a
c = 0
vs = 0

while a > 0:
    c = c + 1
    print(a)
    a = a // 3 - 2
    if a > 0:
        vs = vs + a

print("Za", b, "tovora bomo porabili", c, "ton goriva.")
print("Za", b, "tovora bomo porabili", vs, "ton goriva.")
