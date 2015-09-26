from litescope.software.dump import *

print("creating dump...")
dump = Dump()
for i in range(4):
	dump.add(DumpVariable("foo"+str(i), 2**i, [j for j in range(256)]))
pi = 3.1415
from math import cos, sin
dump.add(DumpVariable("sinus", 8, [128+128*sin(j/(2*pi*16)) for j in range(1024)]))
dump.add(DumpVariable("cosinus", 8, [128+128*cos(j/(2*pi*16)) for j in range(1024)]))

print("csv export test")
from litescope.software.dump.csv import CSVDump
CSVDump(dump).write("dump.csv")

print("python export test...")
from litescope.software.dump.python import PythonDump
PythonDump(dump).write("dump.py")

print("vcd export test...")
from litescope.software.dump.vcd import VCDDump
VCDDump(dump).write("dump.vcd")

print("sigrok export/import test...")
from litescope.software.dump.sigrok import SigrokDump
SigrokDump(dump).write("dump.sr")
SigrokDump(dump).read("dump.sr")
SigrokDump(dump).write("dump.sr")