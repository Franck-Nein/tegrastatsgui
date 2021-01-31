from subprocess import Popen, PIPE
import re
out = ['a','b','c']
def run(command):
 process = Popen(command, stdout=PIPE, shell=True)
 while True:
  line = process.stdout.readline().rstrip()
  if not line:
   break
  yield line

for path in run('sudo tegrastats'):
 x = re.search("CPU[ ].{0,50}[]][ ]", str(path))
 out[0] = x.group()
 y = re.search("GR3D_FREQ.{0,5}[%].{0,5}[ ]", str(path))
 out[1] = y.group()
 z = re.search("RAM[ ].{0,10}MB", str(path))
 out[2] = z.group()
 print(out[0] + '\n' + out[1] + '\n' + out[2])


