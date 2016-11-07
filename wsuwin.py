import frmbase
from Tkinter import *
import subprocess
import os
import platform
import fwin

class wsuFrm(frmbase.frmbase):
	flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def fixAll(self):
                fwin.fixUpdates()
                fwin.runWSUS()
                fwin.runSecunia()
                self.reloadFrm()
	def regenFrm(self):
                self.flagCount = 0
                Button(self.frame, text="Fix", command=self.fixAll).grid(row=0, column=2, ipadx=5)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=3, ipadx=5)
                Label(self.frame, text="Operating System:").grid(row=1, column=0, sticky=W)
                #check for OS
		ver = platform.version()
		if ver.startswith("6.1"):
                        Label(self.frame, text="Windows 7 (Windows " + ver + ")", font="Arial 12 bold").grid(row=1, column=1)
                        Label(self.frame, text="SP1 installed: ").grid(row=2, column=0, sticky=W)
                        sp1=fwin.getSPs(fwin.WIN_7)
                        if sp1[0] == True:
                                Label(self.frame, text="Yes", fg="green").grid(row=2, column=1)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=2, column=1)
                                Button(self.frame, text="Run SP1 installation", command=lambda: (fwin.installSP1(), self.reloadFrm())).grid(row=2, column=2)
                                Button(self.frame, text="Shamelessly lie to Windows about SP1 (do AFTER WSUS start)", command=lambda: (fwin.shamelessSP1spoofish(), self.reloadFrm())).grid(row=2, column=3)
                elif ver.startswith("WIN SERVER 2008 ID HERE"):
                        pass
                elif ver.startswith("WIN 8.1 ID HERE"):
                        pass
                elif ver.startswith("WIN 8 ID HERE"):
                        pass
                elif ver.startswith("WIN 10 ID HERE"):
                        pass
                elif ver.startswith("WIN SERVER 2016 ID HERE"):
                        pass
                else:
                        Label(self.frame, text="OS NOT RECOGNIZED", font="Arial 12 bold", fg="gray").grid(row=1, column=1)
                Label(self.frame, text="WSUS completed? ").grid(row=5, column=0, sticky=W)
                iswsus = fwin.getWSUS()
                if iswsus:
                        Label(self.frame, text="Yes", fg="green").grid(row=5, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=5, column=1)
                Button(self.frame, text="Run WSUS", command=lambda: (fwin.runWSUS(), self.reloadFrm())).grid(row=5, column=2)

                Label(self.frame, text="Secunia installed? ").grid(row=6, column=0, sticky=W)
                isSecunia = fwin.getSecunia()
                if isSecunia:
                        Label(self.frame, text="Yes", fg="green").grid(row=6, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=6, column=1)
                Button(self.frame, text="Install Secunia PSI", command=lambda: (fwin.runSecunia(), self.reloadFrm())).grid(row=6, column=2)

                autoupt = fwin.getUpdateSettings()
                Label(self.frame, text="Updates Installed Automatically? ").grid(row=7, column=0, sticky=W)
                if autoupt:
                        Label(self.frame, text="Yes", fg="green").grid(row=7, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=7, column=1)
                        Button(self.frame, text="Fix Updates", command=lambda: (fwin.fixUpdates(), self.reloadFrm())).grid(row=7, column=2)
                
		#Check flags
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W)

