from setuptools import setup, find_packages

setup(
    name='HydrogenWebsite',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'blinker==1.9.0',
        'click==8.1.8',
        'colorama==0.4.6',
        'Flask==3.1.0',
        'iniconfig==2.1.0',
        'itsdangerous==2.2.0',
        'Jinja2==3.1.6',
        'MarkupSafe==3.0.2',
        'packaging==24.2',
        'pluggy==1.5.0',
        'pytest==8.3.5',
        'Werkzeug==3.1.3',
    ],
)
