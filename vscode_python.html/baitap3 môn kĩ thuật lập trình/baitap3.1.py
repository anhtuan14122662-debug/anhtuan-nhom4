try:
    so_gio_str = input("Nhập số giờ: ")
    so_gio = float(so_gio_str)
    luong_moi_gio_str = input("Nhập lương mỗi giờ: ")
    luong_moi_gio = float(luong_moi_gio_str)
except ValueError:
    print("Lỗi, vui lòng nhập dữ liệu dạng số")
    quit()
nguong_lam_them = 40
he_so_lam_them = 1.5
if so_gio > nguong_lam_them:
    luong_chinh_thuc = nguong_lam_them * luong_moi_gio
    gio_lam_them = so_gio - nguong_lam_them
    luong_lam_them = gio_lam_them * luong_moi_gio * he_so_lam_them
    tong_luong = luong_chinh_thuc + luong_lam_them
else:
    tong_luong = so_gio * luong_moi_gio
print("Lương:", tong_luong)