# Bước 1: Tạo một danh sách rỗng để chứa các số
danh_sach_so = list()

# Bước 2: Bắt đầu vòng lặp vô hạn để nhập dữ liệu
while True:
    # Yêu cầu người dùng nhập (giữ nguyên tiếng Anh cho giống đề bài)
    du_lieu_nhap = input("Enter a number: ")

    # Bước 3: Kiểm tra điều kiện thoát
    if du_lieu_nhap == 'done':
        break
    
    # Bước 4: Cố gắng chuyển đổi sang số thực (float)
    try:
        so_da_chuyen_doi = float(du_lieu_nhap)
        
        # Nếu chuyển đổi thành công, THÊM số đó vào danh sách
        danh_sach_so.append(so_da_chuyen_doi)
        
    except:
        # Nếu nhập sai (không phải số), báo lỗi
        print("Invalid input")

# Bước 5: Sau khi vòng lặp kết thúc (người dùng gõ done)
# Kiểm tra xem danh sách có trống không để tránh lỗi
if len(danh_sach_so) > 0:
    # Dùng hàm max() và min() có sẵn của Python để tìm kết quả
    print("Maximum:", max(danh_sach_so))
    print("Minimum:", min(danh_sach_so))
else:
    print("Bạn chưa nhập số nào cả!")