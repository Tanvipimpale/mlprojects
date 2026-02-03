from setuptools import find_packages, setup  
from typing import List 
def get_requirements(file_path: str) -> list[str]:
'''this is function is used to return list of requirements'''
requirements=[]
with open (file_path) as file_obj:
    requirements=file_obj.readlines()
    requirements=[req.replace("\n","") for req in requirements]
       if HYPEN_E_DOT in requirements:
setup(
    name="mlproject",
    version='0.0.1',
    author="Tanvi Pimpale",
    author_email="tanvipimpale95@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')