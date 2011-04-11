from setuptools import setup, find_packages

setup(
    name = "sphere-automation",
    version = "0.1.0",
    url = 'http://github.com/buzzdavidson/Sphere-Automation',
    license = 'GPL3',
    description = "Open Home Automation for Linux",
    long_description = read('README'),

    author = 'Steve Davidson',
    author_email = 'steve@sphereautomation.org',

    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],

    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Home Automation',
    ]
)
