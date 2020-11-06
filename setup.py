import setuptools

__version__ = "0.0.1"

setuptools.setup(
    name="mangamon",
    version=__version__,
    description="Manga Downloader",
    long_description="Command line program to download mangas from mangapanda",
    url="",
    author="akhil maskeri",
    author_email="akhil.maskeri@gmail.com",
    license="GPLv3",
    packages=["mangamon"],
    entry_points={
        'console_scripts': ["mangamon=mangamon.command_line:main"]
    },
    classifiers=[
        'Programming Language :: Python',   
        'License :: Public Domain',
        'Environment :: Console',
    ]
)