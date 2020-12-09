import openpyxl


def read(i, j):
    loc = r"C:\Users\GT Sanatorium\PycharmProjects\Ecom\placeOrder\TestData\search.xlsx"
    book = openpyxl.load_workbook(loc)
    active_sheet = book.active
    current_cell = active_sheet.cell(i, j)
    data = current_cell.value
    return data
