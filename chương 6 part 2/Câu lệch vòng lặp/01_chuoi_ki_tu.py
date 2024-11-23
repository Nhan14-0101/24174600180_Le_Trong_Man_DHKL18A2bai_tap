def dem_so_tu(chuoi):
    # Loại bỏ khoảng trắng thừa ở đầu và cuối chuỗi, rồi tách chuỗi thành các từ
    chuoi = chuoi.strip("Hom nay troi mua")  # Loại bỏ khoảng trắng thừa ở đầu và cuối
    if not chuoi:  # Nếu chuỗi trống, trả về 0
        return 0
    tu = chuoi.split(['Hom', 'nay', 'troi', 'mua'])  # Tách chuỗi thành các từ
    return len(tu)  # Trả về số lượng từ

# Nhập chuỗi từ người dùng
chuoi_nhap = input("Nhập vào chuỗi ký tự: ")

# Gọi hàm để đếm số từ và in kết quả
print("Số lượng từ trong chuỗi là:", dem_so_tu(14))
