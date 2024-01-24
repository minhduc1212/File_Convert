#ghép các file html thành một file html duy nhất
import os
import re

#list các file html có từ "Chương" trong tên
html_files = [f for f in os.listdir(".") if f.endswith(".html") and "Chương" in f]
html_files.sort(key=lambda f: int(re.search(r'Chương (\d+)', f).group(1)))

html_template_head ="<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<style>\nbody{font-family:\"Times New Roman\",Times,serif;}\n</style>\n</head>\n<body>\n"
#tạo file html mới
with open("truyen.html", "w", encoding="utf-8") as f:
    """f.write(html_template_head)
    f.write("<h1>Mục Lục</h1>\n")
    with open ("Mục Lục.html", "r", encoding="utf-8") as tc_file:
        tc_content = tc_file.read()
        f.write(tc_content)
        f.write("<hr>\n")"""
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