import py2exe
from distutils.core import setup

setup(console = ["cmdParse.py"],
      options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}},
      )