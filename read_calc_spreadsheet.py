import uno

def read_calc_spreadsheet(file_path):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    doc = desktop.loadComponentFromURL(file_path, "_blank", 0, ())
    sheets = doc.getSheets()
    sheet = sheets.getByIndex(0)
    cell = sheet.getCellByPosition(0, 0)  # A1 cell
    print(cell.getString())
    doc.close(True)

if __name__ == "__main__":
    file_path = "file:///path/to/your/spreadsheet.ods"
    read_calc_spreadsheet(file_path)