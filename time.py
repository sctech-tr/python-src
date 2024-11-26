import time
import datetime
import winsound
import keyboard
import sys

def get_char():
    char = None
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            char = event.name
            break
    return char

print("1 - stopwatch (s)")
print("2 - countdown (c)")
print("3 - exit (x)")
selection = input("what do you want to do? press the key associated with the action you want: ")

while True:
    char = get_char()
    if char == 's':
        starttime = time.time()
        lasttime = starttime
        lapnum = 1
        value = ""

        print("press enter for each lap. type 'q' and press enter to stop.")

        while True:
            value = input()
            if value.lower() == "q":
                break
            laptime = round((time.time() - lasttime), 2)
            totaltime = round((time.time() - starttime), 2)
            print("lap no: " + str(lapnum))
            print("total time: " + str(totaltime))
            print("lap time: " + str(laptime))
            print("*" * 20)
            lasttime = time.time()
            lapnum += 1
    elif char == 'c':
        def countdown(h, m, s):
            total_seconds = h * 3600 + m * 60 + s

            while total_seconds > 0:
                timer = datetime.timedelta(seconds=total_seconds)
                print(timer, end="\r")
                time.sleep(1)
                total_seconds -= 1

            print("the countdown is at zero seconds!")
            winsound.Beep(1000, 1000)
            time.sleep(2)

        h = int(input("enter the time in hours: "))
        m = int(input("enter the time in minutes: "))
        s = int(input("enter the time in seconds: "))
        countdown(h, m, s)
    elif char == 'x':
        sys.exit()
    else:
        print("restarting...")
        time.sleep(1)
