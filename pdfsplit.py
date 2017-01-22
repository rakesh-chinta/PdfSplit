import PyPDF2

def PDFsplit(pdf, splits):
	pdfFileObj = open(pdf, 'rb')

	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	start = 0
	end = splits[0]

	for i in range(len(splits)+1):
		pdfWriter = PyPDF2.PdfFileWriter()

		outputpdf = pdf.split('.pdf')[0]+str(i)+'.pdf'

		for page in range(start,end):
			pdfWriter.addPage(pdfReader.getPage(page))

		with open(outputpdf, 'wb') as f:
			pdfWriter.write(f)

		start = end
		try:
			end = splits[i+1]
		except IndexError:
			end = pdfReader.numPages


	pdfFileObj.close()
def main():

	pdf = 'example.pdf'
	splits = [2,4]
	PDFsplit(pdf,splits)

if __name__ =="__main__":
	main()  

