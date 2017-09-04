import py2exe
from distutils.core import setup
import matplotlib

setup(console = ["startGui.py"],
      options = { "py2exe":{"dll_excludes":["MSVCP90.dll"], "includes":["sip"]}},
      data_files = matplotlib.get_py2exe_datafiles()
      )