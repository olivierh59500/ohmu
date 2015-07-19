from setuptools import setup

setup(
    name='ohmu',
    version='0.1.0',
    author='Paul Nechifor',
    author_email='paul@nechifor.net',
    description='View space usage in your terminal.',
    py_modules=['ohmu'],
    keywords='space usage',
    long_description=open('readme.rst').read(),
    entry_points={'console_scripts': ['ohmu=ohmu:main']},
    license='MIT',
    url='http://github.com/paul-nechifor/ohmu',
    test_suite='nose.collector',
    tests_require=['nose'],
)
