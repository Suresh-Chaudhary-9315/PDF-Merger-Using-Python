from glob import glob
from pikepdf import Pdf
new_pdf = Pdf.new()
for pdf in glob("*.pdf"):
    with Pdf.open(pdf) as existing_pdf:
        new_pdf.pages.extend(existing_pdf.pages)
new_pdf.save("merged.pdf")