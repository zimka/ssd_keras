import os
from setuptools import setup


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ssd_keras',
    version='0.1',
    packages=['ssd_keras'],
    include_package_data=True,
    description='ssd_keras',
    url='https://github.com/zimka/ssd_keras',
    author='Pierluigi Ferrari',
    author_email='',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)