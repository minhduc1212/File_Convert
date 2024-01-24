import re

path = "E:/LT/File Convert/output"
# Đọc nội dung file truyện
with open("1.txt", "r", encoding="utf-8") as f:
    content = f.readlines()

# Khởi tạo biến để theo dõi mục lục và nội dung chương
toc = []

html_head_template = "<!DOCTYPE html>\n<html>\n<head>\n<meta charset=\"utf-8\">\n<link rel=\"stylesheet\" href=\"style.css\">\n</head>\n<body>\n"
html_foot_template = "</body>\n</html>"
# Duyệt qua từng dòng trong nội dung file truyện
for line in content:
    line = line.strip()

    # Nếu dòng rỗng, bỏ qua
    if not line:
        continue
    
    if line.startswith("Chương"):
        # Khi tìm thấy dòng bắt đầu bằng "Chương", tạo file HTML mới cho chương đó
        chapter_title = line
        chapter_title = re.sub(r'[\\/:*?"<>|]', ' ', chapter_title)
        filename = f"{chapter_title}.html"
        filename = re.sub(r'[\\/:*?"<>|]', ' ', filename)
        
        with open(f"{path}/{filename}", "w", encoding="utf-8") as chapter_file:
            chapter_file.write(html_head_template)
            chapter_file.write(f"<h1 class=\"chapter\" id=\"{chapter_title}\">{chapter_title}</h1>\n")

        if toc and toc[-1] != chapter_title:
            current_chapter = toc[-1]
            filename = f"{current_chapter}.html"        
            filename = re.sub(r'[\\/:*?"<>|]', ' ', filename)
            with open(f"{path}/{filename}", "a", encoding="utf-8") as f:
                f.write(html_foot_template)             

        toc.append(chapter_title)
    else:
        # Nếu không phải là dòng bắt đầu chương, thêm nội dung vào file HTML hiện tại
        if toc:
            current_chapter = toc[-1]
            filename = f"{current_chapter}.html"
            filename = re.sub(r'[\\/:*?"<>|]', ' ', filename)
            with open(f"{path}/{filename}", "a", encoding="utf-8") as chapter_file:
                chapter_file.write(f"<p>{line}</p>\n")

#tạo file mục lục
with open(f"{path}/toc.html", "w", encoding="utf-8") as toc_file:
    toc_file.write(html_head_template)
    toc_file.write("<h1 class=\"toc\">Mục Lục</h1>\n")
    for chapter_title in toc:
        chapter_title = re.sub(r'[\\/:*?"<>|]', ' ', chapter_title)
        toc_file.write(f"<p><a href=\"{chapter_title}.html\">{chapter_title}</a></p>\n")
    toc_file.write(html_foot_template)

#tạo file css
with open(f"{path}/style.css", "w", encoding="utf-8") as css_file:
    css_file.write("body{font-family:\"Times New Roman\",Times,serif;\ndisplay:block;\n}\n")

#tạo file content.opf
content_opf_head_template = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<package xmlns=\"http://www.idpf.org/2007/opf\" version=\"2.0\" unique-identifier=\"uuid_id\">\n<metadata xmlns:opf=\"http://www.idpf.org/2007/opf\" xmlns:dc=\"http://purl.org/dc/elements/1.1/\" xmlns:dcterms=\"http://purl.org/dc/terms/\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xmlns:calibre=\"http://calibre.kovidgoyal.net/2009/metadata\">\n</metadata>"
content_opf_foot_template = "</package>"
with open(f"{path}/content.opf", "w", encoding="utf-8") as content_file:
    content_file.write(content_opf_head_template)
    content_file.write("<manifest>\n")
    content_file.write("<item href=\"toc.html\" id=\"toc\" media-type=\"application/xhtml+xml\"/>\n")
    for chapter_title in toc:
        chapter_title = re.sub(r'[\\/:*?"<>|]', ' ', chapter_title)
        content_file.write(f"<item href=\"{chapter_title}.html\" id=\"{chapter_title}\" media-type=\"application/xhtml+xml\"/>\n")
    content_file.write("<item href=\"style.css\" id=\"css\" media-type=\"text/css\"/>\n")
    content_file.write("</manifest>\n")
    content_file.write("<spine toc=\"ncx\">\n")
    content_file.write("<itemref idref=\"toc\"/>\n")
    for chapter_title in toc:
        chapter_title = re.sub(r'[\\/:*?"<>|]', ' ', chapter_title)
        content_file.write(f"<itemref idref=\"{chapter_title}\"/>\n")
    content_file.write("</spine>\n")
    content_file.write(content_opf_foot_template)

#tạo file toc.ncx
toc_ncx_head_template = "<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<ncx xmlns=\"http://www.daisy.org/z3986/2005/ncx/\" version=\"2005-1\">\n<head>\n<meta content=\"uuid_id\" name=\"dtb:uid\"/>\n<meta content=\"2\" name=\"dtb:depth\"/>\n<meta content=\"0\" name=\"dtb:totalPageCount\"/>\n<meta content=\"0\" name=\"dtb:maxPageNumber\"/>\n</head>\n<docTitle>\n<text>Truyện</text>\n</docTitle>\n<navMap>"
toc_ncx_foot_template = "</navMap>\n</ncx>"

with open(f"{path}/toc.ncx", "w", encoding="utf-8") as toc_ncx_file:
    toc_ncx_file.write(toc_ncx_head_template)
    for chapter_title in toc:
        chapter_title = re.sub(r'[\\/:*?"<>|]', ' ', chapter_title)
        toc_ncx_file.write(f"<navPoint id=\"{chapter_title}\" playOrder=\"{toc.index(chapter_title) + 1}\">\n<navLabel>\n<text>{chapter_title}</text>\n</navLabel>\n<content src=\"{chapter_title}.html\"/>\n</navPoint>\n")
    toc_ncx_file.write(toc_ncx_foot_template)