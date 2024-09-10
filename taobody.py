import json
import re
from config import get_setting
def txtenfile(tenfile):
    # Sử dụng biểu thức chính quy để trích xuất thông tin
    pattern = r'KS\.(\d{4})\.(\d{2}\.\d{4})-(\d{2})-(\d{2})\.(\d+)\.pdf'
    match = re.match(pattern, tenfile)
    
    if match:
        nam, quyen_so, thang, ngay, so = match.groups()
        tt=f"so:{so}\nquyenSo:{quyen_so.replace('.', '/')}\nngayDangKy:{ngay}.{thang}.{nam}"
        return tt
    else:
        return None

def tao_body_gui_di(rpGemini,tenfile,id):
    rpGemini=kiem_tra_va_them_loai_giay_to(rpGemini)
    # print(rpGemini)
    # print(txtenfile(tenfile))
    rpGemini=txtenfile(tenfile)+"\n"+rpGemini
    # print(rpGemini)
    # Phân tích chuỗi thông tin thành từng dòng
    cac_dong = rpGemini.strip().split('\n')
    # Tạo dictionary để lưu thông tin
    data = {}
    for dong in cac_dong:
        dong = dong.strip()
        if ':' in dong:
            key, value = dong.split(':', 1)
            data[key.strip()] = value.strip()
        else:
            # Xử lý trường hợp dòng không có dấu hai chấm
            continue
    
    # Đọc dữ liệu mappingData cũ
    old_mapping_data = json.loads("[{\"so\":\"02\",\"quyenSo\":\"01/2017\",\"trangSo\":\"4443\",\"ngayDangKy\":\"09.01.2017\",\"loaiDangKy\":0,\"noiDangKy\":\"\",\"nguoiKy\":\"\",\"chucVuNguoiKy\":\"\",\"nguoiThucHien\":\"\",\"ghiChu\":\"\",\"nksHoTen\":\"NGUYỄN NGỌC HOAN\",\"nksGioiTinh\":0,\"nksNgaySinh\":\"\",\"nksNgaySinhBangChu\":\"\",\"nksNoiSinh\":\"\",\"nksNoiSinhDVHC\":\"\",\"nksQueQuan\":\"\",\"nksDanToc\":\"\",\"nksQuocTich\":\"Việt Nam\",\"nksQuocTichKhac\":\"\",\"nksLoaiKhaiSinh\":0,\"nksMatTich\":0,\"nksMatTichNgayGhiChuTuyenBo\":\"\",\"nksMatTichCanCuTuyenBo\":\"\",\"nksMatTichNgayGhiChuHuyTuyenBo\":\"\",\"nksMatTichCanCuHuyTuyenBo\":\"\",\"nksHanCheNangLucHanhVi\":0,\"nksHanCheNangLucHanhViNgayGhiChuTuyenBo\":\"\",\"nksHanCheNangLucHanhViCanCuTuyenBo\":\"\",\"nksHanCheNangLucHanhViNgayGhiChuHuyTuyenBo\":\"\",\"nksHanCheNangLucHanhViNgayCanCuHuyTuyenBo\":\"\",\"meHoTen\":\"\",\"meNgaySinh\":\"\",\"meDanToc\":\"\",\"meQuocTich\":\"Việt Nam\",\"meQuocTichKhac\":\"\",\"meLoaiCuTru\":0,\"meNoiCuTru\":\"\",\"meLoaiGiayToTuyThan\":0,\"meSoGiayToTuyThan\":\"\",\"chaHoTen\":\"\",\"chaNgaySinh\":\"\",\"chaDanToc\":\"\",\"chaQuocTich\":\"Việt Nam\",\"chaQuocTichKhac\":\"\",\"chaLoaiCuTru\":0,\"chaNoiCuTru\":\"\",\"chaLoaiGiayToTuyThan\":0,\"chaSoGiayToTuyThan\":\"\",\"nycHoTen\":\"\",\"nycQuanHe\":\"\",\"nycLoaiGiayToTuyThan\":0,\"nycGiayToKhac\":\"\",\"nycSoGiayToTuyThan\":\"\",\"nycNgayCapGiayToTuyThan\":\"\",\"nycNoiCapGiayToTuyThan\":\"\",\"soDangKyNuocNgoai\":\"\",\"ngayDangKyNuocNgoai\":\"\",\"cqNuocNgoaiDaDangKy\":\"\",\"qgNuocNgoaiDaDangKy\":\"\"}]")

    # Cập nhật dữ liệu mới
    for key, value in data.items():
        if key in old_mapping_data[0]:
            old_mapping_data[0][key] = value

    # Tạo body để gửi đi
    body = {
        "projectId": f"{get_setting('PROJECTID')}",
        "documentId": f"{id}",
        "oldMappingData": "[{\"so\":\"02\",\"quyenSo\":\"01/2017\",\"trangSo\":\"4443\",\"ngayDangKy\":\"09.01.2017\",\"loaiDangKy\":0,\"noiDangKy\":\"\",\"nguoiKy\":\"\",\"chucVuNguoiKy\":\"\",\"nguoiThucHien\":\"\",\"ghiChu\":\"\",\"nksHoTen\":\"NGUYỄN NGỌC HOAN\",\"nksGioiTinh\":0,\"nksNgaySinh\":\"\",\"nksNgaySinhBangChu\":\"\",\"nksNoiSinh\":\"\",\"nksNoiSinhDVHC\":\"\",\"nksQueQuan\":\"\",\"nksDanToc\":\"\",\"nksQuocTich\":\"Việt Nam\",\"nksQuocTichKhac\":\"\",\"nksLoaiKhaiSinh\":0,\"nksMatTich\":0,\"nksMatTichNgayGhiChuTuyenBo\":\"\",\"nksMatTichCanCuTuyenBo\":\"\",\"nksMatTichNgayGhiChuHuyTuyenBo\":\"\",\"nksMatTichCanCuHuyTuyenBo\":\"\",\"nksHanCheNangLucHanhVi\":0,\"nksHanCheNangLucHanhViNgayGhiChuTuyenBo\":\"\",\"nksHanCheNangLucHanhViCanCuTuyenBo\":\"\",\"nksHanCheNangLucHanhViNgayGhiChuHuyTuyenBo\":\"\",\"nksHanCheNangLucHanhViNgayCanCuHuyTuyenBo\":\"\",\"meHoTen\":\"\",\"meNgaySinh\":\"\",\"meDanToc\":\"\",\"meQuocTich\":\"Việt Nam\",\"meQuocTichKhac\":\"\",\"meLoaiCuTru\":0,\"meNoiCuTru\":\"\",\"meLoaiGiayToTuyThan\":0,\"meSoGiayToTuyThan\":\"\",\"chaHoTen\":\"\",\"chaNgaySinh\":\"\",\"chaDanToc\":\"\",\"chaQuocTich\":\"Việt Nam\",\"chaQuocTichKhac\":\"\",\"chaLoaiCuTru\":0,\"chaNoiCuTru\":\"\",\"chaLoaiGiayToTuyThan\":0,\"chaSoGiayToTuyThan\":\"\",\"nycHoTen\":\"\",\"nycQuanHe\":\"\",\"nycLoaiGiayToTuyThan\":0,\"nycGiayToKhac\":\"\",\"nycSoGiayToTuyThan\":\"\",\"nycNgayCapGiayToTuyThan\":\"\",\"nycNoiCapGiayToTuyThan\":\"\",\"soDangKyNuocNgoai\":\"\",\"ngayDangKyNuocNgoai\":\"\",\"cqNuocNgoaiDaDangKy\":\"\",\"qgNuocNgoaiDaDangKy\":\"\"}]",
        "mappingData": json.dumps(old_mapping_data, ensure_ascii=False),
        "action": 4
    }
    
    return body
# from convertpngtotext import *

# thongtin=chuyen_thanh_text("KS.2017.01.2017-02-03.05.png")
# thongtin="""
# trangSo: 05
# nguoiKy: Hoàng Xuân Thủy
# chucVuNguoiKy: Chủ tịch UBND Xã
# nguoiThucHien: Đỗ Thị Mai Trang
# nksHoTen: PHẠM VĂN QUỐC
# nksNgaySinh: 10.6.2010
# nksNoiSinh: Bệnh viện tỉnh Ninh Thuận, Phường Mỹ Hiệp, TP. Phan Rang- Tháp Chàm, Ninh Thuận
# nksQueQuan: Thanh Hải, Ninh Hải, Ninh Thuận
# nksDanToc: Kinh
# meHoTen: Trần Thị Kim Cúc
# meNgaySinh: 30.11.1987
# meDanToc: Kinh
# meNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận
# meSoGiayToTuyThan:
# chaHoTen: Phạm  Nhũng
# chaNgaySinh: 1984
# chaDanToc: Kinh
# chaNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận
# chaSoGiayToTuyThan:
# nycHoTen: Trần Thị Kim Cúc
# nycSoGiayToTuyThan: 269257817
# nycNgayCapGiayToTuyThan: 05/6/2012
# nycNoiCapGiayToTuyThan: CA Ninh Thuận
# """
# body = tao_body_gui_di(thongtin.strip(),"KS.2017.01.2017-02-03.05.pdf","123")
# print('\n\n\n')
# print(body)
# print('\n\n\n')
def kiem_tra_va_them_loai_giay_to(thongtin):
    dong_moi = []
    for dong in thongtin.strip().split('\n'):
        dong_moi.append(dong)
        if 'SoGiayToTuyThan:' in dong and not dong.split(':')[1].strip():
            prefix = dong.split('SoGiayToTuyThan')[0]
            dong_moi.append(f"{prefix}LoaiGiayToTuyThan: 8")
    return '\n'.join(dong_moi)

# Sử dụng hàm
# thongtin_moi = kiem_tra_va_them_loai_giay_to(thongtin)
# print(thongtin_moi)
print(txtenfile("KS.2017.01.2017-02-03.05.pdf"))