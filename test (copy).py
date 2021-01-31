from tkinter import *
from tkinter import messagebox
from subprocess import Popen, PIPE
import re
window = Tk()
window.title("test")
window.geometry('350x200')
lbl = Label(window, text="test")
lbl.grid(column=0, row=2)
out = ['a','b','c']
def run(command):
 process = Popen(command, stdout=PIPE, shell=True)
 while True:
  line = process.stdout.readline().rstrip()
  if not line:
   break
  yield line
def clicked():
# lbl.configure(text="clicked")
 for path in run('sudo tegrastats'):
  x = re.search("CPU[ ].{0,50}[]][ ]", str(path))
  out[0] = x.group()
  y = re.search("GR3D_FREQ.{0,5}[%].{0,5}[ ]", str(path))
  out[1] = y.group()
  z = re.search("RAM[ ].{0,10}MB", str(path))
  out[2] = z.group()
  lbl.configure(text=out[0] + '\n' + out[1] + '\n' + out[2])
  print(out[0] + '\n' + out[1] + '\n' + out[2])
btn = Button(window, text="Click", command=clicked)
btn.grid(column=0, row=0)
window.mainloop()



