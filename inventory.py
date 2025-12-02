products = []

def add_product():
    print("Tính năng nhập hàng chưa được triển khai.")

def view_inventory():
    print("Tính năng xem tồn kho chưa được triển khai.")

def check_low_stock():
    print("Tính năng cảnh báo hết hàng chưa được triển khai.")

def main():
    while True:
        print("\n--- QUẢN LÝ KHO HÀNG ---")
        print("1. Nhập hàng mới")
        print("2. Xem tồn kho")
        print("3. Cảnh báo hết hàng")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_product()
        elif choice == '2':
            view_inventory()
        elif choice == '3':
            check_low_stock()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()

def add_product():
    name = input("Nhập tên sản phẩm: ")
    price = int(input("Nhập giá bán: "))
    qty = int(input("Nhập số lượng tồn kho: "))

    product = {
        'name': name,
        'price': price,
        'qty': qty
    }

    products.append(product)
    print("Đã nhập hàng thành công.")
    