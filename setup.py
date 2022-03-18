from setuptools import setup, find_packages

setup(
    name='beersolver',
    version='0.1.0',
    author="Henrique Nepomuceno",
    author_email="nepo26.hn@protonmail.com",
    packages=find_packages(),
    py_modules=['exercises/ThirdChapter/commands'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'beersolver=exercises.ThirdChapter.commands:cli',
        ],
    },
)
