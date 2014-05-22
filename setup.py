#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='blanc-basic-pages',
    version='0.2.1',
    description='Blanc Basic Pages for Django',
    long_description=open('README.rst').read(),
    url='http://www.blanctools.com/',
    maintainer='Alex Tomkins',
    maintainer_email='alex@hawkz.com',
    platforms=['any'],
    install_requires=[
        'django-mptt>=0.6.0',
        'django-mptt-admin==0.1.8',
    ],
    packages=[
        'blanc_basic_pages',
        'blanc_basic_pages.templatetags',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    license='BSD-2',
)
