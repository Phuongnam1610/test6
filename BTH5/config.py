import os

# Đọc file setting.txt
def load_settings():
    settings = {}
    if os.path.exists('setting.txt'):
        with open('setting.txt', 'r', encoding='utf-8') as f:
            for line in f:
                key, value = line.strip().split('=')
                settings[key.strip()] = value.strip()
    return settings

# Tạo biến toàn cục
globals().update(load_settings())

# Hàm để lấy giá trị của một biến
def get_setting(key, default=None):
    return globals().get(key, default)

def update_setting(key, value):
    # Cập nhật biến toàn cục
    globals()[key] = value
    
    # Đọc tất cả các dòng từ file
    lines = []
    if os.path.exists('setting.txt'):
        with open('setting.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
    
    # Tìm và cập nhật dòng chứa key
    key_updated = False
    for i, line in enumerate(lines):
        if line.strip().split('=')[0].strip() == key:
            lines[i] = f"{key} = {value}\n"
            key_updated = True
            break
    
    # Nếu key không tồn tại, thêm vào cuối file
    if not key_updated:
        lines.append(f"{key} = {value}\n")
    
    # Ghi lại vào file
    with open('setting.txt', 'w', encoding='utf-8') as f:
        f.writelines(lines)

    print(f"Đã cập nhật cài đặt: {key} = {value}")

