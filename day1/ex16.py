import pandas as pd

df = pd.read_excel('../data/excel_without_index-1.xlsx')
print("The dataframe is:")
print(df)

suma = df['Height'].sum(skipna=False)
print("Suma:", suma)
# The dataframe is:
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167
# Suma: 697