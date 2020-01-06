from filecheck import filechecking
from newprojectfile import new_project
from newprojectfile import add_to_project_existing
from file_pause import pause


#print ("hello world")

Yes = ["yes", "Yes", "y", "Y", "YES", "YeS"]

menu = 0
while (menu != 1):
    filechecking()
    print("Title")
    print("Instructions")
    print("option 1: Create new job: Create new project with drilling programs")
    print("option 2: Add to existing project: Description")
    print("option 3: Edit job: Description")
    print("option 4: Import list: Description")
    print("option 5: Edit drilling parts list: Description")
    print("option 6: Exit program")
    
    menuinput = input("Enter a numbered option from above: ")
    print(menuinput)
    
    if menuinput == "1":
        print("Option 1:Create project and add files.")
        new_project()
        pause()
   
    elif menuinput == "2":
        print("Option 2: Add files to existing project.")
        add_to_project_existing()
        pause()
    
    elif menuinput == "3":
        print("Option 1: this function is currently unavailable in this version.")
        pause()
   
    elif menuinput == "4":
        print("Option 1: this function is currently unavailable in this version.")
        pause()
        
    elif menuinput == "5":
        print("Option 1: this function is currently unavailable in this version.")
        pause()
        
    elif menuinput == "6":
        exit=input("Do you wish to exit the program: (Y/N)")
        
        if exit in Yes:
            menu=menu+1

        else:
            pass
    
    else:
        print(menuinput, " is not a valide option please select from the list.")
        pause()
        
