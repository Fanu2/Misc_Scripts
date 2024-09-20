import uno

def read_writer_document(file_path):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    doc = desktop.loadComponentFromURL(file_path, "_blank", 0, ())
    text = doc.Text
    cursor = text.createTextCursor()
    content = text.getString()
    print(content)
    doc.close(True)

if __name__ == "__main__":
    file_path = "file:///path/to/your/document.odt"
    read_writer_document(file_path)