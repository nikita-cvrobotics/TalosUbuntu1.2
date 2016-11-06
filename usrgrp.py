from Tkinter import *
import os
import subprocess
import getpass

rec_min_age = 3
rec_max_age = 30
rec_warn_days = 7

rowCount = 0
flagCount = 0
def flagGuest(justBool):
	global flagCount
	if not justBool:
		return "green"
	else:
		flagCount += 1
		return "red"
def flagPass(justBool):
	global flagCount
	if justBool:
		return "green"
	else:
		flagCount += 1
		return "red"
def flagDis(beDisabled, name):
	global flagCount
	if (name == "root" and not beDisabled) or (name != "root" and beDisabled):
		flagCount += 1
		return "red"
	else:
		return "green"
def flagMin(minIn, name):
	global rec_min_age
	global flagCount
	if (minIn >= rec_min_age) or name == "root":
		return "green"
	else:
		flagCount += 1
		return "red"
def flagMax(maxIn, name):
	global rec_max_age
	global flagCount
	if (maxIn <= rec_max_age) or name == "root":
		return "green"
	else:
		flagCount += 1
		return "red"
def flagWarn(warnIn, name):
	global rec_warn_days
	global flagCount
	if (warnIn >= rec_warn_days) or name == "root":
		return "green"
	else:
		flagCount += 1
		return "red"
class usrgrpFrame(Frame):
	nameList=[]
	def delGroup(self, event, name):
		widget = event.widget
		selection = widget.curselection()
		for i in selection:
			currgp = widget.get(i)
			os.system("sudo deluser %s %s" % (name, currgp))
		self.resetFrm()
	def setUser(self, name, isEnabled):
		if isEnabled:
			os.system("sudo passwd -u %s" % name)
		else:
			os.system("sudo passwd -l %s" % name)
		self.resetFrm()
	def getGuest(self):
		if self.release == "14.04":
			stat = subprocess.check_output("cat /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf", shell=True)
			return "allow-guest=false" not in stat
	def setGuest(self, isEnabled):
		if self.release == "14.04":
			if isEnabled:
				os.system("sudo cp true50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf")
			else:
				os.system("sudo cp false50-ubuntu.conf /usr/share/lightdm/lightdm.conf.d/50-ubuntu.conf")
		self.resetFrm()
	def resetFrm(self):
		global flagCount
		global rowCount
		flagCount = 0
		rowCount = 0
		self.nameList = []
		self.reloadFrm()
	def deleteUser(self, name):
		os.system("sudo deluser %s" % name)
		self.resetFrm()
	def repairUsers(self):
		passwdLn = []
		with open("/etc/passwd", "r") as f:
			passwdLn = f.readlines()
		#Password protection
		os.system("echo '' > passcheck.txt")
		for currLine in passwdLn:
			clspl = currLine.split(":")
			if clspl[0] == "root" or int(clspl[2]) >= 1000:
				os.system("sudo echo '%s:P@ssword1@3$5^' | chpasswd" % clspl[0])
				os.system("echo '%s' >> passcheck.txt" % clspl[0])
		#Disable root
		os.system("sudo passwd -l root")
		shadowLn = []
		with open("/etc/shadow", "r") as f:
			shadowLn = f.readlines()
		#Password age protection
		with open("/etc/shadow", "w") as f:
			for currLine in shadowLn:
				clspl = currLine.split(":")
				clspl[3] = str(rec_min_age)
				clspl[4] = str(rec_max_age)
				clspl[5] = str(rec_warn_days)
				fixLine = ("%s:%s:%s:%s:%s:%s:%s:%s:%s" % (clspl[0], clspl[1], clspl[2], str(rec_min_age), str(rec_max_age), str(rec_warn_days), clspl[6], clspl[7], clspl[8]))
				if clspl[2].startswith("!") or clspl[2].startswith("*"):
					f.write(fixLine)
				else:
					for chkln in passwdLn:
						chspl = chkln.split(":")
						if chspl[0] == clspl[0]:
							if int(chspl[2]) >= 1000:
								f.write(fixLine)
							else:
								f.write(currLine)
		self.resetFrm()
	def usrfrm(self, master, name, isPassword, minage, maxage, warndays, groups, isDisabled):
		global rowCount
		global flagCount
		if name != "root":
			Button(master, text="delete", command=lambda: self.deleteUser(name)).grid(row=rowCount, column=0, sticky=W)
		Label(master, text=name).grid(row=rowCount, column=1, ipadx=10, ipady=5, sticky=W)
		ispass="No"
		if isPassword:
			ispass = "Yes"
		isdis = "No"
		if isDisabled:
			isdis = "Yes"
		Label(master, text=ispass, fg=flagPass(isPassword)).grid(row=rowCount, column=2, ipadx=10, ipady=5, sticky=W)
		Label(master, text=str(minage), fg=flagMin(minage, name)).grid(row=rowCount, column=3, ipadx=10, ipady=5, sticky=W)
		Label(master, text=str(maxage), fg=flagMax(maxage, name)).grid(row=rowCount, column=4, ipadx=10, ipady=5, sticky=W)
		Label(master, text=str(warndays), fg=flagWarn(warndays, name)).grid(row=rowCount, column=5, ipadx=10, ipady=5, sticky=W)
		#find groups
		grpls = subprocess.check_output("groups %s" % name, shell=True).split()
		if len(grpls) > 3:
			grplbox = Listbox(master, fg="red", selectmode=EXTENDED)
			grplbox.grid(row=rowCount, column=6, sticky=W)
			grplbox.bind("<Delete>", lambda evt, nm=name: self.delGroup(evt, nm))
			for i in range(3, len(grpls)):
				flagCount += 1
				grplbox.insert(END, grpls[i])
		else:
			Label(master, text="None", fg="green").grid(row=rowCount, column=6, ipadx=10, ipady=5, sticky=W)			
		Label(master, text=isdis, fg=flagDis(isDisabled, name)).grid(row=rowCount, column=7, ipadx=10, ipady=5, sticky=W)
		Button(master, text="Enable", command = lambda: self.setUser(name, True)).grid(row=rowCount, column=8)
		Button(master, text="Disable", command = lambda: self.setUser(name, False)).grid(row=rowCount, column=9)
		rowCount += 1
	def getUsers(self):
		result = []
		passwdData = []
		with open("/etc/passwd", "r") as f:
			passwdData = f.readlines()
		shadowData = []
		with open("/etc/shadow", "r") as f:
			shadowData = f.readlines()
		passComplete = []
		with open("passcheck.txt", "r") as f:
			while True:
				currComplete = f.readline()
				if not currComplete:
					break
				passComplete.append(currComplete[:-1])
		for psdusr in passwdData:
			dldat = psdusr.split(":")
			if dldat[0] == "root" or (int(dldat[2]) >= 1000 and dldat[0] != "nobody"):
				for shdat in shadowData:
					dldat2 = shdat.split(":")
					if dldat2[0] == dldat[0]:
						try:
							result.append([dldat2[0], dldat2[0] in passComplete, int(dldat2[3]), int(dldat2[4]), int(dldat2[5]), "NOPE", dldat2[1].startswith("!") or dldat2[1].startswith("*")])
						except:
							result.append([dldat2[0], dldat2[0] in passComplete, -1, 999999, -1, "NOPE", dldat2[1].startswith("!") or dldat2[1].startswith("*")])
							print "read error for", dldat2[0], "- check the shadow file."
		return result
	def onFrameConfig(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

		self.release = subprocess.check_output("lsb_release -r", shell=True).split()[1]
		os.system(">passcheck.txt")

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
		fdispt = Label(self.frame, text="Issues:", font="Arial 16 bold")
		fdispt.grid(row=rowCount, column=0, sticky=W, ipadx=10, ipady=10)
		flagDisp = Label(self.frame, font="Arial 16 bold")
		flagDisp.grid(row=rowCount, column=1, sticky=W, ipadx=10, ipady=10)
		Button(self.frame, text="Fix Now", command = lambda: self.repairUsers()).grid(row=rowCount, column=2, ipadx=10, ipady=10)
                Button(self.frame, text="Refresh", command = lambda: self.reloadFrm()).grid(row=rowCount, column=3, ipadx=10, ipady=10)
		rowCount += 1

		#Guest info
		Label(self.frame, text="Guest Session Status:").grid(row=rowCount, column=0, columnspan=2, ipadx=10, ipady=10)
		guesttxt = "Enabled"
		gstat = self.getGuest()
		if not gstat:
			guesttxt = "Disabled"
		Label(self.frame, text=guesttxt, fg=flagGuest(gstat)).grid(row=rowCount, column=2, ipadx=10, ipady=10)
		Button(self.frame, text="Enable", command = lambda: self.setGuest(True)).grid(row=rowCount, column=3)
		Button(self.frame, text="Disable", command = lambda: self.setGuest(False)).grid(row=rowCount, column=4)
		rowCount += 1
		
		#Grid titles
		Label(self.frame, text="Delete?").grid(row=rowCount, column=0, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Name").grid(row=rowCount, column=1, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="P@ssword1@3$5^ Set?").grid(row=rowCount, column=2, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Min Pass Age").grid(row=rowCount, column=3, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Max Pass Age").grid(row=rowCount, column=4, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Pass Warn Days").grid(row=rowCount, column=5, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Groups").grid(row=rowCount, column=6, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Disabled?").grid(row=rowCount, column=7, sticky=W, ipadx=10, ipady=5)
		rowCount += 1
		for curusr in self.getUsers():
			self.nameList.append(self.usrfrm(self.frame, curusr[0], curusr[1], curusr[2], curusr[3], curusr[4], curusr[5], curusr[6]))
		issuefg = "red"
		if flagCount == 0:
			issuefg = "green"
		flagDisp.configure(fg=issuefg, text=str(flagCount))
		fdispt.configure(fg=issuefg)
