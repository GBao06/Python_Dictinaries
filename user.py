user = {}
print("-----Them tai khoang-----")
while True:
    username = input("Nhap ten nguoi dung: ")
    if username == "":
        break
    password = input("Nhap mat khau: ")
    if username in user:
        print("Ten nguoi dung da ton tai!")
    else:
        user[username] = password
   
    

print("------Dang nhap---------")
while True:
    tendangnhap = input("Ten dang nhap: ")
    matkhau = input("Mat khau: ")
    if tendangnhap in user and user[tendangnhap] == matkhau:
        print("Dang nhap thanh cong!")
        break
    else:
        print("Ten dang nhap hoac mat khau khong chinh xac")    
