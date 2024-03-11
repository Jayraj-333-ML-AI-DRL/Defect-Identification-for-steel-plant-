
from setuptools import find_packages, setup
# Import necessary modules from setuptools
import os 

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "Defect-Identification-for-steel-plant-Public"
AUTHOR_USER_NAME = "Jayraj"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "jayrajput1997@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)