import os
from csv import writer
try:
	from pyresparser import ResumeParser
	dirc = 'cvs'
	for files in os.listdir(dirc):
		data = ResumeParser(dirc + '/' + files).get_extracted_data()
		with open('cvs.csv', 'a+', newline='') as write_obj:
			csv_writer = writer(write_obj)
			csv_writer.writerow([data['name'], data['mobile_number'], data['email']])
except Exception as ex:
	print(str(ex))
