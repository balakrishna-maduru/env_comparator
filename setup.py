from setuptools import find_packages, setup
setup(
    name='env_comparator',
    packages=find_packages(include=['env_comparator']),
    version='0.0.1',
    description='Python environment comparator',
    author='Balakrishna Maduru',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)