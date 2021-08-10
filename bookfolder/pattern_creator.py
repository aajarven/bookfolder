"""
Tool for extracting a bookfolding pattern from an image.
"""


class PatternCreator():
    """
    A tool for creating a bookfolding pattern from an image.

    The image must be black and white, with each horizontal pixel in the image
    corresponding to one sheet of paper in the book and each vertical pixel
    corresponding to one "page coordinate unit", i.e. the accuracy of the
    measurement tool used in the folding process.
    """

    def __init__(self, input_path, measurement_interval=0.25):
        """
        Initiate the PatternCreator.

        :input_path: Location of the input file containing the pattern image.
        :measurement_interval: Length of one page coordinate unit in
                               millimeters. Defaults to 0.25 mm.
        """
        self.input_path = input_path
        self.measurement_interval = measurement_interval
        self.pages = []
