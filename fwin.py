'''
While most of the other files are calibrated to appeal to the senses
(With a GUI), the competition also requires that the displayed (and pretty)
tasks are also functional. This document serves to achieve that lofty goal.
'''

WIN_7 = 0
fwpath = {
WIN_7:"wfw\\win7hlevel.wfw"
}

def LFB(evt):
    result = []
    widget = evt.widget
    sel = widget.curselection()
    for i in sel:
        result.append(widget.get(i))
    return result
def LFW(wid):
    result = []
    for i in wid.curselection():
        result.append(wid.get(i))
    return result
#=== FIREWALL ===
def getFirewall():
    return False
def setFirewall(setting):
    if setting:
        print "Enabling firewall!"
    else:
        print "Disabling firewall! What are you doing??"
def applyFW(fwid):
    try:
        print "Applying firewall policy in " + fwpath[fwid]
    except:
        print "Error finding wfw id", fwid
def getshare():
    return ["I am an enemy.", "And yet another enemy."]
def rmshare(shl):
    for i in shl:
        print("Removing share " + i)
def getPorts():
    return {"exceptions":["ALLOW FTP 20, 21", "ALLOW SSH 22", "ALLOW Telnet 23"],
            "gaps":["DENY FTP 20, 21", "DENY TELNET 23", "ALLOW HTTPS 443"]}
def addFWrule(rule):
    for i in rule:
        print "Adding rule to", i
def remFWrule(rule):
    for i in rule:
        print "Destroying rule to", i
#=== UPDATES ===
def getSPs(ver):
    result = []
    if ver == WIN_7:
        sp1 = False
        #Check for SP1
        result.append(sp1)
    return result
def installSP1():
    print "Installing SP1 from \\client\\afsa\\awefae\\fsaf\\ase\\f!!"
def getWSUS():
    iswsus = False
    #check WSUS
    return iswsus
def runWSUS():
    print "Executing \\client\\UpdateInstaller.exe!!!"
def getSecunia():
    isSecunia = False
    #check WSUS
    return isSecunia
def runSecunia():
    print "Executing Secunia Installer!"
def getUpdateSettings():
    isautoupt = False
    #check Automatic Updates
    return isautoupt
def fixUpdates():
    print "Fixing auto updates!"
#=== PROGRAMS ===
def getCCleaner():
    isCCleaner = False
    #Check CCleaner
    return isCCleaner
def runCCleaner():
    print "Running CCleaner scan"
def getBadPrograms():
    result = ["Item1", "Item2", "Item3"]
    #get bad programs
    return result
def getBadPrgFiles():
    result = ["Item1", "Item2", "Item3"]
    #get bad prg files
    return result
def remPrograms(remList):
    print "Removing programs", remList
def remPrgFiles(remList):
    print "Removing program files", remList
#=== FEATURES ===
def getFeatures():
    return {"remove":["ft1", "ft2", "ft3"],
            "install":["ft1", "ft2", "ft3"]}
def removeFeatures(nameList):
    for name in nameList:
        print "Removing", name
def addFeatures(nameList):
    for name in nameList:
        print "Installing", name
#=== BASE SECURITY ===
def getBaseSecpol():
    result = {"allow1":False, "audit1":False, "systime":False}
    return result
def applySecpol(ver):
    if ver == WIN_7:
        print "Applying Secpol .INF file"
def getRDP():
    rdp = False
    #Check RDP
    return rdp
def setRDP(state):
    if state:
        print "Enabling Remote Desktop!"
    else:
        print "DESTROYING Remote Desktop"
#=== SERVICES ===
def getServicesToFix():
    return {"disable":["svc1", "svc2", "svc3"],
            "manual":["svc1", "svc2", "svc3"],
            "auto":["svc1", "svc2", "svc3"]}
def setSvc(svc, state):
    if state == "disable":
        print "Disabling", svc
    elif state == "manual":
        print "Manualing", svc
    elif state == "auto":
        print "Autoing", svc
def setSvcs(svcList, state):
    for i in svcList:
        setSvc(i, state)
def applyReg(ver):
    print "Applying reg", ver
#=== MEDIA FILES ===
def scanUsers():
    print "Scanning C:\\Users..."
    result = ["file1", "file2", "file3"]
    #fill up results
    return result
def scanDisk():
    print "Scanning C:\\ - Brace yourself."
    result = ["dfile1", "dfile2", "dfile3"]
    #fill up results
    return result
def removeMediaFiles(flist):
    print "Removing", flist
#=== SYSTEM FILES ===
def showHiddenFolders():
    print "Revealing hidden folders and extensions to the public eye..."
def isHostsSafe():
    defhosts = False
    #Check hosts
    return defhosts
def scanSysFiles():
    return ["hack1", "hack2", "hack3"]
def scanACLs():
    return [[ "issue1", [("Bob1", "Admin"), ("Bob2", "User")] ], [ "issue2", [("Bob1", "Admin"), ("Bob2", "User")] ]]
def scanUserFolders():
    return ["Phileeep", "Johannes"]
def remHaxFiles(pathlist):
    for path in pathlist:
        print "Removing file", path
def remUserFolders(pathlist):
    for path in pathlist:
        print "Removing user folder", path
def fixACLs(pathlist):
    for path in pathlist:
        print "Fixing ACL of", path
#=== GPOs ===
def getGPOs():
    isgpos = {"domain":False, "computer":False, "user":False,
              "bitlocker":False, "stig":False}
def setGPOs(gpolist):
    for i in gpolist:
        print "Applying", i
def installEMET():
    print "Installing EMET"
#=== ANTIVIRUS ===
def getAVscans():
    return {"avg":False, "mwb":False, "mse":False, "wdf":False}
def installAVG():
    print "Installing AVG!"
def installMWB():
    print "Installing MalwareBytes!"
def installMSE():
    print "Installing MSE!"
def installWDF():
    print "Installing Windows Defender!"
#=== TASKS ===
def getStartupList():
    return ["prg1", "prg2", "prg3", "prg4"]
def getSchTaskProblems():
    return ["task1", "task2", "task3", "task4"]
def remSchTasks(tasklist):
    for i in tasklist:
        print "Deleting task", i
def remStartups(stlist):
    for i in stlist():
        print "Disabling auto start for", i
#=== BITLOCKER ===
def getBitlocker():
    isbit = False
    #Check bitlocker
    return isbit
def activateBitlocker():
    print "Enabling Bitlocker!"
def getApplocker():
    isapp = False
    #Check Applocker
    return isapp
def activateApplocker():
    print "Activating AppLocker!"
