m,n = map(int, input("Nhap so luong hang va cot: ").split())
a = []
print("Nhap ma tran A: ")
for i in range(m):
    row = list(map(int,input().split()))
    a.append(row)
tong = 0
for i in range(m):
    for j in range(n):
        if i == j:
            tong += a[i][j]

print("Tong cac phan tu tren duong cheo chinh: ", tong)
