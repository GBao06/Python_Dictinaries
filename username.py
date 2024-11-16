
user_data = {}


def add_user(username, password):
    if username in user_data:
        print("Tên đăng nhập đã tồn tại.")
    else:
        user_data[username] = password
        print("Thêm người dùng thành công!")


def check_login(username, password):
    if username in user_data and user_data[username] == password:
        print("Đăng nhập thành công!")
    else:
        print("Tên đăng nhập hoặc mật khẩu không chính xác.")


def remove_user(username):
    if username in user_data:
        del user_data[username]
        print("Xóa người dùng thành công!")
    else:
        print("Người dùng không tồn tại.")


def menu():
    while True:
        print("\n--- Quản lý người dùng ---")
        print("1. Thêm người dùng")
        print("2. Đăng nhập")
        print("3. Xóa người dùng")
        print("4. Thoát")
        
        choice = input("Chọn một hành động (1-4): ")
        
        if choice == "1":
            username = input("Nhập tên đăng nhập: ")
            password = input("Nhập mật khẩu: ")
            add_user(username, password)
        elif choice == "2":
            username = input("Nhập tên đăng nhập: ")
            password = input("Nhập mật khẩu: ")
            check_login(username, password)
        elif choice == "3":
            username = input("Nhập tên đăng nhập cần xóa: ")
            remove_user(username)
        elif choice == "4":
            print("Thoát chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng thử lại.")
menu()
