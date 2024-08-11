from setuptools import setup, find_packages

setup(
    name='four_in_a_row',
    version='0.1',
    packages=['app', 'tests'],
    url='',
    license='MIT License',
    author='Emanuel Garcia Rios, Miguel Angel Salas Montoya, Andrea Carolina Romero',
    author_email='emanuelgarciarios@gmail.com',
    description='Proyect  of business process',

    install_requires=[
        '###'
    ],
    entry_points='''
        [console_scripts]
        calc=app.calculator:calc
    '''
)