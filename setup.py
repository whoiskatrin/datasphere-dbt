# setup.py

from setuptools import setup, find_packages

setup(
    name="dbt-datasphere-plugin",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "dbt",
        "soda-sql",
        "great_expectations",
        "data_diff",
        "elementary",
    ],
    entry_points={},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
