"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""

"""
Install the Google AI Python SDK

$ pip install google-generativeai
"""
from config import get_setting
import os
import google.generativeai as genai
from natsort import natsorted

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
  "temperature": 0,
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


# TODO Make these files available on the local file system
# You may need to update the file paths
image_folder = get_setting("IMGFOLDER")
image_files = natsorted([f for f in os.listdir(image_folder) if f.endswith('.png')])
# Tạo danh sách files bằng cách duyệt qua từng tệp ảnh
files = []
for image_file in image_files:
    file_path = os.path.join(image_folder, image_file)
    files.append(upload_to_gemini(file_path, mime_type="image/png"))
def chatss(u):
    if(u==0):
        return model.start_chat(
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
    else:
       return model.start_chat(
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
        "trangSo: 09\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: Lưu Ngọc Tuấn\nnksNgaySinh: 19.01.1985\nnksNoiSinh: Lạc Nghiệp, Phước Diêm, Thuận Nam, Ninh Thuận\nnksQueQuan: Lạc Nghiệp, Phước Diêm, Thuận Nam, Ninh Thuận\nnksDanToc: Kinh\nnksSoDinhDanhCaNhan: \nmeHoTen: Nguyễn Thị Sanh\nmeNgaySinh: 1957\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: 264210067\nchaHoTen: Lưu Văn Hường (đã chết)\nchaNgaySinh: 1954\nchaDanToc: Kinh\nchaNoiCuTru: \nchaSoGiayToTuyThan: \nnycHoTen: Lưu Ngọc Tuấn\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 15\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: NGUYÊN THỊ THÙY DUNG\nnksNgaySinh: 02.4.1989\nnksNoiSinh: Phước Diêm, Thuận Nam, Ninh Thuận\nnksQueQuan: Phước Diêm, Thuận Nam, Ninh Thuận\nnksDanToc: Kinh\nnksSoDinhDanhCaNhan: \nmeHoTen: Trinh Thị Bến\nmeNgaySinh: 1954\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: 264283368\nchaHoTen: Nguyễn Văn Hay\nchaNgaySinh: 1949\nchaDanToc: Kinh\nchaNoiCuTru: Phước Diêm, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan: \nnycHoTen: NGUYÊN THỊ THÙY DUNG\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 18\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: NGUYỄN NGỌC XUÂN BÌNH\nnksNgaySinh: 08.02.2017\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, P. Văn Hải, TP. Phan Rang - Tháp Chàm, tỉnh Ninh Thuận\nnksQueQuan: Quảng Hòa, Quảng Xương, Thanh Hóa\nnksDanToc: Kinh\nnksSoDinhDanhCaNhan: 058317000772\nmeHoTen: Chu Văn Châu\nmeNgaySinh: 17.10.1990\nmeDanToc: Kinh\nmeNoiCuTru: Quán Thẻ 3, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: 174946812\nchaHoTen: Nguyễn Ngọc Dũng\nchaNgaySinh: 20.4.1990\nchaDanToc: Kinh\nchaNoiCuTru: Nam Xuân, Quan Hóa, Thanh Hóa\nchaSoGiayToTuyThan: \nnycHoTen: NGUYỄN NGỌC XUÂN BÌNH\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 28\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: LÊ THỊ NGỌC NHƯ\nnksNgaySinh: 03.3.2017\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, P. Văn Hải, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nnksSoDinhDanhCaNhan: 058317005765\nmeHoTen: Phạm Thị Ngọc Thanh\nmeNgaySinh: 19.11.1988\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: 264411258\nchaHoTen: Lê Thanh Lạc\nchaNgaySinh: 1977\nchaDanToc: Kinh\nchaNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan: \nnycHoTen: LÊ THỊ NGỌC NHƯ\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 21\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: TRẦN TRUNG NHỰT\nnksNgaySinh: 15.4.1973\nnksNoiSinh: Văn Sơn, Văn Hải, Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Văn Sơn, Văn Hải, Phan Rang - Tháp Chàm, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Trần Thị Công (đã chết)\nmeNgaySinh: \nmeDanToc: Kinh\nmeNoiCuTru: \nmeSoGiayToTuyThan: \nchaHoTen: Trần Ngọc Ánh (đã chết)\nchaNgaySinh: \nchaDanToc: Kinh\nchaNoiCuTru: \nchaSoGiayToTuyThan: \nnycHoTen: TRẦN TRUNG NHỰT\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 32\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: NGUYỄN TRẦN HOÀNG ĐĂNG\nnksNgaySinh: 13.10.2016\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, P. Văn Hải, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Hòa Chánh, Sơn Hòa, Châu Thành, Bến Tre\nnksDanToc: Kinh\nnksSoDinhDanhCaNhan: 058216005377\nmeHoTen: Trần Thị Tuyết Nhung\nmeNgaySinh: 29.9.1994\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: 264525871\nchaHoTen: Nguyễn Minh Hoàng\nchaNgaySinh: 08.01.1993\nchaDanToc: Kinh\nchaNoiCuTru: Ấp Hòa Chánh, xã Sơn Hòa, huyện Châu Thành, tỉnh Bến Tre\nchaSoGiayToTuyThan: \nnycHoTen: NGUYỄN TRẦN HOÀNG ĐĂNG\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 46\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: NGUYỄN THỊ PHI KIM YẾN\nnksNgaySinh: 18.4.2017\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, P. Văn Hải, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Phú Lộc, Thừa Thiên - Huế\nnksDanToc: Kinh\nnksSoDinhDanhCaNhan: 058317000857\nmeHoTen: Trần Thị Thu\nmeNgaySinh: 03.4.1979\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: 264206642\nchaHoTen: Nguyễn Hữu Hân\nchaNgaySinh: 05.01.1968\nchaDanToc: Kinh\nchaNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan: \nnycHoTen: NGUYỄN THỊ PHI KIM YẾN\nnycSoGiayToTuyThan: \nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan:",
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
        "trangSo: 58\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: PHẠM THỊ TUYẾT LINH\nnksNgaySinh: 22.10.1972\nnksNoiSinh: Phước Diêm, Thuận Nam, Ninh Thuận\nnksQueQuan: Xuân Hải, Ninh Hải, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: LƯU THỊ MỪNG\nmeNgaySinh: 1949\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: \nchaHoTen: PHẠM PHÚ HƯNG LONG\nchaNgaySinh: 1943\nchaDanToc: Kinh\nchaNoiCuTru: Phước Minh, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan: \nnycHoTen: PHẠM THỊ TUYẾT LINH\nnycSoGiayToTuyThan: 264206786\nnycNgayCapGiayToTuyThan: 30.6.2015\nnycNoiCapGiayToTuyThan: CA Ninh Thuận",
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
        "trangSo: 59\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: PHẠM THỊ THU THỦY\nnksNgaySinh: 16.3.1983\nnksNoiSinh: Tân Tiến, Yên Dũng, Bắc Giang\nnksQueQuan: Yên Dũng, Bắc Giang\nnksDanToc: Kinh\nmeHoTen: NGUYỄN THỊ MIẾT\nmeNgaySinh: 1940\nmeDanToc: Kinh\nmeNoiCuTru: Quán Thẻ 3, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan: \nchaHoTen: PHẠM HỒNG SINH (đã chết)\nchaNgaySinh: 1940\nchaDanToc: Kinh\nchaNoiCuTru: \nchaSoGiayToTuyThan: \nnycHoTen: PHẠM THỊ THU THỦY\nnycSoGiayToTuyThan: 264252141\nnycNgayCapGiayToTuyThan: 05.2.2015\nnycNoiCapGiayToTuyThan: CA Ninh Thuận",
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
        "trangSo: 61\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: NGUYỄN THỊ HOA\nnksNgaySinh: 10.12.1967\nnksNoiSinh: Trạm y tế xã Định Liên, huyện Thiệu Yên, tỉnh Thanh Hóa\nnksQueQuan: Định Liên, Thiệu Yên, Thanh Hóa\nnksDanToc: Kinh\nmeHoTen: Lê Thị Cong\nmeNgaySinh: \nmeDanToc: Kinh\nmeNoiCuTru: Thôn 7, xã Định Liên, huyện Thiệu Yên, tỉnh Thanh Hóa\nmeSoGiayToTuyThan: \nchaHoTen: Nguyễn Văn Cảnh (đã chết)\nchaNgaySinh: \nchaDanToc: Kinh\nchaNoiCuTru: \nchaSoGiayToTuyThan: \nnycHoTen: NGUYỄN THỊ HOA\nnycSoGiayToTuyThan: 264258105\nnycNgayCapGiayToTuyThan: 03.3.2016\nnycNoiCapGiayToTuyThan: CA Ninh Thuận",
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
        "trangSo: 63\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: NGUYỄN THỊ TÂM\nnksNgaySinh: 20.3.1958\nnksNoiSinh: Xuân Thọ, Xuân Lộc, Đồng Nai\nnksQueQuan: Xuân Thọ, Xuân Lộc, Đồng Nai\nnksDanToc: Kinh\nmeHoTen: Huỳnh Thị Sánh (đã chết)\nmeNgaySinh: \nmeDanToc: Kinh\nmeNoiCuTru: \nmeSoGiayToTuyThan:\nchaHoTen: Nguyễn Văn Tái (đã chết)\nchaNgaySinh: \nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Thị Tâm\nnycSoGiayToTuyThan: 264206650\nnycNgayCapGiayToTuyThan: 30.8.2011\nnycNoiCapGiayToTuyThan: CA Ninh Thuận",
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
        "trangSo: 82\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: ĐỖ THỊ BẢO NGỌC\nnksNgaySinh: 19.7.2017\nnksNoiSinh: Trung tâm y tế huyện Thuận Nam - Phước Nam, Thuận Nam, Ninh Thuận\nnksQueQuan: An Hải, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Thúy Linh\nmeNgaySinh: 20.10.1994\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan:\nchaHoTen: Đỗ Trọng Phúc\nchaNgaySinh: 20.4.1994\nchaDanToc: Kinh\nchaNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan:\nnycHoTen: Nguyễn Thị Thúy Linh\nnycSoGiayToTuyThan: 264435895\nnycNgayCapGiayToTuyThan: 06.3.2014\nnycNoiCapGiayToTuyThan: CA Ninh Thuận",
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
        "trangSo: 85\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: TRẦN NGUYỄN KHÁNH AN\nnksNgaySinh: 12.8.2017\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, P. Văn Hải, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Mũi Né, Phan Thiết, Bình Thuận\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Hồng Trang\nmeNgaySinh: 17.02.1991\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan:\nchaHoTen: Trần Văn Anh\nchaNgaySinh: 02.6.1982\nchaDanToc: Kinh\nchaNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan:\nnycHoTen: Trần Văn Anh\nnycSoGiayToTuyThan: 264525444\nnycNgayCapGiayToTuyThan: 25.10.2016\nnycNoiCapGiayToTuyThan: CAT Ninh Thuận",
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
        "trangSo: 86\nnguoiKy: Hoàng Xuân Thủy\nchucVuNguoiKy: Phó Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: HOÀNG TIẾN ĐẠT\nnksNgaySinh: 13.8.2017\nnksNoiSinh: Bệnh viện đa khoa khu vực Nam Bình Thuận -  xã Đức Chính, huyện Đức Linh, tỉnh Bình Thuận\nnksQueQuan: Hưng Hà, Thuận Bình\nnksDanToc: Kinh\nmeHoTen: NGÔ THỊ DUNG\nmeNgaySinh: 09.5.1985\nmeDanToc: Kinh\nmeNoiCuTru: Xã Vũ Hòa, huyện Đức Linh, tỉnh Bình Thuận\nmeSoGiayToTuyThan:\nchaHoTen: HOÀNG DUY TUẤN\nchaNgaySinh: 15.12.1985\nchaDanToc: Kinh\nchaNoiCuTru: Thôn Quan Thẻ 1 - xã Phước Minh, huyện Thuận Nam, tỉnh Ninh Thuận\nchaSoGiayToTuyThan:\nnycHoTen: Hoàng Văn Chuyển\nnycSoGiayToTuyThan: 264004287\nnycNgayCapGiayToTuyThan: 9.8.2016\nnycNoiCapGiayToTuyThan: CA Ninh Thuận\n\n\n\n\n",
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
        "trangSo: 05\nnguoiKy: Trần Mạnh Cương\nchucVuNguoiKy: Chủ tịch UBND Xã\nnguoiThucHien: Đỗ Thị Mai Trang\nnksHoTen: PHẠM VĂN QUỐC\nnksNgaySinh: 10.6.2010\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, phường Mỹ Hương, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: Thanh Hải, Ninh Hải, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Trần Thị Kim Cúc\nmeNgaySinh: 30.11.1987\nmeDanToc: Kinh\nmeNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nmeSoGiayToTuyThan:\nchaHoTen: Phạm Nhung\nchaNgaySinh: 1984\nchaDanToc: Kinh\nchaNoiCuTru: Lạc Tiến, Phước Minh, Thuận Nam, Ninh Thuận\nchaSoGiayToTuyThan:\nnycHoTen: Trần Thị Kim Cúc\nnycSoGiayToTuyThan: 264257877\nnycNgayCapGiayToTuyThan: 05.6.2012\nnycNoiCapGiayToTuyThan: CA Ninh Thuận\n\n",
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
        "trangSo: 81\nnguoiKy: Trần Quyết\nchucVuNguoiKy:Phó Chủ tịch UBND Xã\nnguoiThucHien: Nguyễn Ngọc Tuấn\nnksHoTen: Phan Thanh Nhàn\nnksNgaySinh: 12.11.2007\nnksNoiSinh: Bệnh viện tỉnh Ninh Thuận, phường Mỹ Hương, TP. Phan Rang - Tháp Chàm, Ninh Thuận\nnksQueQuan: An Hải, Ninh Phước, Ninh Thuận\nnksDanToc: Kinh\nmeHoTen: Nguyễn Thị Cẩm\nmeNgaySinh: \nmeDanToc: Kinh\nmeNoiCuTru: \nmeSoGiayToTuyThan:\nchaHoTen: Phan Văn Luôn\nchaNgaySinh: \nchaDanToc: Kinh\nchaNoiCuTru:\nchaSoGiayToTuyThan:\nnycHoTen: Phan Văn Chiêm\nnycQuanHe: Bác ruột\nnycSoGiayToTuyThan:\nnycNgayCapGiayToTuyThan: \nnycNoiCapGiayToTuyThan: ",
      ],
    },
  ]
)
def chuyen_thanh_text(msg):
  print("dang chuyen thanh text")
  response = chatss(get_setting("MODEL")).send_message(upload_to_gemini(f"allpng/{msg}", mime_type="image/png"))
  return (response.text)
