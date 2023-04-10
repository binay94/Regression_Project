from setuptools import find_packages,setup
from typing import List

hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path)as fp:
        requirements=fp.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)

        return requirements

setup(
name="Regressor Project",
version='0.0.1',
author='BINAYA',
author_email='binaya.vicky@gmail.com',
install_requires=get_requirements('requirements.txt'),
packages=find_packages()
)