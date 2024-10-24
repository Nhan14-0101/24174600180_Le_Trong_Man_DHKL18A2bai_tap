#Bài 1:
import math



   # Nhập bán kính và chiều cao từ bàn phím
r = float(input("Nhập bán kính (r): "))
h = float(input("Nhập chiều cao(h): "))
if h > 0 and r > 0:
    pi = 3.14
       #Tính diện tích xung quanh, diện tích toàn phần và thể tích hình trụ 
    S_xung_quanh = 2 * math.pi * r * h
    S_toàn_phần = 2 * math.pi * r * h +2 * pi * r**2
    the_tich = pi * r**2 * h
       # Kết quả
    print(f"Dien tich xung quanh: {round(S_xung_quanh,2)}")
    print(f"Dien tich toan phan: {round(S_toàn_phần, 2)}")
    print(f"Thể tích: {round(the_tich, 2)}")
else:
    print("r va h phai lon hon 0")
    


