import requests
from config import get_setting,update_setting

def gui_api_request(payload):

    for i in range(10):
        try:
            print(" đang gửi api")
            url = 'https://ninhthuan-api.dvcg.vn/document/savedocumentmapping'
            
            headers = {
                'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
                'sec-ch-ua-mobile': '?0',
            'Authorization': f"{get_setting('BAREKEY')}",
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Referer': 'https://ninhthuan.dvcg.vn/',
            'sec-ch-ua-platform': '"Windows"'
        }
            response = requests.post(url, headers=headers, json=payload)
            return response.json()
        except Exception as e:
            key=input("nhap key moi")
            update_setting('BAREKEY', key)
            print(e)
            

# Sử dụng hàm
# payload = {
#     "projectId": "d0ad433e-f36b-1410-8c7f-008f0b9cddcc",
#     "documentId": "6db45504-9d3d-ef11-94e9-b8ca3aeb783a",
#     "mappingData": "[{\"so\":\"24\",\"quyenSo\":\"01/2017\",\"trangSo\":\"\",\"ngayDangKy\":\"17.03.2018\",\"loaiDangKy\":0,\"noiDangKy\":\"\",\"nguoiKy\":\"\",\"chucVuNguoiKy\":\"\",\"nguoiThucHien\":\"\",\"ghiChu\":\"\",\"nksHoTen\":\"\",\"nksGioiTinh\":0,\"nksNgaySinh\":\"\",\"nksNgaySinhBangChu\":\"\",\"nksNoiSinh\":\"\",\"nksNoiSinhDVHC\":\"\",\"nksQueQuan\":\"\",\"nksDanToc\":\"\",\"nksQuocTich\":\"Việt Nam\",\"nksQuocTichKhac\":\"\",\"nksLoaiKhaiSinh\":0,\"nksMatTich\":0,\"nksMatTichNgayGhiChuTuyenBo\":\"\",\"nksMatTichCanCuTuyenBo\":\"\",\"nksMatTichNgayGhiChuHuyTuyenBo\":\"\",\"nksMatTichCanCuHuyTuyenBo\":\"\",\"nksHanCheNangLucHanhVi\":0,\"nksHanCheNangLucHanhViNgayGhiChuTuyenBo\":\"\",\"nksHanCheNangLucHanhViCanCuTuyenBo\":\"\",\"nksHanCheNangLucHanhViNgayGhiChuHuyTuyenBo\":\"\",\"nksHanCheNangLucHanhViNgayCanCuHuyTuyenBo\":\"\",\"meHoTen\":\"\",\"meNgaySinh\":\"\",\"meDanToc\":\"\",\"meQuocTich\":\"Việt Nam\",\"meQuocTichKhac\":\"\",\"meLoaiCuTru\":0,\"meNoiCuTru\":\"\",\"meLoaiGiayToTuyThan\":0,\"meSoGiayToTuyThan\":\"\",\"chaHoTen\":\"\",\"chaNgaySinh\":\"\",\"chaDanToc\":\"\",\"chaQuocTich\":\"Việt Nam\",\"chaQuocTichKhac\":\"\",\"chaLoaiCuTru\":0,\"chaNoiCuTru\":\"\",\"chaLoaiGiayToTuyThan\":0,\"chaSoGiayToTuyThan\":\"\",\"nycHoTen\":\"\",\"nycQuanHe\":\"\",\"nycLoaiGiayToTuyThan\":0,\"nycGiayToKhac\":\"\",\"nycSoGiayToTuyThan\":\"\",\"nycNgayCapGiayToTuyThan\":\"\",\"nycNoiCapGiayToTuyThan\":\"\",\"soDangKyNuocNgoai\":\"\",\"ngayDangKyNuocNgoai\":\"\",\"cqNuocNgoaiDaDangKy\":\"\",\"qgNuocNgoaiDaDangKy\":\"\"}]",
#     "action": 4
# }

# ket_qua = gui_api_request(payload)
# print(ket_qua)