import os
# import logging
# chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"
import requests
from tailieu import tailieu
from convertpdftopng import convert_pdf_to_png
from convertpngtotext import *
from taobody import tao_body_gui_di
from callapi import gui_api_request
# Tạo thư mục allpdf nếu chưa tồn tại
if not os.path.exists("allpdf"):
    os.makedirs("allpdf")

def getname(chuoi_goc):
    vi_tri_bat_dau = chuoi_goc.upper().rfind("KS")
    vi_tri_ket_thuc = chuoi_goc.rfind(".pdf") + 4  # +4 để bao gồm cả ".pdf"
    if vi_tri_bat_dau != -1 and vi_tri_ket_thuc != -1:
        ket_qua = chuoi_goc[vi_tri_bat_dau:vi_tri_ket_thuc]
        return ket_qua
    else:
        return None
def trich_xuat_ks(ten_file):
    # Tìm vị trí của "KS" (không phân biệt chữ hoa/thường)
    vi_tri_ks = ten_file.upper().find("KS")
    if vi_tri_ks != -1:
        # Trích xuất phần sau "KS."
        phan_sau_ks = ten_file[vi_tri_ks+3:]
        # Tìm vị trí của dấu chấm đầu tiên sau "KS."
        vi_tri_cham = phan_sau_ks.find(".")
        if vi_tri_cham != -1:
            # Trích xuất 7 ký tự từ vị trí sau "KS."
            ket_qua = phan_sau_ks[:vi_tri_cham+3]
            return ket_qua
    return None  
# driver =create_driver()
# driver.get(f"https://ninhthuan.dvcg.vn/nhap-lieu")
# wait = WebDriverWait(driver, timeout=15)
# driver.get("https://ninhthuan.dvcg.vn/nhap-lieu")
# fulltl=wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'ng-star-inserted')))
from config import update_setting
from getidandname import *
while True:
    saved=input("lay o save thi chon 1, con lai chon 0 ")
    update_setting('SAVED', saved)
    result = call_ninhthuan_api()
    listidtf=trich_xuat_id_va_ten_file(result)
    listtl=[]
    for i in listidtf:
        try:
            linkpdf = f"https://ninhthuan-api.dvcg.vn/uploads/ho_tich_ninh_thuan/tinhninhthuan/huyenthuannam/xaphuocminh/ks/{trich_xuat_ks(i[1])}/{i[1]}"
        #     # Tải xuống tệp PDF
            response = requests.get(linkpdf)
            if response.status_code == 200:
                pdf_filename = os.path.join("allpdf", f"{i[1]}")
                with open(pdf_filename, "wb") as f:
                    f.write(response.content)
                print(f"Đã tải xuống: {pdf_filename}")
            else:
                print(f"Không thể tải xuống: {linkpdf}")
                continue
            listtl.append(tailieu(i[1],i[0]))
        except Exception as e:
            print(e)
            continue
    convert_pdf_to_png()
    for i,v in enumerate(listtl):
        try:
            print(f"thực hiện file {(i+1)}/{len(listtl)}")
            print(v.id)
            print(v.ten)
            v.body=tao_body_gui_di(chuyen_thanh_text(v.ten.replace('.pdf','.png')),v.ten,v.id)
            print(gui_api_request(v.body))
            print(f"file {v.ten} thực hiện thành công")
        except Exception as e:
            print(e)
            continue
    
