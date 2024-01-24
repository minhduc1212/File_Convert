from PIL import Image
import os
from PyPDF2 import PdfWriter
import shutil

output_dir = 'E:/LT/File Convert/PDF CV/1'
source_dir = 'E:/LT/File Convert/PDF CV/Bill'
pdf_names = [] 
merger = PdfWriter()

for file in os.listdir(source_dir):
    if file.split('.')[-1] in ('png', 'jpg', 'jpeg'):
        image = Image.open(os.path.join(source_dir, file))
        image_converted = image.convert('RGB')
        pdf_name = "{}.pdf".format(file.split('.')[-2])
        pdf_names.append(pdf_name)
        image_converted.save(os.path.join(output_dir, pdf_name))

for pdf in pdf_names:
    merger.append(os.path.join(output_dir, pdf))  # Cung cấp đường dẫn đầy đủ của tệp tin

merger.write("merged-pdf.pdf")
merger.close()

if os.path.exists(output_dir):  # Kiểm tra xem thư mục tồn tại hay không
    shutil.rmtree(output_dir)  # Xóa thư mục và nội dung bên trong
    print(f"Thư mục {output_dir} đã được xóa thành công.")
else:
    print(f"Thư mục {output_dir} không tồn tại.")