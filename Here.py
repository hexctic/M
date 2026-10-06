## Hellow


import time
import os
import platform
import socket
import sqlite3

##################################################
## I'll attempt to test some class functionality #
## probably non-functional atm                   #
##################################################

####################################################
# Actual functional functions , for the most part  #
####################################################

current_dir = os.listdir("/workspaces/M")



def getting_size():
     os.sock



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
                
                ##size_check()##        
    
    
    def size_check():
        if  d != file_to_look_for:
            size = input("Size check ? y/n ")
            if size in ("y", "Y"):
                
                print("Checking the size...")


            else :
                print("Exiting ")
                print(f"Here's what I got : {list_of_found_file}")
        elif d != file_to_look_for :
            print("Could not find the file requested")
                 



    
                     
                     # Stops
    size_check()

         

getting_file_names()


########################################################
# Future SQLite database  connection for tracking      #
# purposes                                             #
########################################################

