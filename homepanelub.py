from Tkinter import *

class homeFrame(Frame):
    def onFrameConfig(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    def __init__(self, master, ospltfm):
        Frame.__init__(self, master)
        self.master = master
        self.ospltfm = ospltfm

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
        self.rowCount = 0
        Label(self.frame, text=self.ospltfm + " platform detected.", font="Arial 16 bold").grid(row=self.rowCount, column=1, columnspan=2, ipadx=10, ipady=10)
        self.rowCount += 1
