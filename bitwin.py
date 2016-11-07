import frmbase
from Tkinter import *
import subprocess
import os
import fwin

class bitFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def fixAll(self):
                fwin.activateBitlocker()
                fwin.setGPOs(["bitlocker"])
                fwin.activateApplocker()
                self.reloadFrm()
	def regenFrm(self):
                self.flagCount = 0                
                Label(self.frame, text="Bitlocker enabled? ").grid(row=1, column=0)
                isbit=fwin.getBitlocker()
                #check Bitlocker
                if isbit:
                        Label(self.frame, text="Yes", fg="green").grid(row=1, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=1, column=1)
                        Button(self.frame, text="Enable", command=lambda: (fwin.activateBitlocker(), self.reloadFrm())).grid(row=1, column=2)
                Label(self.frame, text="( Bitlocker password is P@ssword1@3$5^ )").grid(row=2, column=0)
                Label(self.frame, text="Bitlocker GPO applied? ").grid(row=3, column=0)
                isbitgpo=fwin.getGPOs(fwin.WIN_7)["bitlocker"]
                #check Bitlocker GPO
                if isbitgpo:
                        Label(self.frame, text="Yes", fg="green").grid(row=3, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=3, column=1)
                        Button(self.frame, text="Apply GPO", command=lambda: (fwin.setGPOs(["bitlocker"]), self.reloadFrm())).grid(row=3, column=2)

                Label(self.frame, text="AppLocker enabled? ").grid(row=4, column=0)
                isapp=fwin.getApplocker()
                #check Bitlocker
                if isapp:
                        Label(self.frame, text="Yes", fg="green").grid(row=4, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=4, column=1)
                        Button(self.frame, text="Enable", command=lambda: (fwin.activateApplocker(), self.reloadFrm())).grid(row=4, column=2)
                        
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Fix All", command=self.fixAll).grid(row=0, column=2)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=3)
		
