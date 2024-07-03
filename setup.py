from setuptools import setup

setup(
    name='occlab',
    version='0.0.2',
    install_requires=[
        'requests',
        'importlib-metadata; python_version<"3.10"',
    ],
)

setup(
    setup_requires=['wheel']
)

setup(
    # ...
    packages=['occ', 'wocemaps', 'spmap']
)
