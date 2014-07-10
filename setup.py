from setuptools import setup

setup(
    name='pushy',
    version='0.1',
    description=(''),
    keywords='pushy',
    url='https://github.com/calinf/pushy',
    include_package_data=True,
    install_requires = [
        'redis==2.9.1',
        'tornado==3.2.1',
        'requests==2.3.0'
    ],
    license='BSD License',
)
