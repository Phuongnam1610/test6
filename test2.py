def trich_xuat_id_va_ten_file(du_lieu_json):
    ket_qua = []
    try:
        danh_sach_tai_lieu = du_lieu_json['result']['listDocument']
        for tai_lieu in danh_sach_tai_lieu:
            id = tai_lieu['id']
            ten_file = tai_lieu['originalFileName']
            ket_qua.append((id, ten_file))
    except KeyError:
        print("Lỗi: Không tìm thấy dữ liệu cần thiết trong JSON")
    return ket_qua

# Ví dụ sử dụng:
du_lieu_json = {
    "ok": True,
    "message": None,
    "result": {
        "total": 103,
        "listDocument": [
            {
                "id": "8bb45504-9d3d-ef11-94e9-b8ca3aeb783a",
                "originalFileName": "KS.2017.01.2017-07-05.62.pdf",
                # ... (các trường khác)
            },
             {
                "id": "33333333333333-9d3d-ef11-94e9-b8ca3aeb783a",
                "originalFileName": "KS.2017.01.2017-07-05.62.pdf",
                # ... (các trường khác)
            },
            # ... (các tài liệu khác)
        ]
    }
}

ket_qua = trich_xuat_id_va_ten_file(du_lieu_json)
for cap in ket_qua:
    print(f"ID: {cap[0]}, Tên file: {cap[1]}")