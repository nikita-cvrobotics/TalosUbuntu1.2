import frmbase
from Tkinter import *
import subprocess
import os
import fwin

class ftrFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def fixAll(self):
                blist = fwin.getFeatures()
                fwin.removeFeatures(blist["remove"])
                fwin.addFeatures(blist["install"])
                self.reloadFrm()
	def regenFrm(self):
                self.flagCount = 0
                ftrlist = fwin.getFeatures()
                Label(self.frame, text="Features to Remove:").grid(row=1, column=0, sticky=W)
                ftrrem = Listbox(self.frame, selectmode=EXTENDED, width=50, height=20, fg="green")
                for i in ftrlist["remove"]:
                        self.flagCount += 1
                        ftrrem.insert(END, i)
                ftrrem.grid(row=2, column=0, sticky=W)
                Button(self.frame, text="Remove", command=lambda: (fwin.removeFeatures(fwin.LFW(ftrrem)), self.reloadFrm())).grid(row=2, column=1, sticky=N)
                Label(self.frame, text="Features to Install:").grid(row=1, column=2, sticky=W)
                ftradd = Listbox(self.frame, selectmode=EXTENDED, width=50, height=20, fg="green")
                for i in ftrlist["install"]:
                        self.flagCount += 1
                        ftradd.insert(END, i)
                ftradd.grid(row=2, column=2, sticky=W)
                Button(self.frame, text="Install", command=lambda: (fwin.addFeatures(fwin.LFW(ftradd)), self.reloadFrm())).grid(row=2, column=3, sticky=N)
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Fix All", command=self.fixAll).grid(row=0, column=2)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=3)
		
