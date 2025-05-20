#this file helps us in installing local packages in our environment
from setuptools import setup, find_packages 

setup(
    name="src",
    version="0.0.1",
    author="Vikash Das",
    author_email="vikashdas770@gmail.com",
    packages=find_packages() #will find package under that name "src"
)