import os 
import sys
import requests
import pyrebase
import setting
import datetime
import json 
from rich import print as rprint
import effect

# dòng này đầu tiên nhằm load firebase config
firebase = pyrebase.initialize_app(setting.firebaseConfig)
auth = firebase.auth()
db = firebase.database()

# hàm tạo tài khoản
def createAccount(email, password, name):
    try:
        code = auth.create_user_with_email_and_password(email, password)
        print('Account has been created, please verify.')
        auth.send_email_verification(code.get('idToken'))
        tempData = {
            "name": name,
            "email": email,
            "timeJoin": str(datetime.datetime.now()),
            "bio": ""
        } 
        db.child('/users').push(tempData, code['idToken'])
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
        print('Signin complete')
        return True 
    except:
        print('Signin errror')
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



# chương trình bắt đầu chạy từ đây

# in ra intro logo

if len(sys.argv) >= 2:
    pass 
else:
    effect.intro()
    command = ''
    while True:
        command = input('@spinel>')
        if command == 'exit':
            break
        elif command == '':
            pass
        elif command =='help':
            effect.fhelp()
        elif (command == 'cls') | (command == 'clear'):
            effect.clearscreen()
        else:
            print('Unknow command. Type help to see more')
