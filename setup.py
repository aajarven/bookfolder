from setuptools import setup, find_packages

setup(
    name="bookfolder",
    version="0.1",
    packages=find_packages(),
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
