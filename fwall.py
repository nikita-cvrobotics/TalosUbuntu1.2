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
		isufw = subprocess.check_output("ufw status", shell=True) == "Status: active"
		Label(self.frame, text="UFW enabled: ").grid(row=1, column=0, sticky=W)
		if isufw:
			Label(self.frame, text="Yes", fg="green").grid(row=1, column=1)
		else:
			self.flagCount += 1
			Label(self.frame, text="No", fg="red").grid(row=1, column=1)
			Button(self.frame, text="Enable UFW").grid(row=1, column=3)
		#issue display
                fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold").grid(row=0, column=0, sticky=W)
                fans = Label(self.frame, text=str(self.flagCount), font="Arial 16 bold", fg=self.cheapSelect(self.flagCount > 0, "red", "green"))
                fans.grid(row=0, column=1, sticky=W, ipadx=10)
                Button(self.frame, text="Fix All").grid(row=0, column=2)
		
