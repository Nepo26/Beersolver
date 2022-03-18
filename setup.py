from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setup(
    name='beersolver',
    version='0.1.0',
    author="Henrique Nepomuceno",
    author_email="nepo26.hn@protonmail.com",
    packages=find_packages(),
    py_modules=['exercises/ThirdChapter/commands'],
    description="A script for solving vector mechanics Ferdinand P. Beer proposed exercises.",
    long_description=long_description,
    url="https://github.com/Nepo26/Beersolver",
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'beersolver=exercises.ThirdChapter.commands:cli',
        ],
    },
)
