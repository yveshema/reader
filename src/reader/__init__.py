# __init__.py

from importlib import resources
# `importlib.resources` is used to import non-code or resource files
# from a package without having to figure out their full file paths.
# This is especially helpful when you publish your package to PyPi
# and don't have full control over where your package is installed
# and how it's used. Resource files might even end up inside zip archives.


try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib 

# Version of the realpython-reader package
__version__ = "1.0.0"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("reader", "config.toml"))
URL = _cfg["feed"]["url"]