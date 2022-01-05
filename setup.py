from pathlib import Path

from setuptools import setup, find_packages
from src.customHandlers import __version__

THIS_DIR = Path(__file__).parent

REQUIREMENTS_FILE = THIS_DIR.joinpath("requirements.txt")

install_requires = []
with open(REQUIREMENTS_FILE) as fh:
    for line in fh:
        install_requires.append(line.strip("\n"))

setup(
    name="customHandlers",
    version=__version__,
    author="Roy Assis",
    author_email="roya@cgen.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
    install_requires=install_requires,
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
