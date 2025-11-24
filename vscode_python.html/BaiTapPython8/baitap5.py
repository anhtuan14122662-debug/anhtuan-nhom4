# 1. Nhập tên tệp (bạn sẽ nhập mbox-short.txt)
ten_tep = input("Nhập tên tệp: ")

# 2. Mở tệp tin an toàn
try:
    fhand = open(ten_tep)
except:
    print("Không tìm thấy tệp:", ten_tep)
    quit()

# 3. Khởi tạo biến đếm (bắt đầu từ 0)
count = 0

# 4. Đọc từng dòng trong tệp
for dong in fhand:
    # Xóa khoảng trắng xuống dòng ở cuối mỗi dòng
    dong = dong.rstrip()

    # 5. QUAN TRỌNG: Chỉ chọn dòng bắt đầu bằng "From " 
    # (Lưu ý: phải có dấu cách sau chữ From để tránh nhầm với From:)
    if dong.startswith('From '):
        
        # 6. Tách dòng thành các từ (danh sách)
        cac_tu = dong.split()
        
        # 7. Lấy email (là từ thứ 2, tức là vị trí index [1])
        email = cac_tu[1]
        
        # In email ra màn hình
        print(email)
        
        # 8. Tăng biến đếm thêm 1
        count = count + 1

# 9. In dòng kết luận cuối cùng (theo mẫu đề bài)
print("There were", count, "lines in the file with From as the first word")