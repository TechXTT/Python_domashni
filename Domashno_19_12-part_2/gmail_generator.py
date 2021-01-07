import pyautogui
import sys
import time
import random
import string

def ext():
    print('Exiting...')
    sys.exit()

def open_edge():

    print('Opening Edge...')

    start_button = pyautogui.locateOnScreen('images/start_button.png')
    location = pyautogui.center(start_button)

    if not pyautogui.click(location):
        print('Opened start menu successfully!')
    else:
        print('Failed to open start menu!')
        exit()

    time.sleep(2)

    pyautogui.typewrite('edge')
    pyautogui.typewrite('\n')

    print('Edge is now open and running.')

def locate_gmail():
    time.sleep(3)

    print('Opening Gmail...')

    pyautogui.keyDown('ctrlleft')
    pyautogui.typewrite('a')
    pyautogui.keyUp('ctrlleft')
    pyautogui.typewrite(
        'https://accounts.google.com/SignUp?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ltmpl=default')
    pyautogui.typewrite('\n')

    time.sleep(6)

    print('Locating the form...')

    time.sleep(2)


def randomize(option,length):
    if length > 0:

        if option == '-p':
            string.characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+'
        elif option == '-l':
            string.characters = ['Dave', 'Steve', 'John', 'Grays', 'Jude', 'Martin', 'Steven', 'Alexander', 'Ivan',
                                   'Anatol']
        elif option == '-n':
            string.characters = '1234567890'
        elif option == '-m':
            string.characters = 'JFMASOND'
        elif option == '-u':
            string.characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if option == '-d':
            gened_info = random.randint(1, 28)
        elif option == '-y':
            gened_info = random.randint(1950, 2000)
        elif option == '-l':
            gened_info = random.choice(string.characters)
        else:
            gened_info = ''
            for counter in range(0, length):
                gened_info = gened_info + random.choice(string.characters)

        return gened_info

    else:
        print('No valid length specified...')
        exit()

def gen_info():
    print('Generating credentials...')

    first_name = randomize('-l', 7)
    pyautogui.typewrite(first_name)
    pyautogui.typewrite('\t')
    time.sleep(3)
    last_name = randomize('-l', 8)
    pyautogui.typewrite(last_name)
    pyautogui.typewrite('\t')
    time.sleep(3)
    print('Name:' ,first_name, last_name)

    username = randomize('-u', 10)
    pyautogui.typewrite(username)
    pyautogui.typewrite('\t')
    time.sleep(3)
    print('Username:', username)

    password = randomize('-p', 16)
    pyautogui.typewrite(password + '\t' + password + '\t\t')
    print('Password:', password)
    time.sleep(20)

    month = randomize('-m', 1)
    day = randomize('-d', 1)
    year = randomize('-y', 1)
    pyautogui.typewrite(month + '\t' + str(day) + '\t' + str(year) + '\t')
    print('Date of birth:', month, day, year)

    pyautogui.typewrite('R\t')
    print('Gender:Rather not say')
    pyautogui.typewrite('\t\t\t\t\n')


# Main function
if __name__ == '__main__':

    if open_edge():
        print('Failed to execute "open_edge" command.')
        exit()

    if locate_gmail():
        print('Failed to execute "locate_gmail" command.')
        exit()

    if gen_info():
        print('Failed to execute "gen_info" command.')
        exit()

    print('Done...')
    exit()
