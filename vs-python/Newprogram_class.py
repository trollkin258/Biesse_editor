#Main class for creating new program files.

class newprogram:
    def def __init__(self, origin_file, current_project, new_height_y, new_width_x):
        self.origin_file = origin_file
        self.current_project = current_project
        self.new_height_y = new_height_y
        self.new_width_x = new_width_x
        self.new_program_name = new_width_x + 'X' + new_height_y + ' ' + origin_file
      

program_1 = newprogram()

print(program_1)

program_1.origin_file = ' '
program_1.current_project = ' '
program_1.new_height_y = ' '
program_1.new_width_x = ' '
program_1.new_program_name = ' '