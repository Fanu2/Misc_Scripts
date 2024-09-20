import uno

def add_image_to_writer_document(file_path, image_path):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    doc = desktop.loadComponentFromURL(file_path, "_blank", 0, ())
    text = doc.Text
    cursor = text.createTextCursor()
    text.insertDocumentFromURL(image_path, cursor)
    doc.store()
    doc.close(True)

if __name__ == "__main__":
    file_path = "file:///path/to/your/document.odt"
    image_path = "file:///path/to/your/image.jpg"
    add_image_to_writer_document(file_path, image_path)