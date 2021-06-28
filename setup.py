import io
from setuptools import setup, find_packages
from metriq import __version__

name = "metriq-client"
author = "Viktor Kerkez, UnitaryFund"
author_email = "alefnula@gmail.com, dan@unitary.fund, vincent@unitary.fund"
url = "https://github.com/unitaryfund/metriq-client"


setup(
    name=name,
    version=__version__,
    author=author,
    author_email=author_email,
    maintainer=author,
    maintainer_email=author_email,
    description="Python client for metriq API.",
    long_description=io.open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url=url,
    platforms=["Windows", "POSIX", "MacOSX"],
    license="Apache-2.0",
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        metriq=metriq.__main__:app
    """,
)
