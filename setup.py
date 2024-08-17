# to install dependencies locally in our virtual environment 
from setuptools import find_packages,setup

setup(
    name='mcqgenerator',
    version='0.0.1',
    author='abubakar',
    author_email='abubakkeramjad10@gmail.com',
    install_requires=["openai","langchain","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)
# responsible for finding the local packages hint: __init__.py => find_packages()