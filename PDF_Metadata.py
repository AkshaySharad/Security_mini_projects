import os.path
from pypdf import PdfReader

filename = r'C:\Users\aksha\OneDrive\Desktop\Akshay\Resume\Security_codes\Account_Certificate.pdf'

pdffile = PdfReader(filename)
data = pdffile.metadata

print("Metadata of the file:")

for metadata in data:
    print(metadata+ ':' +data[metadata])



