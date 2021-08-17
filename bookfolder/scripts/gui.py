"""
Graphical user interface for bookfolder
"""
import tkinter
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from tkinter import N, E, S, W

from bookfolder.pattern_creator import PatternCreator


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

        image_input = ImageInput(window)
        pdf_output = PDFOutput(window)
        generate = GeneratePatternFrame(window, image_input.path,
                                        pdf_output.path)
        measurement_interval_input = MeasurementIntervalFrame(window)
        page_number_input = PageNumberFrame(window)

        self._add_components_vertically(
            [
                image_input.frame,
                pdf_output.frame,
                measurement_interval_input.frame,
                page_number_input.frame,
                generate.frame,
            ])

        window.mainloop()

    def _add_components_vertically(self, components):
        """
        Add given `components` to a grid on top of each other.
        """
        # pylint: disable=no-self-use
        for index, component in enumerate(components):
            component.grid(row=index, column=0)


class MeasurementIntervalFrame():
    """
    Return a Frame with text box for entering page number
    """

    def __init__(self, parent_window):
        self._frame = ttk.Frame(parent_window)
        self._frame.grid(column=0, row=0, sticky=(N, E, S, W))
        self.measurement_interval = tkinter.DoubleVar(value=0.25)

    @property
    def frame(self):
        """
        Generate the frame and the field within
        """
        label = tkinter.Label(
            self._frame,
            text="Height of one pixel in mm")
        label.grid(column=0, row=0, sticky=(W, E))

        measurement_interval_entry = ttk.Entry(
                self._frame,
                textvariable=self.measurement_interval)
        measurement_interval_entry.grid(column=1, row=0, sticky=(E, W))

        return self._frame


class PageNumberFrame():
    """
    Return a Frame with text box for entering page number
    """

    def __init__(self, parent_window):
        self._frame = ttk.Frame(parent_window)
        self._frame.grid(column=0, row=0, sticky=(N, E, S, W))
        self.first_page_number = tkinter.IntVar(value=1)

    @property
    def frame(self):
        """
        Generate the frame and the field within
        """
        label = tkinter.Label(
            self._frame,
            text="Page number of first pattern sheet in the pattern")
        label.grid(column=0, row=0, sticky=(W, E))

        page_number_entry = ttk.Entry(
                self._frame,
                textvariable=self.first_page_number)
        page_number_entry.grid(column=1, row=0, sticky=(E, W))

        return self._frame


class GeneratePatternFrame():
    """
    Return a Frame with button to generate the pattern.
    """

    def __init__(self, parent_window, input_path, output_path):
        self._frame = ttk.Frame(parent_window)
        self._frame.grid(column=0, row=0, sticky=(N, E, S, W))

        self.input_path = input_path
        self.output_path = output_path
        self.measurement_interval = tkinter.DoubleVar(value=0.25)

    @property
    def frame(self):
        """
        Create the Frame and the button within.
        """
        btn = ttk.Button(self._frame, text="Generate",
                         command=self._generate)
        btn.grid(column=1, row=0, sticky=(E))
        self._frame.columnconfigure(0, weight=1)

        return self._frame

    def _generate(self):
        """
        Generate the PDF pattern and confirm creation to the user.
        """
        pattern_creator = PatternCreator(self.input_path.get(),
                                         self.measurement_interval.get())
        pattern_creator.save_pdf(self.output_path.get())

        messagebox.showinfo(
            "Success",
            "Wrote the pattern to {}".format(self.output_path.get()))


class FileIOFrame():
    """
    Create a frame for selecting a file for input/output.
    """

    label_text = ""
    button_text = "Browse"

    def __init__(self, parent_window):
        self._frame = ttk.Frame(parent_window)
        self._frame.grid(column=0, row=0, sticky=(N, E, S, W))

        self.path = tkinter.StringVar()

    @property
    def frame(self):
        """
        Create the Frame and its components.

        :returns: the created Frame
        """

        label = tkinter.Label(self._frame, text=self.label_text)
        label.grid(column=0, row=0, sticky=(W, E))

        image_textbox = ttk.Entry(self._frame, textvariable=self.path)
        image_textbox.grid(column=1, row=0, sticky=(E, W))

        btn_browse = ttk.Button(self._frame, text=self.button_text,
                                command=self._browse_files)
        btn_browse.grid(column=2, row=0, sticky=(W))

        self._frame.columnconfigure(1, weight=1)

        return self._frame

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
