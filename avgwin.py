import frmbase
from Tkinter import *
import subprocess
import os
import fwin

class avgFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
	def regenFrm(self):
                self.flagCount = 0
                scanList = fwin.getAVscans()
                avg = scanList["avg"]
                #check AV scan
                Label(self.frame, text="AVG Scanned? ").grid(row=1, column=0, sticky=W)
                if avg:
                        Label(self.frame, text="Yes", fg="green").grid(row=1, column=1)
                else:
                        Label(self.frame, text="No", fg="red").grid(row=1, column=1)
                        Button(self.frame, text="Install AVG", command=lambda: (fwin.installAVG(), self.reloadFrm())).grid(row=1, column=2)
                mwb = scanList["mwb"]
                #check AV scan
                Label(self.frame, text="MalwareBytes Scanned? ").grid(row=2, column=0, sticky=W)
                if mwb:
                        Label(self.frame, text="Yes", fg="green").grid(row=2, column=1)
                else:
                        Label(self.frame, text="No", fg="red").grid(row=2, column=1)
                        Button(self.frame, text="Install MalwareBytes", command=lambda: (fwin.installMWB(), self.reloadFrm())).grid(row=2, column=2)
                mse = scanList["mse"]
                #check AV scan
                Label(self.frame, text="Microsoft Security Essentials Scanned? ").grid(row=3, column=0, sticky=W)
                if mse:
                        Label(self.frame, text="Yes", fg="green").grid(row=3, column=1)
                else:
                        Label(self.frame, text="No", fg="red").grid(row=3, column=1)
                        Button(self.frame, text="Install MSE", command=lambda: (fwin.installMSE(), self.reloadFrm())).grid(row=3, column=2)
                wdf = scanList["wdf"]
                #check AV scan
                Label(self.frame, text="Windows Defender Scanned? ").grid(row=4, column=0, sticky=W)
                if wdf:
                        Label(self.frame, text="Yes", fg="green").grid(row=4, column=1)
                else:
                        Label(self.frame, text="No", fg="red").grid(row=4, column=1)
                        Button(self.frame, text="Install Windows Defender", command=lambda: (fwin.installWDF(), self.reloadFrm())).grid(row=4, column=2)
                if not avg and not mwb and not mse and not wdf:
                        self.flagCount += 1
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=2)
