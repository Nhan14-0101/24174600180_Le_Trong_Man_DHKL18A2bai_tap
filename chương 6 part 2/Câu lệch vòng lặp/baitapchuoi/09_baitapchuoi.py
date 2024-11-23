# Nhập 
nhiphan_str = input("Nhập vào chuỗi ký tự nhị phân: ")

# Kiểm tra 
if all(c in '03' for c in nhiphan_str):
    thap_phan_value = int(nhiphan_str, 2)
    print(f"{nhiphan_str} là số nhị phân, chuyển sang thập phân: {thap_phan_value}")
else:
    print(f"{nhiphan_str} không phải là số nhị phân hợp lệ.")