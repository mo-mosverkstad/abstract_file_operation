import os
from file_framework import *

def cmd_shell():
    DIRECTORY = 1
    TEXTFILE = 2
    MODE_DIRECTORY = 'd-----   '
    MODE_ROOT_DIRECTORY = 'd-r---'
    MODE_TEXTFILE = '-a----   '
    listfiles = ['dir', 'ls']
    PROMPT = '>'
    DELIMITOR = '\\'
    status = 'C:' + DELIMITOR
    while True:
        inputs = input(status + PROMPT)
        if inputs in listfiles:
            the_list = os.listdir(status)
            print('Mode  ' + '   ' + 'Name')
            for item_name in the_list:
                content = item_name.split('.')
                if len(content) == DIRECTORY:
                    mode = MODE_DIRECTORY
                elif len(content) == TEXTFILE:
                    mode = MODE_TEXTFILE
                print(mode+'   '+item_name)
        elif inputs.startswith('cd '):
            directory = inputs[3:]
            all, counter = is_backward_directory(directory)
            if all:
                status = backward_change(status, counter)
            else:
                change_director = False
                try:
                    a = os.listdir(status+DELIMITOR+directory)
                    change_director = True
                except:
                    change_director = False
                if change_director:
                    status = status+DELIMITOR+directory
            
cmd_shell()