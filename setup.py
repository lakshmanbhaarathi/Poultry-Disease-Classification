from setuptools import setup,find_packages

with open (file="README.md", mode="r", encoding="utf-8") as f:
    log_description = f.read()


__version__ = "0.0.0.0"

REPO_NAME = "Poultry-Disease-Classification"
AUTHOR_USER_NAME = "lakshmanbhaarathi"
SRC_REPO = "PoultryDiseaseClassfier"
AUTHOR_EMAIL = "lakshmanbhaarathi@gmail.com"


setup(
    name=SRC_REPO
    , version=__version__
    , author=AUTHOR_USER_NAME
    , author_email=AUTHOR_EMAIL
    , description="An ML package to detect disease in poultry"
    , long_description=log_description
    , long_description_content = "text/markdown"
    , url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    , project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}"
    }
    , package_dir = {"":"src"}
    , packages=find_packages(where="src")
)