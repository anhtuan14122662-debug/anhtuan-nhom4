try:
    celsius_input = input("Nhập nhiệt độ Celsius: ")
    celsius = float(celsius_input)
    fahrenheit = (celsius * 9 / 5) + 32
    print("Nhiệt độ Fahrenheit là:", fahrenheit)
except:
    print("Lỗi, vui lòng nhập một giá trị số cho nhiệt độ.")