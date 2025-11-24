# Bài tập 5: Trích xuất chuỗi và chuyển đổi sang số thực (float)

# Chuỗi đầu vào đã cho:
chuoi_goc = 'X-DSPAM-Confidence: 0.8475'

# 1. Tìm vị trí của ký tự hai chấm (:)
# Chúng ta tìm vị trí của ký tự ':'.
vi_tri_hai_cham = chuoi_goc.find(':')

# 2. Trích xuất phần chuỗi sau ký tự hai chấm
# Phần chúng ta cần là từ vị trí sau dấu hai chấm đến hết chuỗi.
# Chúng ta cộng thêm 1 để bắt đầu ngay sau ký tự ':'.
# Sau đó, sử dụng phương thức strip() để loại bỏ khoảng trắng dư thừa
# ở đầu chuỗi (như khoảng trắng sau dấu hai chấm).
chuoi_so = chuoi_goc[vi_tri_hai_cham + 1:].strip()

# 3. Chuyển đổi chuỗi đã trích xuất thành số thực (float)
gia_tri_float = float(chuoi_so)

# In kết quả ra màn hình
print("Chuỗi gốc:", chuoi_goc)
print("Phần chuỗi đã trích xuất (số):", chuoi_so)
print("Giá trị số thực (float):", gia_tri_float)
print("Kiểu dữ liệu của giá trị trích xuất:", type(gia_tri_float))

print("\n" + "="*50 + "\n")


