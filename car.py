# car game

def command_help():
    print("""start - to start the car
stop - to stop the car
quit - to quit""")

car_started = False
command = ""
while True:

    command = input("> ").lower()
    if command == "help":
        command_help()
    elif command == "start":
        if car_started:
            print("Car is already started???")
        else:
            car_started = True
            print("Car started")
    elif command == "stop":
        if not car_started:
            print("Car is already stopped???")
        else:
            car_started = False
            print("Car stopped")
    elif command == "quit":
        break
    else:
        print("I dom't understand that ...")

