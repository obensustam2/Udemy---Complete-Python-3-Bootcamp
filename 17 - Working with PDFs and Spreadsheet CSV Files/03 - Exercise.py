import csv
import re
import PyPDF2

# Read CSV
path = '/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/exercise/find_the_link.csv'
data = open(path, encoding="utf-8")
csv_data =csv.reader(data)
data_lines = list(csv_data)
address = ''

for i in range(len(data_lines)):
    address += data_lines[i][i]
print(address)


# Read PDF
path_read = '/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/exercise/Find_the_Phone_Number.pdf'
f = open(path_read,'rb')
pdf_reader = PyPDF2.PdfFileReader(f)
page_num = pdf_reader.numPages
pdf_text = ''

for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text += page.extractText()
print(pdf_text)


# Find Number
pattern = r'\d{3}.\d{3}.\d{4}'
if re.search(pattern, pdf_text):
    print(re.search(pattern, pdf_text).group())

