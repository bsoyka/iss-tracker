import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iss_tracker",
    version="2.0.0",
    author="Ben Soyka",
    author_email="bensoyka@icloud.com",
    description="A simple Tkinter GUI for tracking the International Space Station",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://github.com/bsoyka/iss-tracker",
    license="MIT",
    packages=["iss_tracker"],
    entry_points={"console_scripts": ["iss=iss_tracker:start"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["Pillow==7.2.0", "requests==2.24.0"],
)
