import uno

def convert_writer_to_pdf(input_path, output_path):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    doc = desktop.loadComponentFromURL(input_path, "_blank", 0, ())
    doc.storeToURL(output_path, (uno.createUnoStruct('com.sun.star.beans.PropertyValue', 'FilterName', 0, 'writer_pdf_Export', 0),))
    doc.close(True)

if __name__ == "__main__":
    input_path = "file:///path/to/your/document.odt"
    output_path = "file:///path/to/your/document.pdf"
    convert_writer_to_pdf(input_path, output_path)