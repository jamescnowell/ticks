from setuptools import setup, find_packages


setup(
    name='ticks',
    version='0.1.0',
    description='Command line stock ticker',
    packages=find_packages(),
    install_requires=['requests', 'tabulate'],
    entry_points={
        'console_scripts': [
            'ticks=ticks:main'
        ]
    }
)
