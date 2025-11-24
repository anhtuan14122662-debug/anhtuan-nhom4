# Bài tập 2: Tính độ tin cậy Spam trung bình

# Khởi tạo các biến tích lũy
tong_do_tin_cay = 0.0
dem_dong = 0

# 1. Yêu cầu người dùng nhập tên tệp
ten_tep = input('Nhập tên tệp: ')

try:
    # Mở tệp
    tay_cam_tep = open(ten_tep)

    # 2. Lặp qua từng dòng của tệp
    for dong in tay_cam_tep:
        # Loại bỏ khoảng trắng và ký tự xuống dòng ở cuối
        dong = dong.rstrip()

        # Kiểm tra xem dòng có phải là dòng "X-DSPAM-Confidence:" không
        if dong.startswith('X-DSPAM-Confidence:'):
            # 3. Trích xuất số thực
            
            # Tìm vị trí của ký tự hai chấm (:)
            vi_tri_hai_cham = dong.find(':')

            # Cắt chuỗi, bắt đầu sau dấu hai chấm và loại bỏ khoảng trắng dư thừa
            chuoi_so = dong[vi_tri_hai_cham + 1:].strip()

            # Chuyển chuỗi số thành số thực (float)
            try:
                gia_tri = float(chuoi_so)
            except ValueError:
                # Bỏ qua nếu giá trị trích xuất không hợp lệ (nên rất hiếm)
                continue

            # 4. Cập nhật tổng và bộ đếm
            tong_do_tin_cay = tong_do_tin_cay + gia_tri
            dem_dong = dem_dong + 1

    # Đóng tệp
    tay_cam_tep.close()

    # 5. Tính và in kết quả
    if dem_dong > 0:
        do_tin_cay_trung_binh = tong_do_tin_cay / dem_dong
        print(f"Độ tin cậy spam trung bình: {do_tin_cay_trung_binh}")
    else:
        print("Không tìm thấy dòng 'X-DSPAM-Confidence:' trong tệp.")

except FileNotFoundError:
    print(f"Lỗi: Không tìm thấy tệp '{ten_tep}'.")
except Exception as e:
    print(f"Đã xảy ra lỗi không xác định: {e}")
