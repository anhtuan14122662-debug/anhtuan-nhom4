diem_str = input("Nhập điểm (từ 0.0 đến 1.0): ")
try:
    diem = float(diem_str)
    if diem < 0.0 or diem > 1.0:
        print("Không hợp lệ,điểm phải nằm trong khoảng từ 0.0 đến 1.0")
    else:
        if diem >= 0.9:
            grade = "A"
        elif diem >= 0.8:
            grade = "B"
        elif diem >= 0.7:
            grade = "C"
        elif diem >= 0.6:
            grade = "D"
        else: 
            grade = "F"
        print(f"Loại điểm: {grade}")
except ValueError:
    print("Điểm không đúng yêu cầu (điểm hiển thị phải  là số)")