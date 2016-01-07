from setuptools import setup, find_packages


setup(
    name='ticks',
    version='0.1.1',
    author='James Nowell',
    author_email='jnowell129@gmail.com',
    url='https://github.com/jamescnowell/ticks',
    license='WTFPL',
    description='Command line stock ticker',
    long_description='Command line stock ticker',    
    packages=find_packages(),
    install_requires=['requests', 'tabulate'],
    entry_points={
        'console_scripts': [
            'ticks=ticks:main'
        ]
    }
)
