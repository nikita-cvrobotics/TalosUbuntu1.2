import frmbase
from Tkinter import *
import subprocess
import os
import platform
import fwin

class gpoFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def fixAll(self):
                fwin.setGPOs(["domain", "computer", "user", "bitlocker"])
                fwin.installEMET()
                fwin.setGPOs(["stig"])
                self.reloadFrm()
	def regenFrm(self):
                self.flagCount = 0
                Label(self.frame, text="Operating System:").grid(row=1, column=0, sticky=W)
		#check for OS
		ver = platform.version()
		if ver.startswith("6.1"):
                        gpoList = fwin.getGPOs(fwin.WIN_7)
                        Label(self.frame, text="Windows 7 (Windows " + ver + ")", font="Arial 12 bold").grid(row=1, column=1)
                        dsec = gpoList["domain"]
                        #check GPO log and obscure test setting
                        Label(self.frame, text="Domain Security GPO applied? ").grid(row=2, column=0, sticky=W)
                        if dsec:
                                Label(self.frame, text="Yes", fg="green").grid(row=2, column=0, sticky=W)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=2, column=1, sticky=W)
                                Button(self.frame, text="Apply GPO", command=lambda: (fwin.setGPOs(["domain"]), self.reloadFrm())).grid(row=2, column=2, sticky=W)
                                Button(self.frame, text="Check Log", command=lambda: (fwin.openLog("domain"), self.reloadFrm())).grid(row=2, column=3, sticky=W)
                        csec = gpoList["computer"]
                        #check GPO log
                        Label(self.frame, text="Computer Security GPO applied? ").grid(row=3, column=0, sticky=W)
                        if csec:
                                Label(self.frame, text="Yes", fg="green").grid(row=3, column=0, sticky=W)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=3, column=1, sticky=W)
                                Button(self.frame, text="Apply GPO", command=lambda: (fwin.setGPOs(["computer"]), self.reloadFrm())).grid(row=3, column=2, sticky=W)
                                Button(self.frame, text="Check Log", command=lambda: (fwin.openLog("computer"), self.reloadFrm())).grid(row=3, column=3, sticky=W)
                        usec = gpoList["user"]
                        #check GPO log
                        Label(self.frame, text="User Security GPO applied? ").grid(row=4, column=0, sticky=W)
                        if usec:
                                Label(self.frame, text="Yes", fg="green").grid(row=4, column=0, sticky=W)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=4, column=1, sticky=W)
                                Button(self.frame, text="Apply GPO", command=lambda: (fwin.setGPOs(["user"]), self.reloadFrm())).grid(row=4, column=2, sticky=W)
                                Button(self.frame, text="Check Log", command=lambda: (fwin.openLog("user"), self.reloadFrm())).grid(row=4, column=3, sticky=W)
                        bsec = gpoList["bitlocker"]
                        #check GPO log
                        Label(self.frame, text="Bitlocker Security GPO applied? ").grid(row=5, column=0, sticky=W)
                        if bsec:
                                Label(self.frame, text="Yes", fg="green").grid(row=5, column=0, sticky=W)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=5, column=1, sticky=W)
                                Button(self.frame, text="Apply GPO", command=lambda: (fwin.setGPOs(["bitlocker"]), self.reloadFrm())).grid(row=5, column=2, sticky=W)
                                Button(self.frame, text="Check Log", command=lambda: (fwin.openLog("bitlocker"), self.reloadFrm())).grid(row=5, column=3, sticky=W)
                        emet = fwin.isEMET()
                        #check emet
                        Label(self.frame, text="Domain Security GPO applied? ").grid(row=6, column=0, sticky=W)
                        if emet:
                                Label(self.frame, text="Yes", fg="green").grid(row=6, column=0, sticky=W)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=6, column=1, sticky=W)
                                Button(self.frame, text="Install EMET", command=lambda: (fwin.installEMET(), self.reloadFrm())).grid(row=6, column=2, sticky=W)
                        tsec = gpoList["stig"]
                        #chk log
                        Label(self.frame, text="STIG Security GPO applied? ").grid(row=7, column=0, sticky=W)
                        if tsec:
                                Label(self.frame, text="Yes", fg="green").grid(row=7, column=0, sticky=W)
                        else:
                                self.flagCount += 1
                                Label(self.frame, text="No", fg="red").grid(row=7, column=1, sticky=W)
                                Button(self.frame, text="Apply GPO", command=lambda: (fwin.setGPOs(["stig"]), self.reloadFrm())).grid(row=7, column=2, sticky=W)
                                Button(self.frame, text="Check Log", command=lambda: (fwin.openLog("stig"), self.reloadFrm())).grid(row=7, column=3, sticky=W)
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
                #issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Fix All", command=self.fixAll).grid(row=0, column=2)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=3)
