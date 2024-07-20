from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e.'

def get_requirements(file_path:str)->list:
    """
    This function will read the requirements file and return the list of requirements
    """
    
    requirements= []
    with open(file_path) as fileobj:
      requirements = fileobj.readlines()
      requirements = [req.replace('\n', ' ') for req in requirements]
      
      if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)
    
    return requirements






setup(
  name='ml_projet',
  version='0.0.1',
  author='Pratik',
  author_email='pratikrbokade05@gmail.com',
  packages=find_packages(),
  install_requires=get_requirements('requirements.txt'),
)
  