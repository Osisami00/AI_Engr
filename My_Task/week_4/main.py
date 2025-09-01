# This is the module with CSV file path and user prompt
from pathlib import Path
import csv
# import file_ops
import os

def local_path():
    folder = Path('participant_pkg')
    return folder / 'participant.csv'



def participant_info():
    participant = {}
    try:    
        while True:
            name = input("Enter your name: ").strip().title()
            if name.isalpha() == False:
                print("Error! Enter a correct name.")
            else:    
                participant["name"] = name
                break

        while True:
            age = input(f"Dear {participant["name"]}, kindly enter your age: ")
        
            if int(age) <= 1 or int(age) > 120:
                print("That can't be your age. Enter your age")
            # if age.isdigit():
            #     print("Error! Age should be a number")
                participant["age"] = age
            else:
                break
        
        while True:
            phone_number = input("Enter your phone number: ")
            if len(phone_number) != 11:
                print("Phone number should be 11digits")
            elif phone_number.isalpha == True:
                print("Phone Number cannot be a letter")
                participant["phone_number"] = phone_number
            else:
                break
            
        while True:
            track =input("Enter your track: ").strip().upper()
            if track.isalpha == False:
                print("Letter should be in words. Try again.")
                participant["track"] = track
            else: 
                break
    except ValueError as e:
        print(e)

participant_info()





def partcipant_list(n):
    path = local_path()
    for i in range(n):
        participant_dic = participant_info()
        # file_ops.save_participant(path, participant_dic)
partcipant_list(2)




