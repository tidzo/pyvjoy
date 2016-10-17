import os
import sys
from ctypes import *


dll_filename = "vJoyInterface.dll"
dll_path = os.path.dirname(__file__) + os.sep + dll_filename

try:
	_vj = cdll.LoadLibrary(dll_path)
except OSError:
	sys.exit("Unable to load vJoy SDK DLL.  Ensure that %s is present" % dll_filename)
	
	