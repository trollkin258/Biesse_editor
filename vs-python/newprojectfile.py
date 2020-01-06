import os
from os import path
import easygui
import shutil, glob
from file_pause import pause
import config

current_project = ""
current_file = ""
new_x = ""
new_y = ""
new_name = ""


def createnewprojectfile():
    global current_project


    errorcheck = 0
    while (errorcheck != 1):
        newfolder = input('Enter project name: ')
        print(newfolder)

        path = newfolder
        if not os.path.exists(os.path.join('Program_files/Project_files',newfolder)):
            os.makedirs(os.path.join('Program_files/Project_files',newfolder))
            print('New project file created')
            errorcheck = 1
            
            current_project = 'Program_files/Project_files/'+ newfolder
            print(current_project)
        else:
            print(newfolder+' all ready exists, enter a new name.')

def pick_projectfile():
    global current_project

    project_path = 'Program_files/Project_files'

    project_files = [x[0] for x in os.walk(project_path)]

    project_files_clean = project_files[1:]

    #print(*project_files)

    msg='Select a project file'
    title='Project files'
    choices=project_files_clean

    choice = easygui.choicebox(msg, title, choices)

    current_project = choice
    
    if choice != "":
        pass
    else:
        return

    print(current_project)
            
def pick_file():
    global current_file
    current_file = easygui.fileopenbox(msg='Select drill program', default=r'Program_files/Drilling_programs/*')
    if current_file != "":
        pass
    else:
        return

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
    #todo change to gui and loop back to main menu on exit
    i = 0
    while (i != 1):
        repeat_again = ''

        print('Enter (1) To add another program to the current project, and (2) Exit to main')
        repeat_again = input('Enter: ')

        #if repeat_again == '1':
        #    i = 1
        #    new_project()
        if repeat_again == '1':
            i = 1
            add_to_project()
        elif repeat_again == '2':
            i = 1
            pause()
            print('Exiting to main menu')
            return
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

def add_to_project_existing():
    pick_projectfile()
    if current_project == "":
        return
    else:
        pick_file()
        if current_file !    = "":
            return
        else:
            user_input()
            copy_file()
            repeat()


#pick_projectfile()