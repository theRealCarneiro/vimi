import pathlib
from setuptools import setup

with open('vimi/settings.py') as f:
    for line in f:
        if line.startswith('__version__'):
            __version__ = line.replace("'", '').split()[2]
            break

VERSION = __version__
README = (pathlib.Path(__file__).parent / "README.md").read_text()

REQUIREMENTS = []

with open('requirements.txt') as file:
    for line in file:
        REQUIREMENTS.append(line.rstrip())

setup(
    name='vimi',
    version=VERSION,
    description='A virtual midi board',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Gabriel Carneiro',
    author_email='therealcarneiro@gmail.com',
    license="GPL",
    license_files='LICENSE',
    classifiers=[
        "Environment :: X11 Applications",
        "License :: OSI Approved :: MIT License",
    ],
    url='https://github.com/theRealCarneiro/vimi',
    packages=['vimi', 'vimi.ui', 'vimi.midi'],
    install_requires=REQUIREMENTS,
    # data_files=DATA_FILES,
    entry_points={
        "console_scripts": [
            "vimi = vimi.main:main",
        ],
    },

    python_requires=">=3.10",
    include_package_data=True
)
