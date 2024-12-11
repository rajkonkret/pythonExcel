import pandas as pd

writer = pd.ExcelWriter('empty_file.xlsx', engine='xlsxwriter')
empty_dataframe=pd.DataFrame()
empty_dataframe.to_excel(writer, sheet_name='empty')
writer.close()