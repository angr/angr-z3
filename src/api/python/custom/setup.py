from setuptools import setup

setup(
    name='angr-only-z3-custom',
    version='9002',
    description='installation stub for z3-solver',
    long_description="We don't need to host a custom z3 installer anymore! This package now just redirects to the official package.",
    maintainer="Andrew Dutcher",
    maintainer_email="andrew@andrewdutcher.com",
    url='https://github.com/angr/angr-z3',
    license='MIT License',
    packages=[],
    install_requires=['z3-solver']
)
