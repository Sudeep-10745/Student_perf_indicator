from setuptools import setup,find_packages

def get_requirements(file_path):
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n', '') for req in requirements]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='Student_perf_prediction',
    version='0.0.1',
    author='Sudeep',
    author_email='sudeepwarrier4321@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    
)