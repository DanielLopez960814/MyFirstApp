import os
from tkinter import filedialog
from tkinter import Tk
import sys


def Load():
	root = Tk()
	dirname = filedialog.askdirectory(parent=root,initialdir="/",title='Please select a directory')
	#a = []
	#contador = 0
	file1 = open("Ruta.txt","w")#write mode 
	 

	for filename in os.listdir(dirname):
	   # do your stuff
	   
	   file1.write(str(dirname) + '/' + str(filename)+"\n")
	
	file1.close() 
	root.destroy()

#print('That\'\s ok, the path was already load')
#sys.stdout.flush()