import csv

# Read CSV
path = '/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/example.csv'
data = open(path, encoding="utf-8")
csv_data =csv.reader(data)
data_lines = list(csv_data)
# print(data_lines)

ten_data = data_lines[1:11]
# print(ten_data)
for data in ten_data:
    print(data[3])

# Write CSV
file_to_output = open('/home/osustam/Udemy-Complete-Python-3-Bootcamp/17 - Working with PDFs and CSV Files/to_save_file.csv','w',newline='')
csv_writer = csv.writer(file_to_output, delimiter=',')
csv_writer.writerow(['a','b','c'])
file_to_output.close()