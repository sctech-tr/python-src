import time
import sys
print("1 - snake360")
print("2 - pyRPS")
print("3 - explorer")
print("4 - pongPLUS")
selection = input("which game would you like to ban your account from? ")
if selection == "1":
    with open("snkconf.ini", "w") as file:
        file.write("bnfrmsnk260rbxjfnsk7483h")
        print("successfully banned from snake360.")
        sys.exit()
elif selection == "2":
    with open("rpsconf.ini", "w") as file:
        file.write("banwpsconfrpsrbxfps")
        print("successfully banned from pyRPS.")
        sys.exit()
elif selection == "3":
    with open("expconf.ini", "w") as file:
        file.write("hdhfnsjwjfjefhbanexp")
        print("successfully banned from explorer.")
        sys.exit()
elif selection == "4":
    with open("popconf.ini", "w") as file:
        file.write("sdscardsdplusponbanbanned")
        print("successfully banned from pongPLUS.")
        sys.exit()
else:
    print("seems like you entered an invalid value. don't worry, more games are coming soon!")
    time.sleep(3)
    sys.exit()