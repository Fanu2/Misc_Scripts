import uno

def write_to_calc_spreadsheet(file_path, row, col, content):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    doc = desktop.loadComponentFromURL(file_path, "_blank", 0, ())
    sheets = doc.getSheets()
    sheet = sheets.getByIndex(0)
    cell = sheet.getCellByPosition(col, row)
    cell.setString(content)
    doc.store()
    doc.close(True)

if __name__ == "__main__":
    file_path = "file:///path/to/your/spreadsheet.ods"
    row = 0
    col = 0
    content = "Hello, LibreOffice!"
    write_to_calc_spreadsheet(file_path, row, col, content)