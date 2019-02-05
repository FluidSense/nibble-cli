from setuptools import setup

setup(
    name='nibble-cli',
    version='0.1',
    py_modules=['nibble'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        nibble=nibble:main
    ''',
)