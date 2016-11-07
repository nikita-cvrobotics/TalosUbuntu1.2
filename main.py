from Tkinter import *
import ttk

#Detect OS for future imports
import platform
ospltfm = platform.system()

winwidth = 1050
winheight = 480

root = Tk()
root.geometry("%dx%d" % (winwidth, winheight))
root.title("Talos Security Implementation Utility (TSIU) v1.2")
mainpane = ttk.Notebook(root)
mainpane.configure(width=winwidth, height=winheight)

if ospltfm == "Linux":
	import homepanelub
	homeTab = homepanelub.homeFrame(mainpane, ospltfm)
	mainpane.add(homeTab, text="Home", compound=TOP)
	import usrgrp
	usrgrpTab = usrgrp.usrgrpFrame(mainpane)
	mainpane.add(usrgrpTab, text="Users and Groups", compound=TOP)
	import prgm
	prgmTab = prgm.prgmFrm(mainpane)
	mainpane.add(prgmTab, text="Programs")
	import sec
	secTab = sec.secFrm(mainpane)
	mainpane.add(secTab, text="Basic Security")
	import pkgsec
	psecTab = pkgsec.secFrm(mainpane)
	mainpane.add(psecTab, text="Tool Security")
	import fwall
	fsecTab = fwall.secFrm(mainpane)
	mainpane.add(fsecTab, text="Firewall")
	import medub
	msecTab = medub.secFrm(mainpane)
	mainpane.add(msecTab, text="Media Files")
	import htools
	hsecTab = htools.secFrm(mainpane)
	mainpane.add(hsecTab, text="Hardening Tools")
	import damon
	dsecTab = damon.secFrm(mainpane)
	mainpane.add(dsecTab, text="Daemons")
	import selin
	ssecTab = selin.secFrm(mainpane)
	mainpane.add(ssecTab, text="SELinux")
elif ospltfm == "Windows":
	import homepanel
	homeTab = homepanel.homeFrame(mainpane, ospltfm)
	mainpane.add(homeTab, text="Home", compound=TOP)
	import usrgrpwin
	usrgrpTab = usrgrpwin.usrgrpFrame(mainpane)
	mainpane.add(usrgrpTab, text="Users and Groups", compound=TOP)
	import wsuwin
	wsuTab = wsuwin.wsuFrm(mainpane)
	mainpane.add(wsuTab, text="Updates", compound=TOP)
	import prgmwin
	prgmTab = prgmwin.prgmFrm(mainpane)
	mainpane.add(prgmTab, text="Programs", compound=TOP)
	import ftrwin
	ftrTab = ftrwin.ftrFrm(mainpane)
	mainpane.add(ftrTab, text="Features", compound=TOP)
	import secwin
	secTab = secwin.secFrm(mainpane)
	mainpane.add(secTab, text="Base Security", compound=TOP)
	import svcwin
	svcTab = svcwin.svcFrm(mainpane)
	mainpane.add(svcTab, text="Services", compound=TOP)
	import mediawin
	medTab = mediawin.medFrm(mainpane)
	mainpane.add(medTab, text="Media Files", compound=TOP)
	import syswin
	sysTab = syswin.sysFrm(mainpane)
	mainpane.add(sysTab, text="System Files", compound=TOP)
	import gpowin
	gpoTab = gpowin.gpoFrm(mainpane)
	mainpane.add(gpoTab, text="GPOs", compound=TOP)
	import fshwin
	fshTab = fshwin.fshFrm(mainpane)
	mainpane.add(fshTab, text="Network", compound=TOP)
	import avgwin
	avgTab = avgwin.avgFrm(mainpane)
	mainpane.add(avgTab, text="Antivirus", compound=TOP)
	import stawin
	staTab = stawin.secFrm(mainpane)
	mainpane.add(staTab, text="Tasks", compound=TOP)
	import bitwin
	bitTab = bitwin.bitFrm(mainpane)
	mainpane.add(bitTab, text="Bitlocker", compound=TOP)
else:
	print("ERROR - could not detect platform OS.")

mainpane.pack(fill=BOTH)
root.mainloop()
