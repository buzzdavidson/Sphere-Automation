from setuptools import setup, find_packages

setup(
    name = "sphere-automation",
    version = "0.1.0",
    url = 'http://github.com/buzzdavidson/Sphere-Automation',
    license = 'GPL',
    description = "Open Home Automation for Linux",
    author = 'Steve Davidson',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)
