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
   	print("Welcome, this is an implementation of MACA Protocol. \n")
   	maca.__main__(sndr, rcvr)
   	#subprocess.Popen("python3 /Users/computer/Desktop/WSN_Proj/maca.py")
   	#os.system
   else:
   	print("The sender & receiver are not neighbours or no such nodes exist, please check the above configuration.")

master = Tk()
Label(master, text="Sender").grid(row=0)
Label(master, text="Receiver").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

print("The configuration of nodes are:")
print("A :: B :: C :: D")
print("\nWaiting for your input...")

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )