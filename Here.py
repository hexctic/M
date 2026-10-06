## Hellow


import time
import os
import platform
import socket

##################################################
## I'll attempt to test some class functionality #
## probably non-functional atm                   #
##################################################



####################################################
# Actual functional functions , for the most part  #
####################################################

current_dir = os.listdir("/workspaces/M")



        
        
def getting_file_names():
    list_of_found_file = []
    dir_list = os.listdir()
    file_to_look_for = input("Give me a file to look for...")
     # print(d) leaving in for future testing purposes
    for d in dir_list:
            if d == file_to_look_for :
                print(f"Found the file called {d}...")
                time.sleep(.2)
                list_of_found_file.append(d)
            elif:
                print("Couldn't find it, try another one.")

                
                # print list_of_found_file also for future testing purposes .
                print(list_of_found_file)
                size = input("Size check ? y/n ")
                if size ==  "Y" or "y":
                     print("Checking the size")
                     ##checking the size starts
                else: 
                     print("Exiting")
                     
                     # Stops



            
getting_file_names()


########################################################
# Future SQLite database  connection for tracking      #
# purposes                                             #
########################################################

