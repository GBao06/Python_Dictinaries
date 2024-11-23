# a = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# # for i in a:
# #     for e in i:
# #         print("{:<5}".format(e), end=' ')
# #     print()
# for i in range(len(a)):
#     for j in range(len(a[i])):
#         print("{:>7}".format(a[i][j]), end=' ')
#     print()

#khoi tao ma tran gom m hang n cot
# m = 4
# n = 3
# a=[[0]*n]*m
# print(a)

# for i in a:
#     for j in i:
#          print("{:>4}".format(j), end=" ")
#     print()

#nhap ma tran
# a = []
# m = int(input())
# n = int(input())

# for i in range(m):
#     row = []
#     for j in range(n):
#         row = map(int,input().split())
#     a.append(row)
# # print(a)
# for i in a:
#     for j in i:
#         print("{:>7}".format(j), end=' ')
#     print()
a = []
b = []
m,n = map(int,input("Nhap so hang va cot: ").split())
print("Nhap ma tran A: \n")
for i in range(m):
    row = list(map(int, input().split()))
    a.append(row)
print("Nhap ma tran B: \n")
for i in range(m):
    row = list(map(int, input().split()))
    b.append(row)

c = []

for i in range(m):
    hang = []
    for j in range(n):
        hang.append(a[i][j]+b[i][j])
    c.append(hang)
for i in c:
    for d in i:
        print("{:>3}".format(d), end=' ')
    print()