"""Package setup."""
from setuptools import find_packages, setup

name = 'farmzone-web-application'

setup(
    name=name,
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="A marketplace and forum for farmers",
    long_description=open('README.md').read(),
    url="https://github.com/BuildForSDG/Farmzone/",
    author="team-168",
    install_requires=[
        'appdirs==1.4.4',
        "asgiref==3.2.7",
        "astroid==2.4.1",
        "attrs==19.3.0",
        "backcall==0.1.0",
        "decorator==4.4.2",
        'distlib==0.3.0',
        'dj-database-url==0.5.0',
        'Django==3.1.12',
        'djangorestframework==3.11.0',
        'docutils==0.16',
        'filelock==3.0.12',
        'importlib-metadata==1.6.0',
        'ipython==7.14.0',
        'ipython-genutils==0.2.0',
        'isort==4.3.21',
        'jedi==0.17.0',
        'lazy-object-proxy==1.4.3',
        'mccabe==0.6.1',
        'more-itertools==8.2.0',
        'packaging==20.3',
        'parso==0.7.0',
        'pexpect==4.8.0',
        'pickleshare==0.7.5',
        'pluggy==0.13.1',
        'prompt-toolkit==3.0.5',
        'psycopg2==2.8.5',
        'ptyprocess==0.6.0',
        'py==1.8.1',
        'Pygments==2.6.1',
        'pylint==2.5.2',
        'pyparsing==2.4.7',
        'pytest==5.4.2',
        'pytz==2020.1',
        'rstcheck==3.3.1',
        'six==1.14.0',
        'sqlparse==0.3.1',
        'toml==0.10.0',
        'tox==3.15.0',
        'traitlets==4.3.3',
        'typed-ast==1.4.1',
        'virtualenv==20.0.20',
        'wcwidth==0.1.9',
        'wrapt==1.12.1',
        'zipp==3.1.0',
    ],
    include_package_data=True
)
