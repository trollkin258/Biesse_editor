import os
from os import *
import easygui
import shutil, glob
from file_pause import pause

current_project = ''
current_file = ''
new_x = ''
new_y = ''
new_name = ''

def pick_projectfile():
    global current_project
    project_path = '/home/eric/Documents/VS-code/vs-python/Program_files/Project_files/'

    folders = []
    #r = root, d = directories, f = files
    for r, d, f in os.walk(path):
        for folder in d:
            folders.append(os.path.join(r, folder))

    for f in folders:
        print(f)

    
            
def pick_file():
    global current_file
    current_file = easygui.fileopenbox(msg='Select drill program', default=r'Program_files/Drilling_programs/*.bpp', title='Pick program')

def user_input():
    global new_x
    global new_y

    i=0
    a=0

    while (i != 1):  
        new_x = input('Enter X value for program: ')

        try:
            float(new_x)
            i=1
        except ValueError:
            print('This is not a number')

    while (a != 1):  
        new_y = input('Enter Y value for program: ')

        try:
            float(new_y)
            a=1
        except ValueError:
            print('This is not a number')

    print(new_x + 'X' + new_y)   

def resize_file():
    new_name = ' '
    current_new_file = new_name
    y = 'PAN=LPY|379||4|'
    x = 'PAN=LPX|762||4|'


    f = open(current_new_file,'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(y,'PAN=LPY|' + new_y + '||4|')

    f = open(current_new_file,'w')
    f.write(newdata)
    f.close()

    f = open(current_new_file,'r')
    filedata = f.read()
    f.close()

    newdata = filedata.replace(x,'PAN=LPX|' + new_x + '||4|')

    f = open(current_new_file,'w')
    f.write(newdata)
    f.close()
   

def copy_file():
    source = current_file        
    basedir = current_project
    global new_name

     # I use absolute path, case you want to move several dirs.
    old_name = source

    # Separate base from extension
    base, extension = os.path.splitext(source)

    # Initial new name
    new_name = os.path.join(basedir, base, source)

    new_name = os.path.join(basedir,base, base + new_x + 'X' + new_y + extension)
    shutil.copy(old_name, new_name)

    resize_file()

    #print('New name is: ', new_name)

    shutil.move(new_name, current_project)

def repeat():
    i = 0
    while (i != 1):
        repeat_again = ''

        print('Enter (1) To create a new project, (2) To add another program to the current project, and (3) Exit to main')
        repeat_again = input('Enter: ')

        if repeat_again == '1':
            i = 1
            new_project()
        elif repeat_again == '2':
            i = 1
            add_to_project()
        elif repeat_again == '3':
            i = 1
            pause()
            print('Exiting to main menu')
            pass
        else:
            print(repeat_again + ': is not a valid option.')
            pause()
            pass

def new_project():
    createnewprojectfile()
    pick_file()
    user_input()
    copy_file()
    repeat()

def add_to_project():
    pick_file()
    user_input()
    copy_file()
    repeat()


pick_projectfile()