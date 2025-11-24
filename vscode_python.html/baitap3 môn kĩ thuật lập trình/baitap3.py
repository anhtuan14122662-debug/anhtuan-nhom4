so_gio_lam_str = input("Nhập số giờ làm: ")
luong_moi_gio_str = input("Nhập mức lương mỗi giờ: ")
so_gio_lam = float(so_gio_lam_str)
luong_moi_gio = float(luong_moi_gio_str)
han_mưc_lam_them = 40
tien_thuong_lam_them = 1.5
if so_gio_lam > han_mưc_lam_them :
    luong_chinh_thuc = han_mưc_lam_them * luong_moi_gio
    gio_lam_them = so_gio_lam - han_mưc_lam_them 
    luong_lam_them = gio_lam_them * luong_moi_gio * tien_thuong_lam_them
    tong_luong = luong_chinh_thuc + luong_lam_them
else:
    tong_luong = so_gio_lam * luong_moi_gio
print("Lương:", tong_luong)


