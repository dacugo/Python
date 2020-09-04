import xlrd
filePath = "C:\\Users\\Daniel CG\\Desktop\\Prueba Todas\\Prueba Python\\BD_Comparaciones VF.xlsx"

openFile = xlrd.open_workbook(filePath)
sheet = openFile.sheet_by_name("BD_CONSOLIDADO_SIN_DATOS")
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))
print(sheet.cell_value(5,4))