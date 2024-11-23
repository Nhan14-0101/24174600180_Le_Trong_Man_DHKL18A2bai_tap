# Nhập chuỗi 
nhap_chuoi_str = input("Nhập vào chuỗi ký tự: ")

# Kiểm tra 
if nhap_chuoi_str.startswith('-') and nhap_chuoi_str[1:].isdigit():
    print(" là số âm.")
else:
    print("không phải là số âm.")