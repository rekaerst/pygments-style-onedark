#!/usr/bin/python

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pygments-style-onedark",
    version="0.1.1",
    description="A Pygments style inspired by atom one dark theme.",
    long_description=long_description,
    keywords="pygments style",
    license="MIT",
    author="rekaerst",
    author_email="rekaerst@outlook.com",
    url="https://github.com/rekaerst/pygments-style-onedark",
    packages=find_packages(),
    install_requires=["pygments >= 2.2"],
    entry_points="""[pygments.styles]
                    onedark=pygments_style_onedark:OneDarkStyle""",
)
