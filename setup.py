from setuptools import find_packages,setup

def get_requirement(file_path:str):
    file_obj= open(file_path)
    requirements=[]
    for i in file_obj:
        i.replace('\n','')
        requirements.append(i)
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements  


setup(
    name='datascieneproject',
    version='0.0.1',
    author='saurav anand',
    author_email='anandsaurabh6789@gmail.com' ,
    packages=find_packages(),
    requires=get_requirement('requirements.txt')
)