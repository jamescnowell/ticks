from setuptools import setup, find_packages


setup(
    name='ticks',
    version='0.1.3',
    author='James Nowell',
    author_email='jnowell129@gmail.com',
    url='https://github.com/jamescnowell/ticks',
    license='WTFPL',
    description='Command line stock ticker',
    long_description='Command line stock ticker',    
    py_modules=['ticks'],
    install_requires=['requests', 'tabulate'],
    entry_points={
        'console_scripts': [
            'ticks=ticks:main'
        ]
    }
)
