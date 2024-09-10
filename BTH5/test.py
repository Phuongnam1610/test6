"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

import os
import google.generativeai as genai
from config import get_setting
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

# TODO Make these files available on the local file system
# You may need to update the file paths
# Lấy danh sách tất cả các tệp trong thư mục
image_folder = get_setting("IMGFOLDER")
image_files = [f for f in os.listdir(image_folder) if f.endswith('.png')]

# Tạo danh sách files bằng cách duyệt qua từng tệp ảnh
files = []
for image_file in image_files:
    file_path = os.path.join(image_folder, image_file)
    files.append(upload_to_gemini(file_path, mime_type="image/png"))

chat_session = model.start_chat(
  history=[
    {
      "role": "user",
      "parts": [
        files[0],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 81\nnguoiKy: Trần Quyết\nchucVuNguoiKy:Phó Chủ tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Phan Thanh Nhàn\nnksNgaySinh: 12.11.2007\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, phường Mỹ Hương, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: An Hải, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Cẩm\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Phan Văn Luôn\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Phan Văn Chiêm\nnycQuanHe: Bác ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[1],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 117\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Nguyễn Quốc Sang\nnksNgaySinh: 20. 04. 2008\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, phường Mỹ Hương, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Phước Dân, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Trương Thị Chính \nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Quốc Trung\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Quốc Trung\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[2],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 130\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Nguyễn Thị Thanh Thùy\nnksNgaySinh: 11. 01. 2008\nnksNoiSinh: Trung tâm y tế Ninh Hòa, Ninh Hòa, Ninh Thuận\nnksQueQuan: Xuân Hải, Sông Cầu, Phú Yên\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Thoa\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Thanh Tuấn\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Thanh Tuấn\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[3],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 160\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Đoàn Mai Bảo Ngọc\nnksNgaySinh: 29. 10. 2008\nnksNoiSinh: Bệnh viện Ninh Phước, Thị trấn Phước Dân, Ninh Phước Ninh Thuận\nnksQueQuan: Minh Thuận, Vụ Bản, Nam Định\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Hồng\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Đoàn Quang Hiền\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Đoàn Quang Hiền\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[4],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 170\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Võ Hoàng Dũng\nnksNgaySinh: 19.07. 2008\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, phường Mỹ Hương, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Phú Hảo, Phú Hưng, Bến Tre\nnksDanToc: Kinh\nmeHoTen: Kiều Thị Mỹ Hoa\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Võ Văn Hùng\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Kiều Thị Mỹ Hòa\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[5],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 172\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Trịnh Sao Bay\nnksNgaySinh: 28. 10. 2008\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, phường Mỹ Hương, Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Phước Diêm, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Trịnh Thị Nhường\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen:\nchaNgaySinh:\nchaDanToc:\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Trịnh Thị Nhường\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[6],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 182\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Nguyễn Văn Thuận\nnksNgaySinh: 23. 10. 2008\nnksNoiSinh: Lạc Tiến, Phước Minh, Ninh Phước, Ninh Thuận\nnksQueQuan: Nhơn Hải, Ninh Hải, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Phạm Thị Nhẹ\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Văn Hòa\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Văn Hòa\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[7],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 187\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Lương Hương Giang\nnksNgaySinh: 23. 12. 2008\nnksNoiSinh: Trung tâm Y tế Ninh Phước, Phước Dân, Ninh Phước, Ninh Thuận\nnksQueQuan: Hưng Phú, Hưng Nguyên, Nghệ An\nnksDanToc: Kinh\nmeHoTen: Phan Thị Thu Hồng\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Lương Anh Tuấn\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Thị Hoa\nnycQuanHe: Bác ngoại\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[8],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 224\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Trần Hoài Phong\nnksNgaySinh: 21. 03. 2009\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, Phường Mỹ Hương, Thành Phố Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Đông Hải, Phan Rang, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Võ Thị Huấn\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Trần Lắm\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Trần Lân\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[9],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 232\nnguoiKy: Trần Quốc Hoàn\nchucVuNguoiKy: Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Phạm Văn Long\nnksNgaySinh: 30. 11. 1981\nnksNoiSinh:  Trung Trạch, Bố Trạch, Quảng Bình\nnksQueQuan: Trung Trạch, Bố Trạch, Quảng Bình\nnksDanToc: Kinh\nmeHoTen:  Dương Thị Mai\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Phạm Văn Hiệp\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Phạm Văn Hiệp\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[10],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 233\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Trần Chí Thanh\nnksNgaySinh: 26. 06. 2001\nnksNoiSinh: Lạc  Tiến, Phước Minh, Ninh Phước, Ninh Thuận\nnksQueQuan: Tấn  Tài, Phan Rang - Tháp Chàm, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Trần Thị Công Trơn\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: \nchaNgaySinh:\nchaDanToc:\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Trần Trịnh Luân\nnycQuanHe: Anh trai\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[11],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 246\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Lê Ngọc Hoài An\nnksNgaySinh: 13. 08. 2009\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, Phường Mỹ Hương, Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Văn Hải, Phan Rang - Tháp Chàm, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Hồng Xuân\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Lê Xuân Hiếu\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Hồ Thị Mỹ Thiện\nnycQuanHe: Bà nội\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[12],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 250\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Nguyễn Thị Như Quỳnh\nnksNgaySinh: 02. 08. 2007\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, Phường Mỹ Hương, Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Quảng Ngãi\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Ngọc Duyên\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Minh Phú\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Minh Phú\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[13],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 257\nnguoiKy: Trần  Mai Trang\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: \nnksHoTen: Nguyễn Thái  Thiệu  Nhiên\nnksNgaySinh: 02. 08. 2009\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, Phường Mỹ Hương, Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Phước Dân, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Mai Thị Ngọc Hằng\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Thái Thức\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Mai Thị Ngọc Hằng\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[14],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 257\nnguoiKy: Trần  Mai Trang\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: \nnksHoTen: Nguyễn Thái  Thiên Nhiên\nnksNgaySinh: 02.08.2009\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, Phường Mỹ Hương, Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Phước Dân, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Mai Thị Ngọc Hằng\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Thái Thục\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Mai Thị Ngọc Hằng\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[15],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 265\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Trần Thị Thục\nnksNgaySinh: 19.08.1984\nnksNoiSinh:  Xóm 7 Nam Lân, Diễn Lân, Diễn Châu, Nghệ An\nnksQueQuan: Xóm 7 Nam Lân, Diễn Lân, Diễn Châu, Nghệ An\nnksDanToc: Kinh\nmeHoTen: Phạm Thị  Mã\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Trần Thanh Bình\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Trần Thị Thục\nnycQuanHe: Tự khai\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[16],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 273\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Phạm Thị  Trà  My\nnksNgaySinh: 26.09.2009\nnksNoiSinh:  Quán Thẻ, Phước  Minh, Thuận Nam, Ninh Thuận\nnksQueQuan:  Nhơn  Ái, Châu Thành,  Hậu Giang\nnksDanToc: Kinh\nmeHoTen: Phạm Thị Thu Hiền\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen:\nchaNgaySinh:\nchaDanToc:\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Phạm Thị Thu Hiền\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[17],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 284\nnguoiKy: Trần Quốc Hoàn\nchucVuNguoiKy: Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Bùi Thị  Dung\nnksNgaySinh: 20.03.1987\nnksNoiSinh: An  Quý,  Quỳnh  Phụ, Thái  Bình\nnksQueQuan: An Quý, Quỳnh Phụ, Thái Bình\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị  Ruyến\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Bùi Công Lê\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Thị  Ruyến\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[18],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 103\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Nguyễn Ngọc Hải Đăng\nnksNgaySinh: 07.03.2008\nnksNoiSinh: Bệnh viện đa khoa Hạnh Phúc. Long Xuyên, An Giang\nnksQueQuan: An Châu, Châu Thành, An Giang\nnksDanToc: Kinh\nmeHoTen: Phạm Thị  Linh\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Hữu Thắng\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Hữu Thắng\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[19],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 113\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Trần Thị  Hiền\nnksNgaySinh: 30.12.2000\nnksNoiSinh: Lạc Tiến, Phước Minh, Ninh Phước, Ninh Thuận\nnksQueQuan: Thụy  Dương,  Thái Thuý,  Thái Bình\nnksDanToc: Kinh\nmeHoTen: Ngô Thị Nhúng\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Trần Trọng Vinh\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Trần Trọng Vinh\nnycQuanHe: Cha ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n",
      ],
    },
    {
      "role": "user",
      "parts": [
        files[20],
      ],
    },
    {
      "role": "model",
      "parts": [
        "trangSo: 114\nnguoiKy: Trần Quyết\nchucVuNguoiKy: Phó Chủ Tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Trần Nguyễn Chí Cường\nnksNgaySinh: 20.09.2005\nnksNoiSinh: Trạm y tế xã Phước Minh, Ninh Phước, Ninh Thuận\nnksQueQuan: Tân Hải, Ninh Hải, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Hồng\nmeNgaySinh:\nmeDanToc: Kinh\nmeNoiCuTru:\nmeSoGiayToTuyThan:\nchaHoTen: Trần Thanh Phong\nchaNgaySinh:\nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Thị Hồng\nnycQuanHe: Mẹ ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan:\nnycNoiCapGiayToTuyThan:\n\n\n\n\n\n\n",
      ],
    },
  ]
)

response = chat_session.send_message("INSERT_INPUT_HERE")

print(response.text)