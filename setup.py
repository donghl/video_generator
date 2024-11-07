from setuptools import setup, find_namespace_packages

setup(
    name="python-workspace",
    version="0.1.0",
    packages=find_namespace_packages(include=['projects.*', 'external_app.*']),
    install_requires=[
        "toml",
        "pandas",
        "requests"
    ],
) 