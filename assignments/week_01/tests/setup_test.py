import pandas
import nose
import git
import statsmodels
import sklearn

from functools import partial
from distutils.version import LooseVersion


def check_version(package, version):
    return LooseVersion(package.__version__) >= LooseVersion(version)


def test_versions():

    version_dict = {
        nose: "1.3.0",
        git: "2.1.0",
        pandas: "0.23.0",
        sklearn: "0.2.0",
        statsmodels: "0.9.0",
    }

    for package, version in version_dict.items():
        f = partial(check_version, package, version)
        f.description = f"Package {package.__name__} version >= {version}"
        yield f,
