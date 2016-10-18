from Tkinter import *
import os
import subprocess
import getpass
import sys

'''
The following settings are recommended:
Admin(rename)   passchangeable:Y passexpires:Y passrequired:Y groups:admin disabled:Y
Guest(rename)   passchangeable:N passexpires:N passrequired:N groups:Guests disabled:Y
All other users: passchangeable:Y passexpires:Y passrequired:Y groups:none disabled:N
'''
rowCount = 0
flagCount = 0
def flagDisabled(name, isDisabled):
        global flagCount
        if (name == "Guest" or name == "Administrator" or name == "TalosWasHere" or name == "TalosWasHereToo"):
                if isDisabled:
                        return "green"
                else:
                        flagCount += 1
                        return "red"
        else:
                if isDisabled:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
def flagPass(isPass):
        global flagCount
        if isPass:
                return "green"
        else:
                flagCount += 1
                return "red"
def flagPassChg(name, isChg):
        global flagCount
        if name == "Guest" or name == "TalosWasHereToo":
                if isChg:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
        else:
                if not isChg:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
def flagPassExp(name, isExp):
        global flagCount
        if name == "Guest" or name == "TalosWasHereToo":
                if isExp:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
        else:
                if not isExp:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
def flagPassReq(name, isReq):
        global flagCount
        if name == "Guest" or name == "TalosWasHereToo":
                if isReq:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
        else:
                if not isReq:
                        flagCount += 1
                        return "red"
                else:
                        return "green"
def flagName(name):
        global flagCount
        if name == "Guest" or name == "Administrator":
                flagCount += 1
                return "red"
        else:
                return "green"
class usrgrpFrame(Frame):
	nameList=[]
	def resetFrm(self):
		global flagCount
		global rowCount
		flagCount = 0
		rowCount = 0
		self.nameList = []
		self.reloadFrm()
	def repairUsers(self):
		#Apply fixes
                os.system("wmic useraccount where name='Administrator' rename TalosWasHere")
                os.system("wmic useraccount where name='Guest' rename TalosWasHereToo")
		self.resetFrm()
	def usrfrm(self, master, name, isPassword, pschg, psexp, psreq, groups, isDisabled):
		global rowCount
		global flagCount
		if name != "Administrator" and name != "Guest":
			Button(master, text="delete", command=lambda: self.deleteUser(name)).grid(row=rowCount, column=0, sticky=W)
		Label(master, text=name, fg=flagName(name)).grid(row=rowCount, column=1, ipadx=10, ipady=5, sticky=W)
		ispass="No"
		if isPassword:
			ispass = "Yes"
		isdis = "No"
		if isDisabled:
			isdis = "Yes"
		Label(master, text=ispass, fg=flagPass(isPassword)).grid(row=rowCount, column=2, ipadx=10, ipady=5, sticky=W)
		Label(master, text=str(pschg), fg=flagPassChg(name, pschg == "TRUE")).grid(row=rowCount, column=3, ipadx=10, ipady=5, sticky=W)
		Label(master, text=str(psexp), fg=flagPassChg(name, psexp == "TRUE")).grid(row=rowCount, column=4, ipadx=10, ipady=5, sticky=W)
		Label(master, text=str(psreq), fg=flagPassChg(name, psreq == "TRUE")).grid(row=rowCount, column=5, ipadx=10, ipady=5, sticky=W)
		#find groups
		#grpls = subprocess.check_output("groups %s" % name, shell=True).split()
                grpls = []
		if len(grpls) > 3:
			grplbox = Listbox(master, fg="red", selectmode=EXTENDED)
			grplbox.grid(row=rowCount, column=6, sticky=W)
			grplbox.bind("<Delete>", lambda evt, nm=name: self.delGroup(evt, nm))
			for i in range(3, len(grpls)):
				flagCount += 1
				grplbox.insert(END, grpls[i])
		else:
			Label(master, text="None", fg="green").grid(row=rowCount, column=6, ipadx=10, ipady=5, sticky=W)			
		Label(master, text=isdis, fg=flagDisabled(name, isDisabled)).grid(row=rowCount, column=7, ipadx=10, ipady=5, sticky=W)
		Button(master, text="Enable").grid(row=rowCount, column=8)
		Button(master, text="Disable").grid(row=rowCount, column=9)
		rowCount += 1
	def getGroups(self):
                groupArr = subprocess.check_output("net localgroup", shell=True).splitlines()
                resultMap = {}
                for i in groupArr:
                    if i.startswith("*"):
                        currGrpStr = i[1:]
                        userList = []
                        grpOut = subprocess.check_output('net localgroup "' + currGrpStr + '"', shell=True).splitlines()
                        for i in range(6, 100):
                            if grpOut[i] == "The command completed successfully." or grpOut[i] == "":
                                break
                            userList.append(grpOut[i])
                        if len(userList) > 0:
                            resultMap[currGrpStr] = userList
                return resultMap
	def getUsers(self):
		result = []
                wmicList = subprocess.check_output("wmic useraccount").splitlines()
                isLastSpace = True
                wmicMarks = []
                for currIter in range(0, len(wmicList[0])):
                        if wmicList[0][currIter] != ' ' and isLastSpace:
                                wmicMarks.append(currIter)
                        isLastSpace = wmicList[0][currIter] == ' '
                for wmicLine in range(2, len(wmicList) - 2, 2):
                        wmicFL = []
                        for currMark in range(0, len(wmicMarks) - 1):
                                startRead = wmicMarks[currMark]
                                endRead = wmicMarks[currMark + 1]
                                editLine = wmicList[wmicLine]
                                wmicFL.append(editLine[startRead:endRead].rstrip())
                        startRead = wmicMarks[len(wmicMarks) - 1]
                        editLine = wmicList[len(wmicList) - 2]
                        endRead = len(editLine)
                        wmicFL.append(editLine[startRead:endRead].rstrip())
                        result.append([wmicFL[9], False, wmicFL[10], wmicFL[11], wmicFL[12], [], wmicFL[3] == "TRUE"])
		return result
	def onFrameConfig(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.master = master

		os.system("type NUL > passcheck.txt")

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
		
		#Grid titles
		Label(self.frame, text="Delete?").grid(row=rowCount, column=0, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="Name").grid(row=rowCount, column=1, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="P@ssword1@3$5^ Set?").grid(row=rowCount, column=2, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="PasswordChangeable").grid(row=rowCount, column=3, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="PasswordExpires").grid(row=rowCount, column=4, sticky=W, ipadx=10, ipady=5)
		Label(self.frame, text="PasswordRequired").grid(row=rowCount, column=5, sticky=W, ipadx=10, ipady=5)
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
