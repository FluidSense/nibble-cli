from setuptools import setup

setup(
    name='nibble-cli',
    version='0.1',
    py_modules=['nibble'],
    install_requires=[
        'Click',
        'requests'
        'Flask'
    ],
    entry_points='''
        [console_scripts]
        nibble=nibble:main
    ''',
)
