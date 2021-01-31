from tkinter import *
from subprocess import Popen, PIPE
import subprocess
import re
window = Tk()
window.title("test")
window.geometry('350x200')
lbl = Label(window, text="CPU [000%@0000,000%@0000,000%@0000,000%@0000]", justify=LEFT)
lbl.grid(sticky = W, column=0, row=3)
out = ['a','b','c']
def stopall():
 subprocess.Popen.kill(process)
 window.mainloop()
def kill():
 sys.exit()
 quit()
 exit()

def run(command):
 process = subprocess.Popen(command, stdout=PIPE, shell=True)
 while True:
  line = process.stdout.readline().rstrip()
  if not line:
   break
  yield line
def clicked():
 while 1 == 1 :
  for path in run('sudo tegrastats --interval 0'):
   x = re.search("CPU[ ].{0,50}[]][ ]", str(path))
   out[0] = x.group()
   y = re.search("GR3D_FREQ.{0,5}[%].{0,5}[ ]", str(path))
   out[1] = y.group()
   z = re.search("RAM[ ].{0,10}MB", str(path))
   out[2] = z.group()
   lbl.configure(text=out[0] + '\n' + out[1] + '\n' + out[2])
   window.update()
#   print(out[0] + '\n' + out[1] + '\n' + out[2])
btn = Button(window, text="Start", command=clicked)
btn.grid(column=0, row=0)
btn2 = Button(window, text="Stop", command=stopall)
btn2.grid(column=0, row=1)
btn3 = Button(window, text="Kill", command=kill)
btn3.grid(column=0, row=2)
window.mainloop()



