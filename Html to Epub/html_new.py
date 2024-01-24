from bs4 import BeautifulSoup
import requests

#mở 1 file html
with open('E:/T/TC/Hứa Tiên Chí(Tác Giả Thuyết Mộng Thần)/Hứa Tiên Chí.html', 'r', encoding="utf-8" ) as f:
    file_content = f.read()

#tạo đối tượng soup
soup = BeautifulSoup(file_content, 'html.parser')
#tìm tất cả thẻ img
img_tags = soup.find_all('img')
for img_tag in img_tags:
    #lấy giá trị của thuộc tính href
    link = img_tag['src']
    #tải các ảnh về
    img_data = requests.get(link).content
    #tạo tên file
    filename = link.split('/')[-1]
    #lưu ảnh về ổ cứng với dạng jpg
    with open(f"E:/T/TC/Hứa Tiên Chí(Tác Giả Thuyết Mộng Thần)/{filename}", 'wb', ) as handler:
        handler.write(img_data)
    #thay đổi đường dẫn ảnh trong thẻ img và đặt img này là background
    img_tag['src'] = f"{filename}"
    img_tag['style'] = "display: block; margin: auto; width: auto; height: auto;"
    #thêm tag </br> vào sau thẻ img 
    img_tag.insert_after(soup.new_tag("br"))

for a in soup.find_all('a', {'class':'chapter-img'}):
    a.decompose()

#lưu file html mới  
with open('E:/T/TC/Hứa Tiên Chí(Tác Giả Thuyết Mộng Thần)/Hứa Tiên Chí - New.html', 'w', encoding="utf-8" ) as f:
    f.write(str(soup))
print("Done!")