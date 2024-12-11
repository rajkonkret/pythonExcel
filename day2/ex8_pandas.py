import pandas as pd

# pip install xlsxwriter
# pip install pandas

writer = pd.ExcelWriter('../data/empty_file.xlsx', engine='xlsxwriter')
empty_dataframe = pd.DataFrame()
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()
