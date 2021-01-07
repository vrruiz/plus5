import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plus5",
    version="0.1.1",
    author="Víctor R. Ruiz",
    author_email="rvr@linotipo.es",
    description="Python port of a subset of the Processing API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vrruiz/plus5",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
