#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys
from setuptools import setup, find_packages

# ===== Helper to parse requirements =====
def parse_requirements(filename):
    """Read requirements lines, ignoring comments and empty lines."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()
    reqs = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        # If line uses #egg=…, keep the full URL (or transform as needed)
        # This preserves PEP 508 direct references.
        reqs.append(line)
    return reqs

# ===== Read long description from README =====
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            return f.read()
    return "Pupy C2 – cross‑platform remote administration and post‑exploitation tool."

# ===== Single source of version =====
# Option A: read from a file or module (recommended)
# Here we define it directly for simplicity, but you could import pupy.__version__
VERSION = "3.0.0"

# ===== Main setup =====
setup(
    name="pupy",
    version=VERSION,
    description=(
        "Pupy C2 is an opensource, cross‑platform (Windows, Linux, OSX, Android) "
        "remote administration and post‑exploitation tool in Python."
    ),
    long_description=read_readme(),
    long_description_content_type="text/markdown",  # since we read README.md
    author="n1nj4sec",
    author_email="contact@n1nj4.eu",
    url="https://github.com/n1nj4sec/pupy",
    license="LICENSE",  # or use license="GPLv3" etc.
    license_files=("LICENSE",),
    keywords=[
        "python",
        "pentest",
        "cybersecurity",
        "redteam",
        "C2",
        "command and control",
        "post-exploitation",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Security",
        "Topic :: System :: Networking",
    ],
    python_requires=">=3.7",  # adjust based on actual support
    packages=find_packages(where=".", include=["pupy*"], exclude=["tests*", "docs*"]),
    include_package_data=True,   # reads from MANIFEST.in
    package_data={
        "pupy": [
            "conf/**",
            "external/**",
            "packages/**",
            "library_patches_py3/**",
            "library_patches_py2/**",
        ],
    },
    entry_points={
        "console_scripts": [
            "pupysh = pupy.cli.pupysh:main",
        ],
    },
    install_requires=parse_requirements("requirements.txt"),
    # Optional: add extras_require for development or optional features
    extras_require={
        "dev": ["pytest", "black", "flake8", "mypy"],
    },
    zip_safe=False,  # because package uses data files and dynamic imports
)
