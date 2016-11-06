import frmbase
from Tkinter import *
import subprocess
import os

class sysFrm(frmbase.frmbase):
        flagCount = 0
        def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
	def regenFrm(self):
                self.flagCount = 0
                Button(self.frame, text="Fix").grid(row=0, column=2, ipadx=5)
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                Label(self.frame, text="Searching for hidden files and folders?").grid(row=1, column=0, sticky=E)
                hidchk = False
                #check hidden file setting
                
                if not hidchk:
                        self.flagCount += 1
                        Button(self.frame, text="Include Hidden").grid(row=1, column=2, sticky=W)
                        Label(self.frame, text="No", fg="red").grid(row=1, column=1)
                else:
                        Label(self.frame, text="Yes", fg="green").grid(row=1, column=3)
                ishostsdef = False
                #Check for hosts
                Label(self.frame, text="Hosts file contains only default entries? ").grid(row=2, column=0, sticky=E)
                if ishostsdef:
                        Label(self.frame, text="Yes", fg="green").grid(row=2, column=1)
                else:
                        self.flagCount += 1
                        Label(self.frame, text="No", fg="red").grid(row=2, column=1)
                        Button(self.frame, text="Fix hosts file").grid(row=2, column=2)
		Label(self.frame, text="Files of Concern:").grid(row=3, column=0, sticky=W)
                #check for extra files
                Listbox(self.frame, selectmode=EXTENDED, width=50).grid(row=4, column=0)
                Label(self.frame, text="Files Missing:").grid(row=5, column=0, sticky=W)
                #check for lack of files
                Listbox(self.frame, selectmode=EXTENDED, width=50).grid(row=6, column=0)
                Label(self.frame, text="ACL Issues:").grid(row=3, column=1, sticky=W)
                #sysinternals accesschk partay
                Listbox(self.frame, selectmode=EXTENDED, width=50).grid(row=4, column=1)
                Label(self.frame, text="User Folders:").grid(row=5, column=1, sticky=W)
                #Compare user folders to users
                Listbox(self.frame, selectmode=EXTENDED, width=50).grid(row=6, column=1)

                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W)
