import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name='iss_tracker',
      version='1.0.0',
      description='A simple Tkinter GUI for tracking the International Space Station',
      url='http://github.com/bsoyka/iss-tracker',
      author='Benjamin Soyka',
      author_email='bensoyka@icloud.com',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages=setuptools.find_packages(),
      license='GPL-3.0',
      zip_safe=False)
