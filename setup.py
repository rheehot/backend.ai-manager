from setuptools import setup
from pathlib import Path
import re

here = Path(__file__).resolve().parent


def _get_version():
    root_src = (here / 'sorna' / 'manager' / '__init__.py').read_text()
    try:
        version = re.findall(r"^__version__ = '([^']+)'\r?$", root_src, re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine myself version.')
    return version


setup(
    name='sorna-manager',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=get_version(),
    description='Sorna Manager',
    long_description='',
    url='https://github.com/lablup/sorna-manager',
    author='Lablup Inc.',
    author_email='joongi@lablup.com',
    license='LGPLv3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Operating System :: POSIX',
        'Operating System :: MacOS :: MacOS X',
        'Environment :: No Input/Output (Daemon)',
        'Topic :: Scientific/Engineering',
        'Topic :: Software Development',
    ],

    packages=['sorna.manager', 'sorna.gateway', 'sorna.monitor'],
    namespace_packages=['sorna'],

    install_requires=['ConfigArgParse', 'namedlist', 'coloredlogs',
                      'pyzmq', 'aiozmq', 'aiohttp', 'aioredis', 'asyncpg',
                      'python-dateutil', 'simplejson', 'uvloop'],
    extras_require={
        'dev': [],
        'test': ['pytest', 'pytest-mock'],
    },
    data_files=[],
)
