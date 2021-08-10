"""
from fpdf import FPDF

header = ("First name", "Other info")

data = (
    ("Jules", "Smith", "34", "San Juan"),
    ("Mary", "Ramos", "45", "Orlando"),
    ("Carlson", "Banks", "19", "Los Angeles"),
    ("Lucas", "Cimon", "31", "Saint-Mahturin-sur-Loire"),
)

pdf = FPDF()
pdf.add_page()
pdf.set_font("Times", size=10)
line_height = pdf.font_size * 2.5
col_width = pdf.epw / 4  # distribute content evenly

pdf.multi_cell(col_width, line_height, "First name", border=1, ln=3,
               max_line_height=pdf.font_size)
pdf.multi_cell(col_width, line_height, "Other info", border="LTB", ln=3,
               max_line_height=pdf.font_size)
for i in range(len(data) - 3):
    pdf.multi_cell(col_width, line_height, "", border="TB", ln=3,
                   max_line_height=pdf.font_size)
pdf.multi_cell(col_width, line_height, "", border="TBR", ln=3,
               max_line_height=pdf.font_size)

pdf.ln(line_height)

for row in data:
    for datum in row:
        pdf.multi_cell(col_width, line_height, datum, border=1, ln=3, max_line_height=pdf.font_size)
    pdf.ln(line_height)
pdf.output('table_with_cells.pdf')
"""

from bookfolder.pdf import PDFWriter
from bookfolder.sheet import Sheet

sheets = [Sheet(list(range(1, i*14+1, 14)), measurement_interval=0.25, page_number=i*2+1) for i in range(14)]

writer = PDFWriter(sheets)
writer.add_table_page(["page", "measure, mark, cut and fold at (cm)"])
writer.add_sheet_rows()
writer.save("tmp/pdf_test.pdf")
