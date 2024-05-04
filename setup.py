import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
            name='nbb_api',
            version='0.1.6',
            description='Python package for easy access to Brazilian basketball data: NBB (Novo Basquete Brasil), Liga Ouro and LDB',
            long_description=long_description,
            long_description_content_type="text/markdown",
            url='https://github.com/GabrielPastorello/nbb_api',
            author='Gabriel Speranza Pastorello',
            author_email='gabriel.pastorello01@gmail.com',
            license='MIT',
            packages=setuptools.find_packages(),
            keywords=['nbb','novo basquete brasil','scraper','basketball',
                      'international basketball','brazil','ldb','liga-ouro'],
            python_requires=">=3.6",
            install_requires=['pandas>=1.5.3',
                              'numpy>=1.24.1',
                              'python-dateutil>=2.8.2',
                              'pytz>=2022.7',
                              'lxml>=4.9.2'
                              ],
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
)
