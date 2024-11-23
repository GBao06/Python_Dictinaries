m,n = map(int,input("Nhap so luong hang va cot: ").split())

a = []

for i in range(m):
    row = list(map(int,input().split()))
    a.append(row)
check = False
for i in range(m):
    for j in range(n):
        if a[i][j] == a[j][i]:
            check = True
        else:
            check = False
            break

if check:
    print("Yes")
else:
    print("No")