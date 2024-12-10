import openpyxl

from ex3 import total_sales

wb = openpyxl.load_workbook('../data/videogamesales.xlsx')
ws = wb.active

ws = wb['vgsales']

row_position = 1
for i in range(1, ws.max_row):
    row_position += 1  # i = i + 1
    NA_Sales = ws.cell(row=row_position, column=7).value
    EU_Sales = ws.cell(row=row_position, column=8).value
    JP_Sales = ws.cell(row=row_position, column=9).value
    Other_Sales = ws.cell(row=row_position, column=10).value

    total_sales = (NA_Sales + EU_Sales + JP_Sales + Other_Sales)
    ws.cell(row=row_position, column=11).value = total_sales

wb.save('videogamesales.xlsx')  # save the updated workbook)
