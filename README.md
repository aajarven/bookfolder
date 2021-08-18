# Create Your Own Bookfolding Patterns

This tool allows you to generate bookfolding patters from images.

Each color of pixels in the image must correspond to one fold depth in the
scuplture, with each horizontal pixel corresponding to one sheet of paper in
the book and each vertical pixel to one "measurement interval" along the edge
of the book.

If you use a traditional ruler, this measurement interval can be e.g. 1.0 mm,
corresponding to the spacing between the markings in the ruler, or if you feel
you can comfortably eyeball the midpoint between two markings, you can use 0.5
mm instead. For special tools, such as Incra rulers, the interval can be even
shorter.

If your pattern has less sheets than your book has pages, or the book you use
has pages without numbers, you can also set a custom start page for the
pattern, so that the first sheet in the pattern is e.g. page 5 or "page -3".


## Requirements

This software has been tested on Python 3.6, but will likely run on other
versions of Python 3 too. If you use the graphical user interface, you also
need to have `python3-tkinter` installed.


## Installation

1. Ensure you have [Python](https://www.python.org/downloads/) available on
   your system.
   - If you intend to use the graphical user interface, you also need  the
     `python3-tkinter` package
1. Download this tool either using `git clone` or the "Download ZIP" button
   found under the green "Code" menu. If you downloaded the tool as a zip,
   extract it.
1. Navigate to the directory to which you downloaded/extracted this tool.
1. Install the tool using pip:
    ```
    pip install .
    ```


## Usage

### Windowed mode

After installing, you can start the program with command `bookfolder`.

### Command-line use

See `bookfolder-cli --help` for information about available commands and their
invocation.


## License

This software is licensed under [GNU General Public License v3.0](LICENSE.md).
