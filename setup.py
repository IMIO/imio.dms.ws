from setuptools import setup, find_packages

version = '0.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='imio.dms.ws',
    version=version,
    description="",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords='',
    author='',
    author_email='',
    url='https://github.com/IMIO/imio.dms.ws',
    license='gpl',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['imio', 'imio.dms'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
    ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
    # -*- Entry points: -*-
    """,
)
