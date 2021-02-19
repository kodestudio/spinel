from rich import print as rprint 
import os
import subprocess

def intro():
    txt = """
                        $$\                     $$\ 
                    \__|                    $$ |
 $$$$$$$\  $$$$$$\  $$\ $$$$$$$\   $$$$$$\  $$ |
$$  _____|$$  __$$\ $$ |$$  __$$\ $$  __$$\ $$ |
\$$$$$$\  $$ /  $$ |$$ |$$ |  $$ |$$$$$$$$ |$$ |
 \____$$\ $$ |  $$ |$$ |$$ |  $$ |$$   ____|$$ |
$$$$$$$  |$$$$$$$  |$$ |$$ |  $$ |\$$$$$$$\ $$ |
\_______/ $$  ____/ \__|\__|  \__| \_______|\__|
          $$ |                                  
          $$ |                                  
          \__|                                  
    """
    print(txt)

def fhelp():
    print("""
Welcome to Spinel. Try 'spinel [param]'
Some param can use:
    help (-h): give help
    createAccount (-ca) [email] [pass] [username]: create new account with email and password
    signin (-si) [email] [password]: signin to local Spinel
    signout (-so): signout Spinel
    join (-j) [roomID]: join to a secure chat room with ID
    """)

def clearscreen():
    if (os.name == 'posix'):
        #subprocess.call('clear')
        os.system('clear')
    else:
        #subprocess.call('cls')
        os.system('cls')