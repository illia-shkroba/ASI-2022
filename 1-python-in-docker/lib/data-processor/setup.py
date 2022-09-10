from setuptools import find_packages, setup

setup(
    name="data-processor",
    version="0.0.1",
    install_requires=["pandas>=1.4.1"],
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/my-github-page",
    author="Author Name",
    description="ASI Data Processor",
)
