def decimal_to_binary(decimal_number):
    # Hàm chuyển từ hệ thập phân sang hệ nhị phân
    if decimal_number == 0:
        return "0"
    binary_number = ""
    while decimal_number > 0:
        binary_number = str(decimal_number % 2) + binary_number
        decimal_number = decimal_number // 2
    return binary_number

def binary_to_decimal(binary_number):
    # Hàm chuyển từ hệ nhị phân sang hệ thập phân
    decimal_number = 0
    power = 0
    for digit in reversed(binary_number):
        if digit == '1':
            decimal_number += 2 ** power
        power += 1
    return decimal_number

# Giao diện người dùng
def main():
    print("Chọn lựa chuyển đổi:")
    print("1. Hệ thập phân sang hệ nhị phân")
    print("2. Hệ nhị phân sang hệ thập phân")
    choice = input("Nhập lựa chọn (1/2): ")

    if choice == "1":
        decimal_number = int(input("Nhập số hệ thập phân: "))
        print(f"{decimal_number} trong hệ nhị phân là: {decimal_to_binary(decimal_number)}")
    
    elif choice == "2":
        binary_number = input("Nhập số hệ nhị phân: ")
        # Kiểm tra số nhập vào có phải là số nhị phân không
        if all(digit in "01" for digit in binary_number):
            print(f"{binary_number} trong hệ thập phân là: {binary_to_decimal(binary_number)}")
        else:
            print("Số nhập vào không phải là số nhị phân hợp lệ!")
    
    else:
        print("Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
