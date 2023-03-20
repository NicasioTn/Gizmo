from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.pdfgen import canvas

pdf = canvas.Canvas('example1.pdf', pagesize=letter)

# Add a colored rectangle to the PDF
pdf.setFillColor(HexColor('#ff0000'))
pdf.rect(0, 0, 100, 100, fill=True)

# Add some text to the PDF
pdf.setFont('Helvetica', 14)
pdf.drawString(110, 50, 'Hello, World!')

pdf.save()
import os
import smtplib
from PyPDF2 import PdfFileMerger

# Merge two PDF files into one
merger = PdfFileMerger()
merger.append(open('example1.pdf', 'rb'))
merger.append(open('example2.pdf', 'rb'))
merger.write('merged.pdf')

# Send the PDF file as an attachment in an email
sender_email = "63011212069@msu.ac.th"
receiver_email = "63011212098@msu.ac.th"
password = "Tk!130613"

message = "example.pdf"

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()

# Delete the merged PDF file
os.remove('merged.pdf')