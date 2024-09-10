import requests
from config import get_setting,update_setting
def call_ninhthuan_api(is_inputted=False, is_reviewed=False,  page_index=0, page_size=20):
    
    for i in range(10):
        try:
            input_status=get_setting('SAVED')
            project_id=get_setting('PROJECTID')
            url = 'https://ninhthuan-api.dvcg.vn/document/getassigneddocuments'
            params = {
                'ProjectId': project_id,
                'IsInputted': str(is_inputted).lower(),
                'IsReviewed': str(is_reviewed).lower(),
                'InputStatus': input_status,
                'PageIndex': page_index,
                'PageSize': page_size
            }
            
            headers = {
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9,vi;q=0.8',
                'authorization': f"{get_setting('BAREKEY')}",
                'origin': 'https://ninhthuan.dvcg.vn',
                'referer': 'https://ninhthuan.dvcg.vn/',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
            }
            
            response = requests.get(url, params=params, headers=headers)
            
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Lỗi: {response.status_code}")
                print(response.text)
                key=input("nhap key moi")
                update_setting('BAREKEY', key)
                continue
        except Exception as e:
            print(e)
            key=input("nhap key moi")
            update_setting('BAREKEY', key)
def trich_xuat_id_va_ten_file(du_lieu_json):
    ket_qua = []
    try:
        # print('tong tai lieu',du_lieu_json['result']['total'])
        danh_sach_tai_lieu = du_lieu_json['result']['listDocument']
        # print(len(danh_sach_tai_lieu))
        for tai_lieu in danh_sach_tai_lieu:
            id = tai_lieu['id']
            ten_file = tai_lieu['originalFileName']
            ket_qua.append((id, ten_file))
    except KeyError:
        print("Lỗi: Không tìm thấy dữ liệu cần thiết trong JSON")
    return ket_qua
# Sử dụng hàm


# print(len(listidtf))
