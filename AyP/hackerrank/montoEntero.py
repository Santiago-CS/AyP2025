monto = int(input())

c500 = monto // 500
monto = monto % 500 

c200 = monto // 200
monto = monto % 200 

c100 = monto // 100
monto = monto % 100

c50 = monto // 50
monto = monto % 50

c20 = monto // 20
monto = monto % 20

c10 = monto // 10
monto = monto % 10

c5 = monto // 5
monto = monto % 5

c2 = monto // 2
monto = monto % 2

c1 = monto // 1

print(c500, c200, c100, c50, c20, c10, c5, c2, c1)