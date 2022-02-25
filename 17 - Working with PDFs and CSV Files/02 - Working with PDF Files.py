import PyPDF2

# Read PDF
path_read = '/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/Working_Business_Proposal.pdf'
f = open(path_read,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page_num = pdf_reader.numPages
print(page_num)

page_four = pdf_reader.getPage(3)
page_four_text = page_four.extractText()
print(page_four_text)

# Write PDF
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(page_four)
path_write = '/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/Some_New_Doc.pdf'
pdf_output = open(path_write, 'wb')
pdf_writer.write(pdf_output)
f.close()


# List All Page Text
pdf_text = []
path_new = '/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/Working_Business_Proposal.pdf'
f = open(path_new,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())

print(pdf_text)