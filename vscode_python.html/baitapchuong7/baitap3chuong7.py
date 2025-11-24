# Bài tập 3: Chương trình Easter Egg (Trứng Phục Sinh)

# Khởi tạo các biến tích lũy (ví dụ: đếm dòng Subject)
dem_dong_subject = 0
dong_can_dem = 'Subject:' # Giả sử chúng ta đang đếm dòng Subject theo ví dụ

# 1. Yêu cầu người dùng nhập tên tệp
ten_tep = input('Nhập tên tệp: ')

# 2. Kiểm tra điều kiện Easter Egg
if ten_tep.lower() == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - Bạn đã bị trêu chọc!")
    # Kết thúc chương trình một cách lịch sự
    exit()

# 3. Xử lý tệp tin (phần code bình thường)
try:
    # Mở tệp
    tay_cam_tep = open(ten_tep)

    # Lặp qua từng dòng của tệp
    for dong in tay_cam_tep:
        # Giả lập việc tìm kiếm và đếm dòng 'Subject:'
        if dong.startswith(dong_can_dem):
            dem_dong_subject = dem_dong_subject + 1

    # Đóng tệp
    tay_cam_tep.close()

    # In kết quả bình thường
    print(f"Có {dem_dong_subject} dòng {dong_can_dem.strip(':')} trong tệp {ten_tep}")

except FileNotFoundError:
    # Xử lý lỗi nếu tệp không tồn tại
    print(f"Không thể mở tệp: {ten_tep}")
except Exception as e:
    print(f"Đã xảy ra lỗi không xác định: {e}")
