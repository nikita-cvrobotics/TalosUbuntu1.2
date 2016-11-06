import frmbase
from Tkinter import *
import subprocess
import os

class medFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
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
                Button(self.frame, text="Scan Users Folder").grid(row=1, column=2)
                Button(self.frame, text="Scan Entire Disk").grid(row=1, column=3)
                Label(self.frame, text="Media files to remove:").grid(row=2, column=0, sticky=W)
                Listbox(self.frame, selectmode=EXTENDED, width=80, height=20).grid(row=3, column=0, sticky=N)
                Button(self.frame, text=">> Exempt >>").grid(row=3, column=1, sticky=N)
                Listbox(self.frame, selectmode=EXTENDED, width=50, height=10).grid(row=3, column=2, sticky=N)
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Remove Files in List").grid(row=0, column=2)
