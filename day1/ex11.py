import pandas as pd

df = pd.read_csv("../data/height_file.csv")
# read_excel()

writer = pd.ExcelWriter('excel_from_csv.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name="first_sheet", index=False)
writer.close()
