import os
import sys
import time


snake360 = "snkconf.ini"
pyrps = "rpsconf.ini"
explorer = "expconf.ini"
pongplus = "popconf.ini"

print("1 - snake360")
print("2 - pyRPS")
print("3 - explorer")
print("4 - pongPLUS")
selection = input("which game would you like to unban your account from? ")
if selection == "1":
   if os.path.exists(snake360):
    os.remove(snake360)
    print("successfully unbanned from snake360.")
   else:
    print("you're already unbanned from snake360.")

elif selection == "2":
   if os.path.exists(pyrps):
    os.remove(pyrps)
    print("successfully unbanned from pyRPS.")
   else:
    print("you're already unbanned from pyRPS.")

elif selection == "3":
   if os.path.exists(explorer):
    os.remove(explorer)
    print("successfully unbanned from explorer.")
   else:
    print("you're already unbanned from explorer.")

elif selection == "4":
  if os.path.exists(pongplus):
    os.remove(pongplus)
    print("successfully unbanned from pongPLUS.")
  else:
    print("you're already unbanned from pongPLUS.")
else:
    print("invalid value")
    time.sleep(3)
    sys.exit()