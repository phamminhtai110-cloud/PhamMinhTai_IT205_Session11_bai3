product_list = [
    {"product_id": "SP001", "product_name": "Áo polo nam", "price": 299000, "quantity": 20},
    {"product_id": "SP002", "product_name": "Quần kaki nam", "price": 399000, "quantity": 15},
    {"product_id": "SP003", "product_name": "Váy công sở nữ", "price": 459000, "quantity": 10}
]

while True:
    print("\n1.Xem  2.Thêm  3.Cập nhật  4.Xóa  5.Thoát")
    choice = input("Chọn: ")

    if choice == "1":
        for p in product_list:
            print(p)

    elif choice == "2":
        product_id = input("Mã SP: ").strip().upper()

        if any(p["product_id"] == product_id for p in product_list):
            print("Mã sản phẩm bị trùng")
            continue

        try:
            product_name = input("Tên SP: ")
            price = int(input("Giá: "))
            quantity = int(input("Số lượng: "))

            if price <= 0 or quantity <= 0:
                print("Giá/Số lượng không hợp lệ")
                continue

            product_list.append({
                "product_id": product_id,
                "product_name": product_name,
                "price": price,
                "quantity": quantity
            })

            print("Thêm thành công")

        except:
            print("Giá/Số lượng không hợp lệ")

    elif choice == "3":
        product_id = input("Mã SP: ").strip().upper()

        for p in product_list:
            if p["product_id"] == product_id:
                p["product_name"] = input("Tên mới: ")
                p["price"] = int(input("Giá mới: "))
                p["quantity"] = int(input("Số lượng mới: "))
                print("Cập nhật thành công")
                break
        else:
            print("Không tìm thấy mã sản phẩm cần cập nhật!")

    elif choice == "4":
        product_id = input("Mã SP: ").strip().upper()

        for p in product_list:
            if p["product_id"] == product_id:
                product_list.remove(p)
                print("Xóa thành công")
                break
        else:
            print("Không tìm thấy mã sản phẩm cần xoá!")

    elif choice == "5":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ")