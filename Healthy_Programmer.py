# -------------------------------- Healthy Programmer --------------------------------------
"""
Write a program to make a programmer healthy
Working hour: 9 AM to 5 PM
Water - water.mp3 - Every 1.5 hours 250 ml- Total 3.5 litres (3500ml) - Stop: Drank - save in log file with time stamp
Eyes - eyes.mp3 - Every 30 minutes - Stop: EyDone -  Save in log file with time stamp
Physical Exercise - physical.mp3 - Every 45 minutes - Stop: ExDone - save in log file with time stamp

Challenges: Time may overlap, so to avoid the collision, wait until one task is finished, then only move to another
For example: first finished drining water and then only eyes.

Rules: use Pygame module to play audio
Note: As M1 runs an issue, so I am importing os to play sound

Details of Program: office hour 9am to 5pm ho ra tyas samaya bich ma harek half and hour (30 minutes) ma program le
eyes ko ecercise garnu vanxa tyas paschat harek 45 minutes ma physical exercise garnu vanxa ra harek 1 and half hour
(1.5 hours) ma water piunu vanxa. """
import datetime
import os

# mp3 files location
water_mp3 = 'mp3files/water.mp3'
eyes_mp3 = 'mp3files/eyes.mp3'
physical_mp3 = 'mp3files/physical.mp3'

# Accessing local time
current_time = datetime.datetime.now()
now = current_time.strftime("%H:%M:%S")

# Infinite loop
while True:
    # 9:30 Am -> eyes exercise
    if now.__eq__("09:30:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter EyDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 9:45 Am -> physical exercise
    elif now.__eq__("09:45:00"):
        print("Please do the physical exercise !!!")
        while True:
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the physical exercise, Invalid Input !!!")
    # 10:00 Am -> eyes exercise
    elif now.__eq__("10:00:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 10:30 Am -> water, eyes, and physical exercise
    elif now.__eq__("10:30:00"):
        print("Please Drink a glass of water and do the eyes exercise and physical exercise respectively!!!")
        while True:
            # drink water first
            os.system("afplay " + water_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("Drank"):
                continue
            # eyes exercise
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                continue
            # physical exercise
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the exercises, Invalid Input !!!")
    # 11:00 Am -> eyes exercise
    elif now.__eq__("11:00:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 11:15 Am -> physical exercise
    elif now.__eq__("11:15:00"):
        print("Please do the physical exercise !!!")
        while True:
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the physical exercise, Invalid Input !!!")
    # 11:30 Am -> eyes exercise
    elif now.__eq__("11:30:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 9:30 Am -> water, eyes, and physical exercise
    elif now.__eq__("12:00:00"):
        print("Please Drink a glass of water and do the eyes exercise and physical exercise respectively!!!")
        while True:
            # drink water first
            os.system("afplay " + water_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("Drank"):
                continue
            # eyes exercise
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                continue
            # physical exercise
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the exercises, Invalid Input !!!")
    # 12:30 pm -> eyes exercise
    elif now.__eq__("12:30:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 12:45 pm -> physical exercise
    elif now.__eq__("12:45:00"):
        print("Please do the physical exercise !!!")
        while True:
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the physical exercise, Invalid Input !!!")
    # 13:00 pm -> eyes exercise
    elif now.__eq__("13:00:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 13:30 pm -> water, eyes, and physical exercise
    elif now.__eq__("13:30:00"):
        print("Please Drink a glass of water and do the eyes exercise and physical exercise respectively!!!")
        while True:
            # drink water first
            os.system("afplay " + water_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("Drank"):
                continue
            # eyes exercise
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                continue
            # physical exercise
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the exercises, Invalid Input !!!")
    # 14:00 pm -> eyes exercise
    elif now.__eq__("14:00:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 14:15 pm -> physical exercise
    elif now.__eq__("14:15:00"):
        print("Please do the physical exercise !!!")
        while True:
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the physical exercise, Invalid Input !!!")
    # 14:30 pm -> eyes exercise
    elif now.__eq__("14:30:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 15:00 pm -> water, eyes, and physical exercise
    elif now.__eq__("15:00:00"):
        print("Please Drink a glass of water and do the eyes exercise and physical exercise respectively!!!")
        while True:
            # drink water first
            os.system("afplay " + water_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("Drank"):
                continue
            # eyes exercise
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                continue
            # physical exercise
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the exercises, Invalid Input !!!")
    # 15:30 pm -> eyes exercise
    elif now.__eq__("15:30:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    # 15:45 pm -> physical exercise
    elif now.__eq__("15:45:00"):
        print("Please do the physical exercise !!!")
        while True:
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the physical exercise, Invalid Input !!!")
    # 16:00 pm -> water, eyes, and physical exercise
    elif now.__eq__("16:00:00"):
        print("Please do the eyes exercise !!!")
        while True:
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                break
            else:
                print("Finish do the eyes exercise, Invalid Input !!!")
    elif now.__eq__("16:30:00"):
        print("Please Drink a glass of water and do the eyes exercise and physical exercise respectively!!!")
        while True:
            # drink water first
            os.system("afplay " + water_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("Drank"):
                continue
            # eyes exercise
            os.system("afplay " + eyes_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("EyDone"):
                continue
            # physical exercise
            os.system("afplay " + physical_mp3)
            user_input = input("Enter ExDone if you are finished : ")
            user_input_ = user_input.lower()
            if user_input_.__eq__("ExDone"):
                break
            else:
                print("Finish do the exercises, Invalid Input !!!")
    elif now.__eq__("17:00:00"):
        print("Office Time Over !!!")
    elif now > "17:00:00":
        print("You can go home !!!")
        break
    else:
        print("You can program !!!")
        break
