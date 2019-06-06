from PIL import Image 
import pytesseract
from pdf2image import convert_from_path

PDF_file = "/home/savera/Python3/PyOCR_PDF/sample.pdf"

pages = convert_from_path(PDF_file, 100)

image_counter = 1

for page in pages:

    filename = "page_"+str(image_counter)+".jpg"
    
    page.save('/home/savera/Python3/PyOCR_PDF/'+filename, 'JPEG')

    image_counter = image_counter + 1


filelimit = image_counter-1

outfile = "/home/savera/Python3/PyOCR_PDF/sample.csv"

f = open(outfile, "a")

for i in range(1, filelimit + 1): 
  
    filename = "page_"+str(i)+".jpg"

    text = str(((pytesseract.image_to_string(Image.open('/home/savera/Python3/PyOCR_PDF/'+filename))))) 
  
    text = text.replace('-\n', '')     
  
    f.write(text)

f.close() 