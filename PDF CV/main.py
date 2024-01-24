from PIL import Image
from PyPDF2 import PdfWriter
import os

def convert_images_to_pdf(image_paths, output_path):
    pdf_writer = PdfWriter()

    for image_path in image_paths:
        image = Image.open(image_path)
        pdf_writer.add_page(image.convert('RGB'))

    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

# Đường dẫn của thư mục chứa các tệp tin ảnh
image_directory = 'E:\T\TTr\Thiên Thanh\Thiên Thanh Chap 1'

# Tạo danh sách đường dẫn đến các tệp tin ảnh trong thư mục
image_paths = [os.path.join(image_directory, filename) for filename in os.listdir(image_directory)]

# Đường dẫn của file PDF đầu ra
output_path = 'output.pdf'

# Chuyển đổi ảnh thành PDF
convert_images_to_pdf(image_paths, output_path)