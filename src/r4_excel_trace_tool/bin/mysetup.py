import py2exe
from distutils.core import setup

setup(console = ["csv2excel.py"],
      options = { "py2exe":{"dll_excludes":["MSVCP90.dll"]}},
      )