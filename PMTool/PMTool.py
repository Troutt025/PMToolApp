import tkinter as tk
from tkinter import ttk
from datetime import date
import os

# Set variables for DeltaV drive letters and Machine information
DVDriveLetter = ""
DVDataLoc = ":\deltav\dvdata\download"
strNodeName = ""
strNodeType = ""
strWinEdition = ""
backupsLocation = "D"
dateStamp = date.today()

# Check for dt.scr and set variables related
if(os.path.exists("C" + DVDataloc + "\dt.scr")):
    DVDriveLetter = "C"
elif(os.path.exists("D" + DVDataloc + "\dt.scr")):
    DVDriveLetter = "D"
else:
    DVDataLoc = ""

class PMToolApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('PMTool')
        self.geometry('640x480')
        self.minsize(640,480)

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        self.frames = {}
        for F in (HomePage, Backups, CopyFiles, SystemInformation):
            frame = F(container, self)

            self.frames[F] = frame
            frame.place(relwidth = 1.0, relheight = 1.0)

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    
# Home Page for Backups, File Copying, and System Information
class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels and Buttons for window
        label = ttk.Label(self, text = "Home Page")
        label.place(relx = 0.5, rely = 0.0, anchor = 'n')

        button1 = ttk.Button(self, text = "Backups",
                             command = lambda : controller.show_frame(Backups))
        button1.place(relx = 0.5, rely = 0.3, anchor = 'center', height = 50, width = 150)

        button2 = ttk.Button(self, text = "Copy Files",
                             command = lambda : controller.show_frame(CopyFiles))
        button2.place(relx = 0.5, rely = 0.5, anchor = 'center', height = 50, width = 150)

        button3 = ttk.Button(self, text = "System Information",
                             command = lambda : controller.show_frame(SystemInformation))
        button3.place(relx = 0.5, rely = 0.7, anchor = 'center', height = 50, width = 150)


# Backups window for gathering backups and system information
class Backups(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def gatherBackups():
            # Set top level window variables
            gatherBackupsTopWin = tk.Toplevel()
            gatherBackupsTopWin.title("Backups")
            gatherBackupsTopWin.geometry('640x480')
            gatherBackupsTopWin.minsize(640,480)

        def gatherSysInfo():
            # Set top level window variables
            gatherSysInfoTopWin = tk.Toplevel()
            gatherSysInfoTopWin.title("Backups")
            gatherSysInfoTopWin.geometry('640x480')
            gatherSysInfoTopWin.minsize(640,480)

        # Labels and Buttons for window
        label = ttk.Label(self, text = "Backups")
        label.place(relx = 0.5, rely = 0.0, anchor = 'n')

        button1 = ttk.Button(self, text = "Back",
                             command = lambda : controller.show_frame(HomePage))
        button1.place(relx = 0.0, rely = 0.0, anchor = 'nw')

        button2 = ttk.Button(self, text = "Gather Backups",
                             command = gatherBackups)
        button2.place(relx = 0.5, rely = 0.4, anchor = 'center', height = 50, width = 160)

        button3 = ttk.Button(self, text = "Gather System Information",
                             command = gatherSysInfo)
        button3.place(relx = 0.5, rely = 0.6, anchor = 'center', height = 50, width = 160)


# Copy file window for selecting files to copy, selecting machines to copy to, and copying the selections to the destinations
class CopyFiles(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def filesTop():
            # Set top level window variables
            filesTopWin = tk.Toplevel()
            filesTopWin.title("Copy Files")
            filesTopWin.geometry('640x480')
            filesTopWin.minsize(640,480)

            label = ttk.Label(filesTopWin, text = DVDriveLetter)
            label.place(relx = 0.5, rely = 0.5, anchor = 'center')

        def machinesTop():
            # Set top level window variables
            machinesTopWin = tk.Toplevel()
            machinesTopWin.title("Copy Files")
            machinesTopWin.geometry('640x480')
            machinesTopWin.minsize(640,480)

        def startCopy():
            # Set top level window variables
            startCopyTopWin = tk.Toplevel()
            startCopyTopWin.title("Copy Files")
            startCopyTopWin.geometry('640x480')
            startCopyTopWin.minsize(640,480)

        # Labels and Buttons for window
        label = ttk.Label(self, text = "Copy Files")
        label.place(relx = 0.5, rely = 0.0, anchor = 'n')

        button1 = ttk.Button(self, text = "Back",
                             command = lambda : controller.show_frame(HomePage))
        button1.place(relx = 0.0, rely = 0.0, anchor = 'nw')

        button2 = ttk.Button(self, text = "Select Files",
                             command = filesTop)
        button2.place(relx = 0.5, rely = 0.3, anchor = 'center', height = 50, width = 150)

        button3 = ttk.Button(self, text = "Select Machines",
                             command = filesTop)
        button3.place(relx = 0.5, rely = 0.5, anchor = 'center', height = 50, width = 150)

        button4 = ttk.Button(self, text = "Start Copy",
                             command = filesTop)
        button4.place(relx = 0.5, rely = 0.7, anchor = 'center', height = 50, width = 150)


# Window for displaying system information gathered in backups window
class SystemInformation(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels and Buttons for window
        label = ttk.Label(self, text = "System Information")
        label.place(relx = 0.5, rely = 0.0, anchor = 'n')

        button1 = ttk.Button(self, text = "Back",
                             command = lambda : controller.show_frame(HomePage))
        button1.place(relx = 0.0, rely = 0.0, anchor = 'nw')


# Driver code
PMToolApp = PMToolApp()
PMToolApp.mainloop()