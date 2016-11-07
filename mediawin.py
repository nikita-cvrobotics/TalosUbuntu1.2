import frmbase
from Tkinter import *
import subprocess
import os
import fwin

class medFrm(frmbase.frmbase):
        flagCount = 0
        mediaList = []
        meList = []
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
        def scanUsers(self):
                self.mediaList = []
                self.meList = []
                self.mediaList = fwin.scanUsers()
                self.reloadFrm()
        def scanDisk(self):
                self.mediaList = []
                self.meList = []
                self.mediaList = fwin.scanDisk()
                self.reloadFrm()
        def remFiles(self):
                toRemove = []
                for i in self.mediaList:
                        if i not in self.meList:
                                toRemove.append(i)
                fwin.removeMediaFiles(toRemove)
        def eFile(self, lb):
                for i in fwin.LFW(lb):
                        if i not in self.meList:
                                self.meList.append(i)
                                self.mediaList.remove(i)
                self.reloadFrm()
        def ueFile(self, lb):
                for i in fwin.LFW(lb):
                        if i not in self.mediaList:
                                self.mediaList.append(i)
                                self.meList.remove(i)
                self.reloadFrm()
	def regenFrm(self):
                self.flagCount = 0
                uscan = False
		Label(self.frame, text="Users Folder scanned? ").grid(row=1, column=0, sticky=W)
                #check logs for media scan
		if uscan:
                        Label(self.frame, text="Yes", fg="green").grid(row=1, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=1, column=1)
                Button(self.frame, text="Scan Users Folder", command=self.scanUsers).grid(row=1, column=2)
                Button(self.frame, text="Scan Entire Disk", command=self.scanDisk).grid(row=1, column=3)
                Label(self.frame, text="Media files to remove:").grid(row=2, column=0, sticky=W)
                haxList = Listbox(self.frame, selectmode=EXTENDED, width=80, height=20, fg="red")
                for i in self.mediaList:
                        if i not in self.meList:
                                haxList.insert(END, i)
                haxList.grid(row=3, column=0, sticky=N, rowspan=2)
                
                Button(self.frame, text=">> Exempt >>", command=lambda: self.eFile(haxList)).grid(row=3, column=1, sticky=S, ipadx=5)
                Button(self.frame, text="<< Unexempt <<", command=lambda: self.ueFile(ehaxList)).grid(row=4, column=1, sticky=N)                
                
                ehaxList = Listbox(self.frame, selectmode=EXTENDED, width=60, height=20, fg="orange")
                for i in self.meList:
                        ehaxList.insert(END, i)
                ehaxList.grid(row=3, column=2, sticky=N, rowspan=2)
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Remove Files in List", command=self.remFiles).grid(row=0, column=2)
