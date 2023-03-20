import PyPDF2 
from fpdf import FPDF
from PyPDF2 import PdfReader, PdfWriter

writer = PdfWriter()

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 20, txt="Welcome to Python PDF!", ln=1, align="C")
#pdf.output("./Files/note.pdf")
pdf.output("encrypted-pdf.pdf")


print(PyPDF2.__version__)