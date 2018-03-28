from setuptools import setup

setup(
    name='color-changer',
    version='1.0.4',
    packages=['colorchanger', ],
    license='MIT',
    description='Reads in an image and swap specified colors ',
    long_description=open('README.rst').read(),
    author='Florian Dahlitz',
    author_email='f2dahlitz@freenet.de',
    url='https://github.com/DahlitzFlorian/python-color-changer',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='color changer color-changer opencv numpy',
    install_requires=[
        'click',
        'numpy'
    ],
)