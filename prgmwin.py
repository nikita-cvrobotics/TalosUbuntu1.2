import frmbase
from Tkinter import *
import subprocess
import os
import fwin

class prgmFrm(frmbase.frmbase):
	flagCount = 0
	eplist = []
	epflist = []
	def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def fixAll(self):
                fwin.runCCleaner()
<<<<<<< HEAD
                self.killPrograms()
                #WAIT FOR UNINSTALLS TO COMPLETE, THEN DO NEXT COMMAND!!
                self.killProgramFiles()
=======
                fwin.remPrograms(fwin.getBadPrograms())
                #WAIT FOR UNINSTALLS TO COMPLETE, THEN DO NEXT COMMAND!!
                fwin.remPrgFiles(fwin.getBadPrgFiles())
>>>>>>> origin/Windows-usrgrp
                self.reloadFrm()
        def ePrg(self, lbw):
                for i in lbw.curselection():
                        if lbw.get(i) not in self.eplist:
                                self.eplist.append(lbw.get(i))
                self.reloadFrm()
        def ePrgF(self, lbw):
                for i in lbw.curselection():
                        if lbw.get(i) not in self.epflist:
                                self.epflist.append(lbw.get(i))
                self.reloadFrm()
        def uePrg(self, lbw):
                for i in lbw.curselection():
                        if lbw.get(i) in self.eplist:
                                self.eplist.remove(lbw.get(i))
                self.reloadFrm()
        def uePrgF(self, lbw):
                for i in lbw.curselection():
                        if lbw.get(i) in self.epflist:
                                self.epflist.remove(lbw.get(i))
                self.reloadFrm()
<<<<<<< HEAD
        def killPrograms(self):
                toDestroy = []
                for i in fwin.getBadPrograms():
                        if i not in self.eplist:
                                toDestroy.append(i)
                fwin.remPrograms(toDestroy)
        def killProgramFiles(self):
                toDestroy = []
                for i in fwin.getBadPrgFiles():
                        if i not in self.epflist:
                                toDestroy.append(i)
                fwin.remPrograms(toDestroy)
=======
>>>>>>> origin/Windows-usrgrp
	def regenFrm(self):
                self.flagCount = 0
                Label(self.frame, text="CCleaner scan completed?").grid(row=1, column=0)
                ccleaned=fwin.getCCleaner()
                if ccleaned:
                        Label(self.frame, text="Yes", fg="green").grid(row=1, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=1, column=1)
                        Button(self.frame, text="Install CCleaner", command=lambda: (fwin.runCCleaner(), self.reloadFrm())).grid(row=1, column=2)
                bprgmlist = fwin.getBadPrograms()
                for i in self.eplist:
                        if i in bprgmlist:
                                bprgmlist.remove(i)
                Label(self.frame, text="Programs to Remove:").grid(row=2, column=0, sticky=W)
                prembox = Listbox(self.frame, selectmode=EXTENDED, width=40, fg="red")
                for i in bprgmlist:
                        self.flagCount += 1
                        prembox.insert(END, i)
                prembox.grid(row=3, column=0, rowspan=2)
                
                Label(self.frame, text="Exempted Programs:").grid(row=2, column=2, sticky=W)
                epbox = Listbox(self.frame, selectmode=EXTENDED, width=40, fg="orange")
                for i in self.eplist:
                        epbox.insert(END, i)
                epbox.grid(row=3, column=2, rowspan=2)
                
                Button(self.frame, text=">> Exempt >>", command=lambda: self.ePrg(prembox)).grid(row=3, column=1)
                Button(self.frame, text="<< Unexempt <<", command=lambda: self.uePrg(epbox)).grid(row=4, column=1)
                bpflist = fwin.getBadPrgFiles()
                for i in self.epflist:
                        if i in bpflist:
                                bpflist.remove(i)
                Label(self.frame, text="Program File Folders to Destroy:").grid(row=5, column=0, sticky=W)
                bpfrembox = Listbox(self.frame, selectmode=EXTENDED, width=40, fg="red")
                for i in bpflist:
                        self.flagCount += 1
                        bpfrembox.insert(END, i)
                bpfrembox.grid(row=6, column=0, rowspan=2)
                Label(self.frame, text="Exempted Program File Folders:").grid(row=5, column=2, sticky=W)
                epfbox = Listbox(self.frame, selectmode=EXTENDED, width=40, fg="orange")
                
                for i in self.epflist:
                        epfbox.insert(END, i)
                epfbox.grid(row=6, column=2, rowspan=2)
                
                Button(self.frame, text=">> Exempt >>", command=lambda: self.ePrgF(bpfrembox)).grid(row=6, column=1)
                Button(self.frame, text="<< Unexempt <<", command=lambda: self.uePrgF(epfbox)).grid(row=7, column=1)
		Button(self.frame, text="Fix", command=self.fixAll).grid(row=0, column=2)
		Button(self.frame, text="Refresh", command=self.reloadFrm).grid(row=0, column=3)
		fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)

		
		
