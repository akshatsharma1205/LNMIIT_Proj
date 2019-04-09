from tkinter import *
import os
import subprocess
import maca

   
nghbr = [["A", "B"], ["B", "C"], ["C", "D"]]

def show_entry_fields():
   #print("Sender: %s\nReceiver: %s" % (e1.get(), e2.get()))
   sndr = e1.get().upper()
   rcvr = e2.get().upper()

   if [sndr, rcvr] in nghbr or [rcvr, sndr] in nghbr:
   	print("Match Exist")
   	maca.__main__(sndr, rcvr)
   	#subprocess.Popen("python3 /Users/computer/Desktop/WSN_Proj/maca.py")
   	#os.system
   else:
   	print("no Match")

master = Tk()
Label(master, text="Sender").grid(row=0)
Label(master, text="Receiver").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )