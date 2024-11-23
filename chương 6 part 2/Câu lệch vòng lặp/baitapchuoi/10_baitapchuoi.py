# Nhập 
nhap_kt_str = input("Nhập vào chuỗi ký tự: ")

#  tạo chuỗi chứa số và chuỗi chứa các ký tự không phải số
so = ""
non_so = ""

# kiểm tra
for char in nhap_kt_str:
    if char.isdigit():  
        so += char
    else: 
        non_so += char

# Kết hợp chuỗi số và chuỗi không phải số
ket_qua = so + non_so

# In kết quả
print("Kết quả:", ket_qua)