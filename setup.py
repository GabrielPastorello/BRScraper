import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
            name='BRScraper',
            version='0.1.0',
            description='Python module for Basketball Reference scraping and easy access to basketball data',
            long_description=long_description,
            long_description_content_type="text/markdown",
            url='https://github.com/GabrielPastorello/BRScraper',
            author='Gabriel Speranza Pastorello',
            author_email='gabriel.pastorello01@gmail.com',
            license='MIT',
            packages=setuptools.find_packages(),
            keywords=['basketball reference','scraper','nba','wnba',
                      'gleague','basketball','international basketball'],
            python_requires=">=3.6",
            install_requires=['pandas==2.0.3',
                              'numpy==1.24.4',
                              'python-dateutil==2.8.2',
                              'pytz==2023.3'
                              ],
            classifiers=[
                "Programming Language :: Python :: 3",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
            ],
)
