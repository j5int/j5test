from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future import standard_library
standard_library.install_aliases()
from builtins import *
from setuptools import setup

setup(
    name='j5test',
    version='1.3',
    packages=['j5test'],
    license='Apache License, Version 2.0',
    description='Some testing utilities used by other j5 projects.',
    long_description=open('README.md').read(),
    url='http://www.sjsoft.com/',
    author='St James Software',
    author_email='support@sjsoft.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: Apache Software License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    install_requires = ["nose", "j5basic", "future"],
    extras_require = {
        'LoggingTest':  ["j5.Logging"],
        'IterativeTester-ThreadCleanup': ["j5.OS"],
        'BrowserDim': ['selenium'],
        }
)
