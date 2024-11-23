m,n = map(int,input("Nhap so luong hang va cot cua ma tran A: ").split())
d,f = map(int,input("Nhap so luong hang va cot cua ma tran B: ").split())

if n != d:
    print("Không thể nhân ma trận vì số cột của A không bằng số hàng của B.")
    exit()

a = []
b = []
print("Nhap ma tran A: ")
for i in range(m):
    row = list(map(int,input().split()))
    a.append(row)

print("Nhap ma tran B: ")
for i in range(d):
    row = list(map(int,input().split()))
    b.append(row)

c = [[0]*f  for _ in range(m)]

for i in range(m):
    for j in range(f):
        for k in range(n):
            c[i][j] += a[i][k] * b[k][j]

print("Kết quả của phép nhân ma trận A và B là:")
for row in c:
    print(row)