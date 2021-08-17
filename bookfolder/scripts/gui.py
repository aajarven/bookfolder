"""
Graphical user interface for bookfolder
"""
import tkinter
from tkinter import filedialog
from tkinter import ttk
from tkinter import N, E, S, W


class GUI():
    """
    Graphical user interface for bookfolder
    """

    def __init__(self):
        self.image_path = ""

    def show(self):
        """
        Show the GUI to the user
        """
        window = tkinter.Tk()
        window.grid_columnconfigure(0, weight=1)

        image_io = ImageInput(window)
        image_io.create().grid(row=0, column=0)

        pdf_io = PDFOutput(window)
        pdf_io.create().grid(row=1, column=0)

        window.mainloop()


class FileIOFrame():
    """
    Create a frame for selecting a file for input/output.
    """

    label_text = ""
    button_text = "Browse"

    def __init__(self, parent_window):
        self.frame = ttk.Frame(parent_window)
        self.frame.grid(column=0, row=0, sticky=(N, E, S, W))

        self.path = tkinter.StringVar()

    def create(self):
        """
        Create the Frame and its components.

        :returns: the created Frame
        """

        label = tkinter.Label(self.frame, text=self.label_text)
        label.grid(column=0, row=0, sticky=(W, E))

        image_textbox = ttk.Entry(self.frame, textvariable=self.path)
        image_textbox.grid(column=1, row=0, sticky=(E, W))

        btn_browse = ttk.Button(self.frame, text=self.button_text,
                                command=self._browse_files)
        btn_browse.grid(column=2, row=0, sticky=(W))

        self.frame.columnconfigure(1, weight=1)

        return self.frame

    def _browse_files(self):
        raise NotImplementedError("Must be implemented in subclasses")


class ImageInput(FileIOFrame):
    """
    Create a Frame for selecting source image for the pattern
    """

    label_text = "Source image"

    def _browse_files(self):
        filename = filedialog.askopenfilename(
            title="Select a File",
            filetypes=(
                ("Image files", "*.png"),
                ("all files", "*.*"),
                ),
            )

        self.path.set(filename)


class PDFOutput(FileIOFrame):
    """
    Create a Frame for selecting PDF output location
    """

    label_text = "Save as"

    def _browse_files(self):
        filename = filedialog.asksaveasfilename(
            title="Save as",
            filetypes=(
                ("PDF files", "*.pdf"),
                ("all files", "*.*"),
                ),
            )

        self.path.set(filename)


if __name__ == "__main__":
    gui = GUI()
    gui.show()
