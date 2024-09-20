import uno

def merge_writer_documents(input_paths, output_path):
    local_context = uno.getComponentContext()
    resolver = local_context.ServiceManager.createInstanceWithContext("com.sun.star.bridge.UnoUrlResolver", local_context)
    context = resolver.resolve("uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext")
    desktop = context.ServiceManager.createInstanceWithContext("com.sun.star.frame.Desktop", context)
    merged_doc = desktop.loadComponentFromURL("private:factory/swriter", "_blank", 0, ())

    for input_path in input_paths:
        doc = desktop.loadComponentFromURL(input_path, "_blank", 0, ())
        text = doc.Text
        cursor = text.createTextCursor()
        cursor.gotoEnd(False)
        text.insertControlCharacter(cursor, uno.getConstantByName("com.sun.star.text.ControlCharacter.PARAGRAPH_BREAK"), False)
        merged_doc.Text.insertDocumentFromURL(input_path, ())
        doc.close(True)

    merged_doc.storeToURL(output_path, ())
    merged_doc.close(True)

if __name__ == "__main__":
    input_paths = ["file:///path/to/your/document1.odt", "file:///path/to/your/document2.odt"]
    output_path = "file:///path/to/your/merged_document.odt"
    merge_writer_documents(input_paths, output_path)