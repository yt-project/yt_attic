import os
from setuptools import setup
from setuptools import find_packages

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

dev_requirements = [
    'flake8', 'girder-client', 'gitpython',
    'sphinx', 'sphinx_bootstrap_theme']

setup(
    name = "yt_attic",
    version = "0.0.1",
    author = "The yt project",
    author_email = "yt-dev@lists.spacepope.org",
    description = ("The yt attic."),
    long_description = ("""Disused yt analysis modules."""),
    license = "BSD",
    keywords = ["simulation", "spectra", "astronomy", "astrophysics"],
    url = "http://yt-project.org/",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Scientific/Engineering :: Astronomy",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Visualization",
    ],
    install_requires=['yt', 'h5py', 'numpy', 'matplotlib'],
    extras_require = {
        'dev':  dev_requirements,
    },
)
