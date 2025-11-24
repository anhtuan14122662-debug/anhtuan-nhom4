
# Bài tập 6: Sử dụng các phương thức chuỗi strip() và replace()

# Bài tập này yêu cầu đọc tài liệu và thực hành.
# Dưới đây là các ví dụ minh họa cách sử dụng hai phương thức hữu ích: strip() và replace().

# --- Ví dụ về strip() ---
print("Ví dụ về phương thức strip():")
chuoi_co_khoang_trang = "   Đây là chuỗi có khoảng trắng ở đầu và cuối. \n "
print(f"Chuỗi gốc (có khoảng trắng ẩn): '{chuoi_co_khoang_trang}'")

# Loại bỏ tất cả khoảng trắng (spaces, tabs, newlines) ở đầu và cuối chuỗi.
chuoi_da_xu_ly_strip = chuoi_co_khoang_trang.strip()
print(f"Chuỗi sau khi dùng strip(): '{chuoi_da_xu_ly_strip}'")

# strip() cũng có thể loại bỏ các ký tự cụ thể:
chuoi_can_lam_sach = "abc---Giá trị---cba"
# Chỉ loại bỏ các ký tự 'a', 'b', 'c', '-' ở hai đầu:
chuoi_da_lam_sach = chuoi_can_lam_sach.strip('abc-')
print(f"Chuỗi gốc: '{chuoi_can_lam_sach}'")
print(f"Chuỗi sau khi dùng strip('abc-'): '{chuoi_da_lam_sach}'")


# --- Ví dụ về replace() ---
print("\nVí dụ về phương thức replace():")
chuoi_thong_bao = "Giá tiền là $10.00 đô la."

# Thay thế tất cả các lần xuất hiện của chuỗi con
chuoi_da_thay_the = chuoi_thong_bao.replace('$', 'VND')
print(f"Chuỗi gốc: '{chuoi_thong_bao}'")
print(f"Chuỗi sau khi dùng replace('$', 'VND'): '{chuoi_da_thay_the}'")

# Thay thế các ký tự không mong muốn (ví dụ: dấu phẩy) trước khi chuyển sang số:
chuoi_so_co_loi = "1,234,567.89"
chuoi_da_loai_phay = chuoi_so_co_loi.replace(',', '')
gia_tri_float_replace = float(chuoi_da_loai_phay)
print(f"Chuỗi số có lỗi: '{chuoi_so_co_loi}'")
print(f"Chuỗi đã loại phẩy: '{chuoi_da_loai_phay}' (Giá trị Float: {gia_tri_float_replace})")

# Phương thức replace() cũng có thể nhận đối số thứ ba để giới hạn số lần thay thế
chuoi_lap_lai = "banana, banana, táo"
chuoi_thay_the_gioi_han = chuoi_lap_lai.replace('banana', 'chuối', 1) # Chỉ thay thế lần đầu
print(f"Chuỗi lặp lại: '{chuoi_lap_lai}'")
print(f"Chuỗi sau khi thay thế giới hạn (1 lần): '{chuoi_thay_the_gioi_han}'")
