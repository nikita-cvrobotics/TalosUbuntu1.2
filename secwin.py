import frmbase
from Tkinter import *
import subprocess
import os

class secFrm(frmbase.frmbase):
	def regenFrm(self):
                self.flagCount = 0
<<<<<<< HEAD
		textOut = "RDesktop, inf, secpols, DEP, IESecZones not checked."
=======
		textOut = "Firewall, Updates, RDesktop, inf not checked."
>>>>>>> origin/Windows-usrgrp
		Label(self.frame, text=textOut).pack()
		
