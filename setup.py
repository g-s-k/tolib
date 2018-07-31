from setuptools import setup, find_packages

setup(
    name = 'tolib',
    version = '0.1.0',
    description = 'batch tag and organize music files',
    author = 'George Kaplan',
    author_email = 'george@georgekaplan.xyz',
    url = 'https://github.com/g-s-k/tolib',
    packages = find_packages(),
    scripts = ['bin/tolib'],
    install_requires = [
        'mutagen==1.41.0',
        'Pillow==5.3.0'
    ]
)
