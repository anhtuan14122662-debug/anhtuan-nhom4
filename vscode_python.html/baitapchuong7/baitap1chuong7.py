# Bài tập 1: Đọc tệp và in nội dung bằng chữ hoa (Python Shout)

# 1. Yêu cầu người dùng nhập tên tệp
ten_tep = input('Nhập tên tệp: ')

try:
    # 2. Mở tệp để đọc
    tay_cam_tep = open(ten_tep)

    # 3. Lặp qua từng dòng và in bằng chữ hoa
    for dong in tay_cam_tep:
        # Loại bỏ ký tự xuống dòng dư thừa ở cuối
        dong = dong.rstrip()
        # Chuyển dòng thành chữ hoa và in
        print(dong.upper())

    # 4. Đóng tệp
    tay_cam_tep.close()

except FileNotFoundError:
    # Xử lý lỗi nếu tệp không tồn tại
    print(f"Lỗi: Không tìm thấy tệp '{ten_tep}'. Vui lòng kiểm tra lại tên tệp.")
except Exception as e:
    # Xử lý các lỗi khác (ví dụ: lỗi quyền truy cập)
    print(f"Đã xảy ra lỗi: {e}")
