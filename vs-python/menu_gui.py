from filecheck import filechecking
from newprojectfile import new_project
from newprojectfile import add_to_project_existing
from file_pause import pause
from easygui import *


main_menu_options = ["Instructions", "option 1: Create new job: Create new project with drilling programs",
"option 2: Add to existing project: Description", "option 3: Edit job: Description",
"option 4: Import list: Description", "option 5: Edit drilling parts list: Description", "option 6: Exit program"]
        

def menu():
    menu = 0
    while (menu != 1):
        filechecking()
        msg='Select a project option'
        title='Main Menu'
        choices=main_menu_options

        menuinput = choicebox(msg, title, choices)
        
        if menuinput == main_menu_options[0]:
            msgbox(msg="This selection is currantly under development", title="Intructions")

        elif menuinput == main_menu_options[1]:
            new_project()
            pause()
   
        elif menuinput == main_menu_options[2]:
            add_to_project_existing()
            pause()
    
        elif menuinput == main_menu_options[3]:
            print("Option 1: this function is currently unavailable in this version.")
            pause()
   
        elif menuinput == main_menu_options[4]:
            print("Option 1: this function is currently unavailable in this version.")
            pause()
        
        elif menuinput == main_menu_options[5]:
            print("Option 1: this function is currently unavailable in this version.")
            pause()
        
        elif menuinput == main_menu_options[6]:
            menu=menu+1
        else:
            return
            
            
#menu()

