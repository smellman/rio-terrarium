"""rio-terrarium: setup."""

from setuptools import setup, find_packages

# Parse the version from the fiona module.
with open("rio_terrarium/__init__.py") as f:
    for line in f:
        if line.find("__version__") >= 0:
            version = line.split("=")[1].strip()
            version = version.strip('"')
            version = version.strip("'")
            break

long_description = """"""

# Runtime requirements.
inst_reqs = ["click", "rasterio~=1.0", "rio-mucho", "Pillow", "mercantile"]

extra_reqs = {
    "test": ["pytest", "pytest-cov", "codecov", "hypothesis", "raster_tester"],
    "dev": [
        "pytest", "pytest-cov", "codecov", "hypothesis", "raster_tester", "pre-commit"
    ],
}

setup(name="rio-terrarium",
      version=version,
      description=u"Encode arbitrary bit depth rasters in pseudo base-256 as RGB",
      long_description=long_description,
      classifiers=[],
      keywords="",
      author=u"Taro Matsuzawa",
      author_email="btm@tech.email.ne.jp",
      url="https://github.com/smellman/rio-terrarium",
      license="BSD",
      packages=find_packages(exclude=["ez_setup", "examples", "tests"]),
      include_package_data=True,
      zip_safe=False,
      install_requires=inst_reqs,
      extras_require=extra_reqs,
      entry_points="""
      [rasterio.rio_plugins]
      terrarium=rio_terrarium.scripts.cli:terrarium
      """)
