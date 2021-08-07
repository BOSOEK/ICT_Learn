import PyPDF2

if __name__ == "__main__":
    with open("example/recipe-book.pdf", "r+b") as f:  # b => binary
        reader = PyPDF2.PdfFileReader(f)
        # print(reader.numPages)
        # print(reader.getDocumentInfo)

        for page in range(0, reader.numPages):
            pageObj = reader.getPage(page)
            print("\n" + pageObj.extractText())
