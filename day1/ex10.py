import pandas as pd

data = [
    {"Name": "Aditya", "Height": 179},
    {"Name": "Sameer", "Height": 181},
    {"Name": "Daarwin", "Height": 170},
    {"Name": "Aditya", "Height": 167},
]
df = pd.DataFrame(data)
print(df)

writer = pd.ExcelWriter('../day2/excel_with_dict.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='first_sheet', index=False)
writer.close()
