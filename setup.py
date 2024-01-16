from setuptools import setup, find_packages

setup(
    name='book_manager',
    version='0.0.1',
    author='Michael Glössl',
    author_email='mgloessl04@gmail.com',
    url='https://github.com/MichaelGloessl04/book_manager',
    description='Import books and display them.',
    long_description=open('README.md').read(),

    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=[
        'pandas',
    ],
    extras_require={
        'dev': [
            'pytest',
        ],
    },
)