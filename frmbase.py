from Tkinter import *
import os
import subprocess
import getpass

class frmbase(Frame):
	def onFrameConfig(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

		#CREATE A SCROLLER
		self.canvas = Canvas(self)
		self.frame = Frame(self.canvas)
		self.vsb = Scrollbar(self, orient="vertical", command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=self.vsb.set)
		self.hsb = Scrollbar(self, orient="horizontal", command=self.canvas.xview)
		self.canvas.configure(xscrollcommand=self.hsb.set)
		self.vsb.pack(side="right", fill="y")
		self.hsb.pack(side="bottom", fill="x")
		self.canvas.pack(side="left", fill="both", expand=True)
		self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
		self.frame.bind("<Configure>", self.onFrameConfig)
		self.pack(expand=True)
		
		self.reloadFrm()

	def reloadFrm(self):
		global flagCount
		global rowCount
		flagCount = 0
		for chile in self.frame.winfo_children():
			chile.destroy()
		self.regenFrm()
	def regenFrm(self):
		pass
