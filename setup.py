from setuptools import setup

setup(
    name='ct',
    version='0.1',
    py_modules=['ct'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        ct=ct:cli
    ''',
)