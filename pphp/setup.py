'''A spinoff of PHP in Python

See:
https://kenny2github.github.io/pphp
'''

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.txt'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="pphp",
    version='0.0.1',

    description='A spinoff of PHP in Python',
    long_description=long_description,

    url='https://kenny2github.github.io/pphp',

    author='Ken Hilton',
    author_email='kenny2minecraft@gmail.com',

    license='GNU',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',

        'Programming Language :: Python :: 2.7'
    ],
    keywords='php basehttpserver python',

    py_modules=['pphp'],

    install_requires=['lxml'],

    python_requires='<3'
)
