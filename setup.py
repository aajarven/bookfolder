from setuptools import setup, find_packages

setup(
    name="bookfolder",
    version="0.1",
    author="Anni Järvenpää",
    description="Convert an image into a bookfolding pattern",
    url="https://github.com/aajarven/bookfolder",
    packages=find_packages(),
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        "click",
        "imageio",
    ],
    entry_points={
        "console_scripts": [
            "bookfolder-cli = bookfolder.scripts.cli:cli",
            "bookfolder = bookfolder.scripts.gui:start",
        ],
    },
)
