import os 
import sys
import requests
import pyrebase
import setting
import datetime
import json 
from rich import print as rprint
import effect
import getpass 


# dòng này đầu tiên nhằm load firebase config
firebase = pyrebase.initialize_app(setting.firebaseConfig)
auth = firebase.auth()
db = firebase.database()


# hàm tạo tài khoản
def createAccount(email, password):
    try:
        code = auth.create_user_with_email_and_password(email, password)
        print('Account has been created, please verify.')
        auth.send_email_verification(code.get('idToken'))
        tempData = {
            "email": email,
            "timeJoin": str(datetime.datetime.now()),
        } 
        db.child('/users/' + code['localId']).set(tempData, code['idToken'])
        return True
    except:
        print('Fail when create new account')
        return False

def signinAccount(email, password):
    try:
        code = auth.sign_in_with_email_and_password(email, password)
        f = open('config.json', 'wt')
        f.write(json.dumps(auth.current_user))
        f.close()
        txt = 'You have signed in with account {}'
        print(txt.format(email))
        return True 
    except:
        print('An error occurred while signin.')
        return False

def resetPassword(email):
    try:
        code = auth.send_password_reset_email(email)
        print('Done')
        return True
    except:
        print('Error')
        return False
def signoutAccount():
    pass
def userStatus():
    if auth.current_user == None:
        print('No account exists')
    else:
        txt = """Email: {}
ID: {}"""
        print(txt.format(auth.current_user['email'], auth.current_user['localId']))
                


# chương trình bắt đầu chạy từ đây

# in ra intro logo

if len(sys.argv) >= 2:
    pass 
else:
    effect.intro()
    command = ''
    strinput = 'home@spinel>'
    while True:
        command = input(strinput)
        if command == 'exit':
            break
        elif command == '':
            pass
        elif command =='help':
            effect.fhelp()
        elif (command == 'cls') | (command == 'clear'):
            effect.clearscreen()
        elif (command == 'signin') | (command == '-si'):
            print('Sign in to Spinel')
            email = input('Email:')
            password = getpass.getpass('Password:')
            signinAccount(email, password)
        elif (command == 'createAccount') | (command == '-ca'):
            print('Create Spinel account')
            email = input('Email:')
            password = getpass.getpass('Password:')
            check = input('Do you agree to the terms? (Y/n):')
            if (check == 'Y') | (check == 'y'): 
                createAccount(email, password)
                password = email  = ''
            else:
                pass
        elif (command == 'user'):
            # print(auth.current_user)
            userStatus()
        else:
            print('Unknow command. Type help to see more')
