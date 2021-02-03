from tkinter import *
from subprocess import Popen, PIPE
import subprocess
import re
window = Tk()
window.title("test")
window.geometry('492x200')
lbl = Label(window, text="000%@0000")
lbl.grid(sticky = W, column=0, row=9)
lbl0 = Label(window, text="000%@0000")
lbl0.grid(sticky = W, column=0, row=1)
lbl1 = Label(window, text="000%@0000")
lbl1.grid(sticky = W, column=0, row=2)
lbl2 = Label(window, text="000%@0000")
lbl2.grid(sticky = W, column=0, row=3)
lbl3 = Label(window, text="000%@0000")
lbl3.grid(sticky = W, column=0, row=4)
out = ['a','b','c']
def stopall():
 subprocess.Popen.kill(process)
 window.mainloop()
def kill():
 sys.exit()
 quit()
 exit()
process = subprocess.Popen('sudo tegrastats --interval 1000', stdout=PIPE, shell=True)
def run(command):
 window.update()
 process = subprocess.Popen(command, stdout=PIPE, shell=True)
 while True:
  line = process.stdout.readline().rstrip()
  if not line:
   break
  yield line
  window.update()
def clicked():
 window.update()
 while 1 == 1 :
  for path in run('sudo tegrastats --interval 1000'):
   x = re.search("CPU[ ].{0,50}[]][ ]", str(path))
   out[1] = x.group()
   y = re.search("GR3D_FREQ.{0,5}[%].{0,5}[ ]", str(path))
   out[0] = y.group()
   z = re.search("RAM[ ].{0,10}MB", str(path))
   out[2] = z.group()
   replaced = out[1].replace('CPU [', '').replace(' ]', '').replace(']', '').split(',')
#   lbl.configure(text=out[0] + '\n' + str(replaced) + '\n' + out[2] + '\n' + "000%@0000")
   lbl.configure(text="000%@0000")
   lbl0.configure(text=replaced[0])
   lbl1.configure(text=replaced[1])
   lbl2.configure(text=replaced[2])
   lbl3.configure(text=replaced[3])
#   lbl.configure(text=out[0] + '\n' + out[1] + '\n' + out[2] + '\n' + "000%@0000")

   print(replaced)
btn = Button(window, text="Start", command=clicked)
btn.grid(column=0, row=0)
btn2 = Button(window, text="Stop", command=stopall)
btn2.grid(column=1, row=0)
btn3 = Button(window, text="Kill", command=kill)
btn3.grid(column=2, row=0)
window.mainloop()



