
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



def user_input_XY():
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