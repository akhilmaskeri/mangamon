import setuptools

__version__ = "0.0.2"

setuptools.setup(
    name="mangamon",
    version=__version__,
    description="Manga Downloader",
    long_description="Command line program to download mangas from mangapanda",
    url="https://github.com/akhilmaskeri/mangamon",
    author="akhil maskeri",
    author_email="akhil.maskeri@gmail.com",
    license="GPLv3",
    packages=["mangamon"],
    entry_points={
        'console_scripts': ["mangamon=mangamon.command_line:main"]
    },
    classifiers=[
	    'Development Status :: 3 - Alpha',
        'Programming Language :: Python',   
        'License :: Public Domain',
        'Environment :: Console',
    ],
    python_requires=">=3",
    setup_requires=["wheel"],
    install_requires=[
        "argparse >= 1.4.0",
        "requests >= 2.24.0",
        "bs4 >= 0.0.1",
        "img2pdf >= 0.4.0",
        "tabulate >= 0.8.7"
    ]
)
