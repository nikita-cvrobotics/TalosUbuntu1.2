import frmbase
from Tkinter import *
import subprocess
import os

class secFrm(frmbase.frmbase):
	def regenFrm(self):
                self.flagCount = 0
		textOut = "Firewall, Updates, RDesktop, inf not checked."
		Label(self.frame, text=textOut).pack()
		
