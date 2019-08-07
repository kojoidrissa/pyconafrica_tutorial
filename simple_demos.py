from openpyxl import Workbook

wb_out = Workbook()
ws1 = wb_out.create_sheet("Kojo", 0)
ws1["b2"] = 99
wb_out.save('kojo_demo.xlsx')

def akwaaba(name):
    print(f"Welcome {name}")