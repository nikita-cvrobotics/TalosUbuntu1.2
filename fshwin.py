import frmbase
from Tkinter import *
import subprocess
import os
import fwin

class fshFrm(frmbase.frmbase):
	flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def fixAll(self):
                fwin.rmshare(fwin.getshare())
                fwin.applyFW(fwin.WIN_7)
                self.reloadFrm()
	def regenFrm(self):
                self.flagCount = 0
                
		Label(self.frame, text="Scandalous Folder Shares:").grid(row=1, column=0, sticky=W)
		shareList = fwin.getshare()
		fshbox = Listbox(self.frame, selectmode=EXTENDED, width=40, height=6, fg="red")
		for i in shareList:
                        self.flagCount += 1
                        fshbox.insert(END, i)
                fshbox.bind("<Delete>", lambda evt: (fwin.rmshare(fwin.LFB(evt)), self.reloadFrm()))
                fshbox.grid(row=2, column=0, sticky=W)
                #Network issues
                Label(self.frame, text="Firewall", font="Arial 12 bold").grid(row=3, column=0, sticky=W)
                #check if firewall is using recommended settings
                firewallGood = fwin.getFirewall()
                if firewallGood:
                        Label(self.frame, text="Enabled", fg="green").grid(row=3, column=1, ipadx=10)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="Disabled", fg="red").grid(row=3, column=1, ipadx=10)
                Button(self.frame, text="Enable", command=lambda: (fwin.setFirewall(True), self.reloadFrm())).grid(row=3, column=2)

                Button(self.frame, text="Apply .wfw file", command=lambda: (fwin.applyFW(fwin.WIN_7), self.reloadFrm())).grid(row=4, column=0)
                Label(self.frame, text="Port rules to annihilate:").grid(row=5, column=0, sticky=W)
		frules = fwin.getPorts()
		rrules = Listbox(self.frame, selectmode=EXTENDED, width=60, fg="red")
		rrules.bind("<Delete>", lambda evt: (fwin.remFWrule(fwin.LFB(evt)), self.reloadFrm()))
		rrules.grid(row=6, column=0)
                Label(self.frame, text="Port rules to add:").grid(row=7, column=0, sticky=W)
		arules = Listbox(self.frame, selectmode=EXTENDED, width=60, fg="red")
		arules.bind("<Delete>", lambda evt: (fwin.addFWrule(fwin.LFB(evt)), self.reloadFrm()))
		arules.grid(row=8, column=0)

		for i in frules["exceptions"]:
                        self.flagCount += 1
                        rrules.insert(END, i)
                for i in frules["gaps"]:
                        self.flagCount += 1
                        arules.insert(END, i)
                #issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Fix All", command=self.fixAll).grid(row=0, column=2)
                Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=3)
