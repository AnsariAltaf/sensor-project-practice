'''
Sometimes when we have our code and we try to import it ,we get error "Module not found".
In order to avoid this,we have this file so that our sensor package can be utilized as a library.
Once it is available as a library we can share it or publish it.
'''

'''
find_packages will return a list of packages by searching the root directory.
'''

from setuptools import find_packages,setup

'''
def get_requirements():    
    requirements_list=[]
    with open('requirements.txt','r') as f:
        for line in f.readlines():
            if line!='\n' and line!='-e .':
                requirements_list.append(line.strip())
        return requirements_list
'''

setup(
    name= "sensor", 
    version= "0.0.1", 
    author= "ineuron", 
    author_email= "ansarialtaf23.aa@gmail.com",
    packages = find_packages(),
    install_requires=['pymongo==4.2.0'], #get_requirements() 
)