# 1. Nhập tên tệp (bạn chỉ cần gõ romeo.txt)
ten_tep = input("Nhập tên tệp: ")

# 2. Mở tệp tin
try:
    fhand = open(ten_tep)
except:
    print("Lỗi: Không tìm thấy tệp", ten_tep)
    quit() # Thoát chương trình nếu lỗi

# 3. Tạo danh sách rỗng để chứa các từ
danh_sach_tu = list()

# 4. Đọc từng dòng trong tệp
for dong in fhand:
    # Cắt dòng thành các từ nhỏ (tách bằng khoảng trắng)
    cac_tu = dong.split()
    
    # 5. Duyệt qua từng từ vừa cắt được
    for tu in cac_tu:
        # Nếu từ đó CHƯA có trong danh sách thì mới thêm vào
        if tu not in danh_sach_tu:
            danh_sach_tu.append(tu)

# 6. Sắp xếp danh sách theo bảng chữ cái
danh_sach_tu.sort()

# 7. In kết quả ra màn hình
print(danh_sach_tu)