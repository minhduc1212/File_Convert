import os
import re

# Đọc nội dung file truyện
with open("1.txt", "r", encoding="utf-8") as f:
    content = f.readlines()

# Khởi tạo biến để theo dõi mục lục và nội dung chương
toc = []
chapter_title = ""
chapter_content = ""
in_chapter = False

# Duyệt qua từng dòng trong nội dung file truyện
for line in content:
    line = line.strip()
    
    # Nếu dòng rỗng, bỏ qua
    if not line:
        continue
    
    # Kiểm tra xem dòng hiện tại có chứa "Chapter" (mục lục) hay không
    if line.startswith("Chương "):
        print(line)
        if in_chapter:
            toc.append(chapter_title)
            chapter_filename = f"{chapter_title}.html"
            #Loại bỏ các ký tự đặc biệt trong tên file
            chapter_filename = re.sub(r'[\\/:*?"<>|]', ' ', chapter_filename)
            
            with open(chapter_filename, "w", encoding="utf-8") as chapter_file:
                    chapter_file.write(f"<h1 class=\"chapter\" id=\"{chapter_title}\">{chapter_title}</h1>\n")
                    chapter_file.write(chapter_content)
        
        # Bắt đầu chương mới
        chapter_title = line
        in_chapter = True
    elif in_chapter:
        # Thêm nội dung của chương
        chapter_content += f"<p>{line}</p>\n"

# Sau khi duyệt xong, lưu nội dung chương cuối cùng
if in_chapter:
    toc.append(chapter_title)
    chapter_filename = f"{chapter_title}.html"
    chapter_filename = re.sub(r'[\\/:*?"<>|]', ' ', chapter_filename)
    with open(chapter_filename, "w", encoding="utf-8") as chapter_file:
        chapter_file.write(f"<h1 class=\"chapter\" id=\"{chapter_title}\">{chapter_title}</h1>\n")
        chapter_file.write(chapter_content)

# Tạo file mục lục
with open("Mục Lục.html", "w", encoding="utf-8") as toc_file:
    for chapter in toc:
        toc_file.write(f'<p><a href="#{chapter}">{chapter}</a></p>\n')

#list các file html có từ "Chương" trong tên
html_files = [f for f in os.listdir(".") if f.endswith(".html") and "Chương" in f]
html_files.sort(key=lambda f: int(re.search(r'Chương (\d+)', f).group(1)))

html_template_head ="<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<style>\nbody{font-family:\"Times New Roman\",Times,serif;\n line-height: 1.2;}\n</style>\n</head>\n<body>\n"
#tạo file html mới
with open("truyen.html", "w", encoding="utf-8") as f:
    f.write(html_template_head)
    f.write("<h1>Mục Lục</h1>\n")
    with open ("Mục Lục.html", "r", encoding="utf-8") as tc_file:
        tc_content = tc_file.read()
        f.write(tc_content)
    for html_file in html_files:
        with open(html_file, "r", encoding="utf-8") as chapter_file:
            chapter_content = chapter_file.read()
            f.write(chapter_content)
            f.write("<hr>\n")
    f.write("</body>\n</html>")
#xóa các file html cũ
for html_file in html_files:
    os.remove(html_file)
os.remove("Mục Lục.html")
print("Done!")
