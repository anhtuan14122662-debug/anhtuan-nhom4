

try:
  
    so_gio = float(input("Nhập giờ: "))
    muc_luong = float(input("Tỷ lệ nhập: "))
    tong_luong = so_gio * muc_luong
    print("Trả tiền:", tong_luong)
except:
    print("Lỗi, vui lòng nhập giá trị số.")