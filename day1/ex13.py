import pandas as pd

df = pd.read_excel('../data/excel_without_index-1.xlsx')
print("The dataframe is:")
print(df)
# The dataframe is:
#        Name  Height
# 0    Aditya     179
# 1    Sameer     181
# 2  Dharwish     170
# 3      Joel     167
print(type(df))  # <class 'pandas.core.frame.DataFrame'>
