from setuptools import setup

setup(
    name='nibble-cli',
    version='0.1',
    py_modules=['nibble', 'list_items', 'stage', 'auth'],
    install_requires=[
        'Click',
        'requests',
        'Flask',
        'Authlib'
    ],
    entry_points='''
        [console_scripts]
        nibble=nibble:main
    ''',
)
