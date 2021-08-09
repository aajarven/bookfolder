"""
Representation of a sheet of paper in a book.
"""


class Sheet():
    """
    A sheet of book in a bookfolding sculpture.

    The locations of the folds are internally handled in "page coordinates",
    the separation of which is determined by `measurement_interval`.
    """

    def __init__(self, fold_locations, measurement_interval=0.25):
        """
        Create a new bookfolding sheet.

        :fold_locations: Locations of the folds on this page shown on page
                         coordinates.
        :measurement_interval: Length of a page coordinate unit in millimeters.
                               Default is 0.25 mm.
        """
        self.folds = fold_locations.copy()
        self.folds.sort()
