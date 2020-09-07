# -*- encoding: utf-8 -*-
# Source: https://packaging.python.org/guides/distributing-packages-using-setuptools/

import io
import re

from setuptools import find_packages, setup


dev_requirements = [
    "bandit",
    "flake8",
    "isort",
    "pytest",
]
unit_test_requirements = [
    "pytest",
]
integration_test_requirements = [
    "pytest",
]
run_requirements = [
    "loguru==0.5.1",
    "uvicorn==0.11.5",
    "fastapi==0.58.0",
    "gunicorn==20.0.4",
    "pymongo==3.10.1",
    "scikit-learn==0.23.1 ",
]

with io.open("./classifiers_gym/__init__.py", encoding="utf8") as version_f:
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_f.read(), re.M)
    if version_match:
        version = version_match.group(1)
    else:
        raise RuntimeError("Unable to find version string.")

with io.open("README.md", encoding="utf8") as readme:
    long_description = readme.read()

setup(
    name="Classifiers Gym",
    version=version,
    author="Kevin Araujo",
    author_email="k.santanaraujo@gmail.com",
    packages=find_packages(exclude="tests"),
    include_package_data=True,
    url="https://github.com/kevinsantana/classifiers-gym",
    license="COPYRIGHT",
    description="",
    long_description=long_description,
    zip_safe=False,
    install_requires=run_requirements,
    extras_require={
         "dev": dev_requirements,
         "unit": unit_test_requirements,
         "integration": integration_test_requirements,
    },
    python_requires=">=3.8",
    classifiers=[
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.8"
    ],
    keywords=(),
    entry_points={
        "console_scripts": [
            "classifiers_gym = classifiers_gym.__main__:start"
        ],
    },
)
