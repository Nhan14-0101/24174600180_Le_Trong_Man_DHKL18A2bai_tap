# Nhập 
input_str = input("Nhập vào chuỗi ký tự: ")
#tạo biến đếm
count_viet_hoa = 0  
count_viet_thuong = 0  
# kiểm tra  ký tự 
for char in input_str:
    if char.isupper():  
        count_viet_hoa += 1
    elif char.islower(): 
        count_viet_thuong += 1
# kết quả
print(f"Số chữ cái viết hoa: {count_viet_hoa}")
print(f"Số chữ cái viết thường: {count_viet_thuong}")