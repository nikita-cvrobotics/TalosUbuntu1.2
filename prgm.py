import frmbase
from Tkinter import *
import subprocess
import os

class prgmFrm(frmbase.frmbase):
	def findPrograms(self):
		result = []
		pkgList = subprocess.check_output('dpkg --get-selections | cut -f1', shell=True).splitlines()
		defPkgList = []
		with open("ub14pkgdef", "r") as f:
			for i in f.readlines():
				defPkgList.append(i[:-1])
		for i in pkgList:
			if i not in defPkgList:
				result.append(i)
		return result
	def regenFrm(self):
		hazards = self.findPrograms()
		textOut = "No packages to delete!"
		if len(hazards) > 0:
			textOut = ""
			for i in hazards:
				textOut += (i + "\n")
		Label(self.frame, text=textOut).pack()
		
