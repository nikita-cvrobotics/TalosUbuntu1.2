import frmbase
from Tkinter import *
import subprocess
import os
import platform
<<<<<<< HEAD
import fwin

class svcFrm(frmbase.frmbase):
        flagCount = 0
        ver = fwin.WIN_7
=======

class svcFrm(frmbase.frmbase):
        flagCount = 0
>>>>>>> origin/Windows-usrgrp
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
<<<<<<< HEAD
                        self.ver = fwin.WIN_7
                svcList = fwin.getServicesToFix()
                Label(self.frame, text="Services to disable:").grid(row=1, column=0, sticky=W)
                dlb = Listbox(self.frame, selectmode=EXTENDED, width=28, height=20, fg="red")
                for i in svcList["disable"]:
                        self.flagCount += 1
                        dlb.insert(END, i)
                dlb.grid(row=2, column=0, sticky=W)
                Button(self.frame, text="Fix", command=lambda: (fwin.setSvcs(fwin.LFW(dlb), "disable"), self.reloadFrm())).grid(row=2, column=1, sticky=N)
                
                Label(self.frame, text="Services to set manual:").grid(row=1, column=2, sticky=W)
                mlb = Listbox(self.frame, selectmode=EXTENDED, width=28, height=20, fg="red")
                for i in svcList["manual"]:
                        self.flagCount += 1
                        mlb.insert(END, i)
                mlb.grid(row=2, column=2, sticky=W)
                Button(self.frame, text="Fix", command=lambda: (fwin.setSvcs(fwin.LFW(mlb), "manual"), self.reloadFrm())).grid(row=2, column=3, sticky=N)
                
                Label(self.frame, text="Services to set auto:").grid(row=1, column=4, sticky=W)
                alb = Listbox(self.frame, selectmode=EXTENDED, width=28, height=20, fg="red")
                for i in svcList["auto"]:
                        self.flagCount += 1
                        alb.insert(END, i)
                alb.grid(row=2, column=4, sticky=W)
                Button(self.frame, text="Fix", command=lambda: (fwin.setSvcs(fwin.LFW(alb), "auto"), self.reloadFrm())).grid(row=2, column=5, sticky=N)
                
=======
                                        
                Label(self.frame, text="Services to disable:").grid(row=1, column=0, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=28, height=20).grid(row=2, column=0, sticky=W)
                Button(self.frame, text="Fix").grid(row=2, column=1, sticky=N)
                Label(self.frame, text="Services to set manual:").grid(row=1, column=2, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=28, height=20).grid(row=2, column=2, sticky=W)
                Button(self.frame, text="Fix").grid(row=2, column=3, sticky=N)
                Label(self.frame, text="Services to set auto:").grid(row=1, column=4, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=28, height=20).grid(row=2, column=4, sticky=W)
                Button(self.frame, text="Fix").grid(row=2, column=5, sticky=N)
>>>>>>> origin/Windows-usrgrp
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
<<<<<<< HEAD
                Button(self.frame, text="Apply .reg", command=lambda: (fwin.applyReg(self.ver), self.reloadFrm())).grid(row=0, column=2)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=5)
=======
                Button(self.frame, text="Apply .reg").grid(row=0, column=2)
>>>>>>> origin/Windows-usrgrp
		
