import pandas as pd

# Đường dẫn đến file Excel ban đầu
input_file = "merged_file.xlsx"

# Đọc file Excel và lấy dữ liệu
data = pd.read_excel(input_file)

# Chia đôi dữ liệu thành hai DataFrame
half_rows = len(data) // 2
df1 = data.iloc[:half_rows]
df2 = data.iloc[half_rows:]

# Đường dẫn đến file Excel chia đôi 1
output_file1 = "split_file1.xlsx"
df1.to_excel(output_file1, index=False)

# Đường dẫn đến file Excel chia đôi 2
output_file2 = "split_file2.xlsx"
df2.to_excel(output_file2, index=False)

print("Đã chia đôi file Excel thành công!")