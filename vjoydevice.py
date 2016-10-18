
from pyvjoy.constants import *
from pyvjoy.exceptions import *

import pyvjoy._sdk as _sdk

class VJoyDevice(object):
	"""Object-oriented API for a vJoy Device"""

	def __init__(self,rID=None,):
		"""Constructor"""

		self.rID=rID
		self._sdk=_sdk
		self._vj=self._sdk._vj


		try:
			_sdk.vJoyEnabled()
			#DriverMatch()
			_sdk.AcquireVJD(rID)

		#TODO FIXME
		except vJoyException:
			raise

	def SetButton(self,state,buttonID):
		self._sdk.SetBtn(state,self.rID,buttonID)

	def SetAxis(self,AxisValue,AxisID):
		self._sdk.SetAxis(AxisValue,self.rID,AxisID)



