import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mockbrython", # Replace with your own username
    version="0.0.1",
    author="Bill Pringle",
    author_email="bllprngl@gmail.com",
    description="Mock brython functions for local testing and debugging.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wapringle/mockbrython",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
)
