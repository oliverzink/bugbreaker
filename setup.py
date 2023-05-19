import sys
from setuptools import setup

if sys.version_info[:3] < (3, 0, 0):
    print("Requires Python 3 to run.")
    sys.exit(1)

setup(
    name="bugbreaker",
    version="1.5.0",
    description="Terminal tool that explains program bugs",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Debuggers",
        "Natural Language :: English",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python"
    ],
    include_package_data=True,
    packages=["bugbreaker", "bugbreaker.utilities"],
    entry_points={"console_scripts": [
        "bugbreaker = bugbreaker.bugbreaker:main"]},
    install_requires=["revChatGPT", "pygments"],
    requires=["revChatGPT", "pygments"],
    python_requires=">=3",
)
