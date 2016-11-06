import frmbase
from Tkinter import *
import subprocess
import os

class secFrm(frmbase.frmbase):
	flagCount = 0
	def cheapSelect(self, btest, fan, san):
                if btest:
                        return fan
                return san
	def regenFrm(self):
                self.flagCount = 0
		Label(self.frame, text="Autoruns and Scheduled tasks have not been patched yet.").grid(row=1, column=0, sticky=W)
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Fix All").grid(row=0, column=2)
		
