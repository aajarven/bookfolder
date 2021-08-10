"""
Module for writing the pattern into a PDF file.
"""

from fpdf import FPDF


class PDFWriter():
    """
    A tool that writes bookfolding Sheet data into a file.
    """

    data_columns = 14
    font = "Times"
    font_size = 10

    line_height = font_size * 1.0
    n_columns = 14

    def __init__(self, sheets):
        """
        Create a `PDFWriter`.

        :sheets: a list of Sheet objects depicting pages in the bookfolding
                 pattern.
        """
        self.sheets = sheets
        self.pdf = FPDF()
        self.pdf.set_font(self.font, size=self.font_size)
        self.column_width = self.pdf.epw / self.n_columns

    def add_table_page(self, header):
        """
        Add a new page to the document and add a table header to that page.

        :header: List of header fields.
        """
        self.pdf.add_page()

        if len(header) < self.n_columns:

            for i in range(len(header) - 1):
                self._add_cell(header[i], border=1)

            last_column_width = (
                    (self.n_columns - len(header) + 1) * self.column_width)
            self._add_cell(header[-1], width=last_column_width)

        elif len(header) == self.n_columns:
            for cell in header:
                self._add_cell(cell, border=1)

        else:
            raise ValueError("Header {} has too many fields: the page only "
                             "fits {} fields".format(header, self.n_columns))
        self._add_new_row()

    def add_sheet_rows(self):
        """
        Add a row for each sheet into the table.
        """
        for sheet in self.sheets:
            if len(sheet.folds) <= self.n_columns:
                self._add_single_row_sheet(sheet)
            else:
                raise ValueError("Very complicated sheets not supported (yet)")

    def _add_single_row_sheet(self, sheet):
        """
        Add a data row for a single Sheet
        """
        self._add_cell(sheet.page_number)
        for fold_point in sheet.fold_locations_in_cm():
            self._add_cell(fold_point)
        self._add_n_empty_cells(self.n_columns - len(sheet.folds) - 1)
        self._add_new_row()

    def _add_cell(self, content, border=1, width=None):
        """
        Add a table cell to the PDF.

        :content: Contents of the cell
        :border: Which borders to draw. 1 for all borders, 0 for none, or a
                 string containing a set of characters from L, R, T and B for
                 left, right, top and bottom borders respectively. Defaults to
                 1.
        :width: Width of the cell. Defaults to self.column_width.
        """
        if width is None:
            width = self.column_width

        self.pdf.multi_cell(
            width,
            self.line_height,
            str(content),
            border=border,
            ln=3,
            max_line_height=self.pdf.font_size
            )

    def _add_n_empty_cells(self, n_cells):
        """
        Add `n_cells` empty cells.
        """
        for _ in range(n_cells):
            self._add_cell("")

    def _add_new_row(self):
        """
        Add new row to the table
        """
        self.pdf.ln(self.line_height)

    def save(self, output_path):
        """
        Write the constructed PDF into a file.

        :output_path: the file in which the PDF file is saved.
        """
        self.pdf.output(output_path)
