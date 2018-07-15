#|==============================================================|#
# Made by IntSPstudio
# PTIA Plugin
# Thank you for using this plugin!
# Version: 0.0.1.20181507
# ID: 980007009
#
# Twitter: @IntSPstudio
#|==============================================================|#

#LIBRARIES
import os
from platform import system as osp
#CHECK OS
osccmd =""
if osp() == "Windows":
	osccmd ="cls"
else:
	osccmd ="clear"
#OPERATING SYSTEM SETTINGS
def clearScreen():
	os.system(osccmd)
#START MARKS
def defSet(args):
  clearScreen()
  print(args["settings"]["titlePrefix"])
  print(args["visuals"]["contentLine"])
#COM
def main(args):
  #SET
  stMark = args["visuals"]["stMark"]
  defSet(args)
  ap = args["pages"]
  #LOOP
  for i in range(1, len(ap)):
    bp = str(i)
    cp = str(ap[bp])
    bp = "%02d" % i #FORMAT
    dp = bp + stMark[2] + cp
    print(dp)
  return input(stMark)