import os
import pandas as pd

# Thư mục chứa các file XLSX
folder_path = "E:\LT\File Convert\split"

# Tìm tất cả các file XLSX trong thư mục
file_paths = []
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith(".xlsx"):
            file_paths.append(os.path.join(root, file))

# Đọc các file XLSX và lưu dữ liệu vào một DataFrame
dfs = []
for file_path in file_paths:
    df = pd.read_excel(file_path)
    dfs.append(df)

data = pd.concat(dfs, ignore_index=True)

# Lưu DataFrame vào một file XLSX mới
output_file = "merged_file.xlsx"
data.to_excel(output_file, index=False)

print("Đã tìm và ghép các file thành công!")