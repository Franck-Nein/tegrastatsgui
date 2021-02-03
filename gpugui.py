from tkinter import *
from subprocess import Popen, PIPE
import re
window = Tk()
window.title("GPU")
window.geometry('45x45')
lbl0, lbl1 = Label(), Label()
lbl0.grid(column=0, row=0)
lbl1.grid(column=0, row=1)
def run(command):
 process = Popen(command, stdout=PIPE, shell=True)
 while True:line=process.stdout.readline().rstrip();yield line
for path in run('sudo tegrastats --interval 100'):gpu=re.search('GR3D_FREQ.{0,5}[%].{0,5}[ ]',str(path)).group().replace('GR3D_FREQ ','').replace('%@','% @').split(' ');lbl0.configure(text=gpu[0]);lbl1.configure(text=gpu[1]);window.update()
window.mainloop()
