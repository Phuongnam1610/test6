import os
import fitz  # PyMuPDF

def convert_pdf_to_png():
    if not os.path.exists('allpng'):
        os.makedirs('allpng')

    for filename in os.listdir('allpdf'):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join('allpdf', filename)
            doc = fitz.open(pdf_path)
            
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                pix = page.get_pixmap()
                png_filename = f"{os.path.splitext(filename)[0]}.png"
                png_path = os.path.join('allpng', png_filename)
                pix.save(png_path)
            
            doc.close()
    
    print("Quá trình chuyển đổi đã hoàn tất.")
