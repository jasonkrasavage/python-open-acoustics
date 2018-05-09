from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyopenacoustics',
    version='1.0.0a2',
    description='A module executing acoustics calculations',
    long_description_content_type='text/markdown',
    url='https://github.com/jasonkrasavage/python-open-acoustics',
    author='Jason Krasavage',
    author_email='jason.krasavage@loop.colum.edu',
    classifiers=[  
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='acoustics audio sound environmentalacoustics ',
    py_modules=["pyopenacoustics"],
    install_requires=['numpy'],

   
)
