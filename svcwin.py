import frmbase
from Tkinter import *
import subprocess
import os
import platform

class svcFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
	def regenFrm(self):
                self.flagCount = 0

                Label(self.frame, text="Operating System:").grid(row=0, column=3, sticky=W)
                #check for OS
		ver = platform.version()
		if ver.startswith("6.1"):
                        Label(self.frame, text="Windows 7 (Windows " + ver + ")", font="Arial 12 bold").grid(row=0, column=4)
                                        
                Label(self.frame, text="Services to disable:").grid(row=1, column=0, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=28, height=20).grid(row=2, column=0, sticky=W)
                Button(self.frame, text="Fix").grid(row=2, column=1, sticky=N)
                Label(self.frame, text="Services to set manual:").grid(row=1, column=2, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=28, height=20).grid(row=2, column=2, sticky=W)
                Button(self.frame, text="Fix").grid(row=2, column=3, sticky=N)
                Label(self.frame, text="Services to set auto:").grid(row=1, column=4, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=28, height=20).grid(row=2, column=4, sticky=W)
                Button(self.frame, text="Fix").grid(row=2, column=5, sticky=N)
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Apply .reg").grid(row=0, column=2)
		
