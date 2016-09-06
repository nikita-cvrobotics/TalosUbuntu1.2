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
    import usrgrp
    usrgrpTab = usrgrp.usrgrpFrame(mainpane)
    mainpane.add(usrgrpTab, text="Users and Groups", compound=TOP)
elif ospltfm == "Windows":
    #import usrgrpwin
    #usrgrpTab = usrgrpwin.usrgrpFrame(mainpane)
    #mainpane.add(usrgrpTab, text="Users and Groups", compound=TOP)
    pass

prgmTab = Frame(mainpane)
mainpane.add(prgmTab, text="Programs")

mainpane.pack(fill=BOTH)
root.mainloop()
