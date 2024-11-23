#Tìm số nguyên số lớn nhất nhỏ hơn hoặc bằng 20
n = 20
while True:
    for i in range(n):
        if n%1==0 and i!=1 and i!=n:
            n = n -1
            break
    else:
        break 

    if n < 1:
        break
print(f"So nguyen to la {n}")