from setuptools import setup,find_packages
from typing import List

project_name="House price prediction"
version="0.0.3"
author="hema"
desc="house price prediction project"
email="hemasrinivasulu.ds@gmail.com"

hyphen_e_dot="-e ."
filename="requirements.txt"
requirements=[]

def get_requirements(filepath:str)->List[str]:
    with open(filepath) as f:
        requirements=f.readlines()
        requirements=[i.replace("\n","") for i in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(name=project_name,
      version=version,
      author=author,
      description=desc,
      author_email=email,
      packages=find_packages(),
      install_requires=get_requirements(filename)
      )

