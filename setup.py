from setuptools import setup, find_packages

setup(
    name='gtr_trainer',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'rich',
        'click'
    ],
    entry_points={
        'console_scripts': [
            'gtr-trainer=gtr_trainer.cli:main'
        ]
    },
)