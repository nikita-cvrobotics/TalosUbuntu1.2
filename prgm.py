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
			redprg = []
			ylwprg = []
			rflags = ""
			with open("redflags.txt", "r") as f:
				rflags = f.read().replace('\n', '')
			for i in hazards:
				if i in rflags:
					redprg.append(i)
				else:
					ylwprg.append(i)
			redfind = Listbox(self.frame, fg="red")
			for i in redprg:
				redfind.insert(END, str(i))
			ylwfind = Listbox(self.frame, fg="orange")
			for i in ylwprg:
				ylwfind.insert(END, str(i))
			keepBtn = Button(self.frame, text="Keep Program")
			Label(self.frame, text="Issues: " + str(len(ylwprg) + len(redprg)), fg="red", font="Arial 16 bold").grid(row=0, column=0, ipadx=10, ipady=5)
			Label(self.frame, text="Programs of Great Concern:").grid(row=1, column=0, ipadx=5, ipady=5)			
			redfind.grid(row=2, column=0)
			Label(self.frame, text="Programs to Also Remove:").grid(row=3, column=0, ipadx=5, ipady=5)			
			ylwfind.grid(row=4, column=0)
			destBtn = Button(self.frame, text="DESTROY PACKAGES")
			destBtn.grid(row=0, column=1)
			Label(self.frame, text="<Program name>").grid(row=1, column=1, ipadx=5, ipady=5)			
			keepBtn.grid(row=1, column=2)
			Label(self.frame, text="Dependencies:\nlol").grid(row=2, column=1, columnspan=2, ipadx=10, ipady=10, sticky=N)
			rfBtn = Button(self.frame, text="Refresh")
			rfBtn.grid(row=0, column=3, sticky=E)
			Label(self.frame, text="Programs to Keep:").grid(row=1, column=3, ipadx=5, ipady=5)			
			svprg = Listbox(self.frame, fg="green")
			#POPULATE SVPRG
			svprg.grid(row=2, column=3)
		else:
			pass
			#Label(self.frame, text=textOut).pack()
		
