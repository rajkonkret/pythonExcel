
import pandas as pd


# df = pd.read_excel('../data/excel_with_multiple_sheets-1.xlsx', sheet_name=2)
# df = pd.read_excel('../data/excel_with_multiple_sheets-1.xlsx', sheet_name="marks")
data = pd.ExcelFile('../data/excel_with_multiple_sheets-1.xlsx')
print(data.sheet_names)  # ['height', 'weight', 'marks']
# df = pd.read_excel('../data/excel_with_multiple_sheets-1.xlsx', sheet_name=df.sheet_names[0])
# print(df)
# df = pd.read_excel('../data/excel_with_multiple_sheets-1.xlsx', sheet_name="marks", usecols=["Name"])
print(data)
df = data.parse("height")
print(df.head())
print(df)
print(df.columns.tolist())  # ['Name', 'Height']
