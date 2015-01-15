''' Project:      Homework 6 (MalaveRafaelHomework05Sec02.py)
    Name:         Rafael Malave
    Date:         12/08/14
    Description:  This program will allow the user to click on five
    squares and a random dice will appear on each of the squares and
    a result will display the total value of the dice
'''

from graphics import *
from os import path


def is_above_poverty(lst_family):
    ''' This function will return True if the family is above
        the povery level '''

    ## If family with no family members ##
    if int(lst_family[1]) <= 0:
        print('Invalid number of family members', lst_family[1])
        return False

    return not is_poor(lst_family)


def is_poor(lst_family):
    '''This function returns True if the at or below the poverty
       level, False otherwise '''

    int_income_poor = 0

    ## If family with no family members ##
    if int(lst_family[1]) <= 0:
        print('Invalid number of family members', lst_family[1])
        return False

    ## Calculate the family income ##
    if lst_family[3] == 'HI':
        int_income_poor = 10700 + 3660 * (int(lst_family[1]) - 1)

    elif lst_family[3] == 'AK':
        int_income_poor = 11630 + 3980 * (int(lst_family[1]) - 1)

    else:
        int_income_poor = 9310 + 3180 * (int(lst_family[1]) - 1)

    # print('family ID {0}, n members {1}, income {2} state {3}, '
    #         'calc pov in {4}'.format(lst_family[0], lst_family[1],
    #             lst_family[2], lst_family[3], int_income_poor))

            ## Check if the family is at or below poverty level ##
    if int(lst_family[2]) <= int_income_poor:
        return True

    else:
        return False


def generate_report_1(lst_master, lbl_header, lbl_report, win):
    '''This function will write to a file all the families that
       fall below the Poverty level'''

    # Clear report text
    lbl_report.setText('')
    str_state = ''
    int_income_poor = 0

    str_file_name = 'report1.txt'
    with open(str_file_name, 'w') as out_file:
        for lst_family in lst_master:
            if lst_family is None:
                print('lst_family is None')
                continue

            if is_poor(lst_family):
                out_file.write('{}\n'.format(lst_family[0]))

    lbl_header.setText('Generated report file: report1.txt')


def generate_report_2(int_box_value, lst_master, lbl_header, lbl_report, win):
    '''This function will write in the window all the families
       that are above the Poverty level'''

    # Familes per line limit to four
    int_fpl = 0

    # Clear report text
    lbl_report.setText('')

    for lst_family in lst_master:

        if is_above_poverty(lst_family):

            if int_fpl == 3:
                lbl_report.setText(lbl_report.getText() + '\n' + str(lst_family[0]))
                int_fpl = 1

            else:
                lbl_report.setText(lbl_report.getText() + ' ' +  str(lst_family[0]))
                int_fpl += 1

    lbl_header.setText('Generated report 2')


def generate_report_3(int_box_value, lst_master, lbl_header, lbl_report, win):
    ''' This function will print the Percentage of families below poverty level
    '''

    int_income_poor = 0

    for lst_family in lst_master:
        if is_poor(lst_family):
            int_income_poor += 1

    int_percent = len(lst_master) / int_income_poor
    lbl_report.setText('Percentage of families below poverty level: ' +
                       str(int_percent) + '%')

    lbl_header.setText('Generated report 3')


def generate_report_4(lst_master, lbl_header, lbl_report, win):
    '''This function will write to a file all the families data
       and write next to each family if it falls below the Poverty level'''

    # Clear report text
    lbl_report.setText('')

    str_file_name = 'report4.txt'
    with open(str_file_name, 'w') as out_file:
        for lst_family in lst_master:

            if is_poor(lst_family):
                out_file.write('{} Below Poverty'
                               ' Level\n'.format(' '.join(lst_family)))

            else:
                out_file.write('{}\n'.format(' '.join(lst_family)))

    lbl_header.setText('Generated report file: report4.txt')


def sanitize_list(lst):
    '''This function will remove all elements from the list'''

    # As items are removed from the list, it's length is reduced
    # Account for this by always removing item 0
    for i in range(len(lst)):
        x = lst[0]
        lst.remove(x)


def import_data_file(int_box_value, input_entry, lst_raw, lbl_header, win):
    '''This function will take the file from the entry box '''

    lbl_header.setText('')

    int_ret_val = -1

    # Did user specify filename?
    if len(input_entry.getText()) == 0:
        lbl_header.setText('Error: No file specified')

    # Is filepath valid?
    elif not path.exists(input_entry.getText()):
        lbl_header.setText('Error: file does not exist')

    # Verify it is indeed a file (ie not a directory)
    elif not path.isfile(input_entry.getText()):
        lbl_header.setText('Error: is not a file')

    # All checks passed, import file contents!
    else:
        lbl_header.setText('Successfully loaded file!')
        with open(input_entry.getText(), 'r') as in_file:
            for line in in_file:
                lst_raw.append(line)

            in_file.close()

        int_ret_val = 0

    return int_ret_val


def is_lower_button_clicked(int_box_value, click_xy, int_button_num, win):
    ''' This function will check if one of the lower buttons was clicked '''

    int_upper_left_x = calc_button_coord(int_box_value, int_button_num,
                                         2, win)
    int_upper_left_y = calc_button_coord(int_box_value, int_button_num,
                                         3, win)
    int_lower_right_x = calc_button_coord(int_box_value, int_button_num,
                                          0, win)
    int_lower_right_y = calc_button_coord(int_box_value, int_button_num,
                                          1, win)

    if (click_xy.getX() >= int_upper_left_x and
            click_xy.getX() <= int_lower_right_x and
            click_xy.getY() >= int_upper_left_y and
            click_xy.getY() <= int_lower_right_y):
        return True

    else:
        return False


def is_import_clicked(int_box_value, click_xy, win):
    '''This function will check if the import button was clicked '''

    int_upper_left_x = calc_button_coord(int_box_value, 4, 2, win)
    int_upper_left_y = int_box_value
    int_lower_right_x = calc_button_coord(int_box_value, 4, 0, win)
    int_lower_right_y = int_box_value * 1.5

    if (click_xy.getX() >= int_upper_left_x and
            click_xy.getX() <= int_lower_right_x and
            click_xy.getY() >= int_upper_left_y and
            click_xy.getY() <= int_lower_right_y):
        return True

    else:
        return False


def get_clicked(int_box_value, click_xy, win):
    '''This function will return the button number for the clicked button or -1 if
       no button was clicked
       return values:
       1: Report 1 button
       2: Report 2 button
       3: Report 3 button
       4: Report 4 button
       5: Exit button
       6: Import button
       -1: No button '''
    # check if import button was clicked
    if is_import_clicked(int_box_value, click_xy, win):
        return 6

    # Check if one of the lower buttons was clicked and return its value
    for i in range(1, 6):
        if is_lower_button_clicked(int_box_value, click_xy, i, win):
            return i

    # No button was clicked
    return -1


def calc_button_coord(int_box_value, int_button_num, int_coord_type, win):
    ''' This function will give us the coordinates of the buttons
        int_coord_type:
        0: Lower Right X
        1: Lower Right Y
        2: Upper Left X
        3: Upper Left Y
        4: Center X coordinates
        5: Center Y coordinates '''

    int_value = -1

    if int_button_num < 1 or int_button_num > 5:
        print('calc_button_coord: Invalid int_button_num {}'
                .format(int_button_num))
        return -1

    # 0: Lower Right X
    if int_coord_type == 0:
        int_value = (int_button_num * int_box_value * 2 +
                int_button_num * int_box_value)

        # 1: Lower Right Y
    elif int_coord_type == 1:
        int_value = win.getHeight() - int_box_value

    # 2: Upper Left X
    elif int_coord_type == 2:
        int_value = (int_button_num * int_box_value +
            (int_button_num - 1) * int_box_value * 2)

    # 3: Upper Left Y
    elif int_coord_type == 3:
        int_value = win.getHeight() - (2 * int_box_value)

    # 4: Center x button coordinates
    elif int_coord_type == 4:
        int_upper_left_x = calc_button_coord(int_box_value, int_button_num,
            2, win)
        int_lower_right_x = calc_button_coord(int_box_value, int_button_num,
            0, win)
    # Use midpoint formula to calculate center x
        int_value = (int_upper_left_x + int_lower_right_x) / 2

    # 5: Center y coordinates
    elif int_coord_type == 5:
        int_upper_left_y = calc_button_coord(int_box_value, int_button_num,
            3, win)
        int_lower_right_y = calc_button_coord(int_box_value, int_button_num,
            1, win)

    # Use midpoint formula to calculate center y
        int_value = (int_upper_left_y + int_lower_right_y) / 2

    else:
        print('calc_button_coord: Invalid int_coord_type {}'
                .format(int_coord_type))
        int_value = -1

    return int_value


def draw_import_button(int_box_value, win):
    '''This functin will draw and import button next to the
       entry box '''

    int_upper_left_x = calc_button_coord(int_box_value, 4, 2, win)
    int_upper_left_y = int_box_value
    int_lower_right_x = calc_button_coord(int_box_value, 4, 0, win)
    int_lower_right_y = int_box_value * 1.5

    # Use midpoint formula to calculate center x
    int_center_x = (int_upper_left_x + int_lower_right_x) / 2

    # Use midpoint formula to calculate center y
    int_center_y = (int_upper_left_y + int_lower_right_y) / 2


    btn_import = Rectangle(Point(int_upper_left_x, int_upper_left_y),
            Point(int_lower_right_x, int_lower_right_y))
    btn_import.draw(win)

    lbl_import = Text(Point(int_center_x, int_center_y), 'Import')
    lbl_import.draw(win)


def draw_lower_button(int_box_value, int_button_num, win):
    '''This function will draw a lower button '''

    if int_button_num < 1 or int_button_num > 5:
        print('draw_lower_button: Invalid int_button_num {}'
                .format(int_button_num))
        return -1

    int_upper_left_x = calc_button_coord(int_box_value, int_button_num,
            2, win)
    int_upper_left_y = calc_button_coord(int_box_value, int_button_num,
            3, win)
    int_lower_right_x = calc_button_coord(int_box_value, int_button_num,
            0, win)
    int_lower_right_y = calc_button_coord(int_box_value, int_button_num,
            1, win)
    int_center_x = calc_button_coord(int_box_value, int_button_num, 4, win)

    int_center_y = calc_button_coord(int_box_value, int_button_num, 5, win)

    btn_lower = Rectangle(Point(int_upper_left_x, int_upper_left_y),
            Point(int_lower_right_x, int_lower_right_y))
    btn_lower.draw(win)

    if int_button_num != 5:
        lbl_label = Text(Point(int_center_x, int_center_y), 'Report ' +
                str(int_button_num))
    else:
        lbl_label = Text(Point(int_center_x, int_center_y), 'Exit')

    lbl_label.draw(win)

    return 0


def draw_elements(int_box_value, int_button_type, win):
    ''' Use this function to draw the buttons on the window
        button type vlues
        Reports = 0
        Exit    = 1
        Import  = 2'''

    if int_button_type < 0 or int_button_type > 2:
        print('draw_elements: Invalid button type', int_button_type)
        return None

    if (int_box_value <= 0 or int_box_value > win.getWidth()
            or int_box_value > win.getHeight()):
        print('draw_elements: Invalid int_box_value value', int_box_value)
        return None

    # Reports = 0
    if int_button_type == 0:
        for i in range(1, 5):
            draw_lower_button(int_box_value, i, win)

    # Exit = 1
    elif int_button_type == 1:
        draw_lower_button(int_box_value, 5, win)

    # Import = 2
    elif int_button_type == 2:
        draw_import_button(int_box_value, win)

    else:
        print('Imposible!!')

    return None


def main():

    # standard value for creating buttons, windows, etc
    int_box_value = 40

    win = GraphWin('Poverty Guidelines', int_box_value * 16, int_box_value * 10)
    win.setBackground('white')

    # Draw report buttons
    draw_elements(int_box_value, 0, win)
    # Draw exit button
    draw_elements(int_box_value, 1, win)
    # Draw import button
    draw_elements(int_box_value, 2, win)
    # Draw entry box
    int_entry_ulx = calc_button_coord(int_box_value, 1,
                                      2, win)
    int_entry_uly = int_box_value
    int_entry_center_x = int_entry_ulx + 4 * int_box_value
    int_entry_center_y = int_entry_uly + int_box_value / 4
    input_entry = Entry(Point(int_entry_center_x, int_entry_center_y),
                        35)
    input_entry.draw(win)

    # Create file status labels
    int_fstat_ulx = calc_button_coord(int_box_value, 1,
                                      2, win)
    int_fstat_center_x = int_fstat_ulx + 4 * int_box_value
    int_fstat_center_y = 0.5 * int_box_value

    # Labels to use on the generate_report functions
    lbl_header = Text(Point(int_fstat_center_x + 1.28 * int_box_value,
                            int_fstat_center_y),
                      'Note: Master list is sanitized when new data files'
                      'are imported.')

    lbl_header.setTextColor('red')
    lbl_header.draw(win)

    # Draw report 1 description
    Text(Point(int_box_value * 5.95, int_box_value * 2.5),
         'Report 1: Write families that fall below poverty level'
         ' to a file').draw(win)

    # Draw report 2 description
    Text(Point(int_box_value * 4.98, int_box_value * 3),
         'Report 2: Display families above the poverty'
         ' level').draw(win)

    # Draw report 3 description
    Text(Point(int_box_value * 5.48, int_box_value * 3.5),
         'Report 3: Display the % of families'
         ' below poverty level').draw(win)

    # Draw report 4 description
    Text(Point(int_box_value * 7.78, int_box_value * 4),
         'Report 4: Write families to a file '
         'and indicate if they fall below the'
         ' poverty level').draw(win)

    lbl_report = Text(Point(int_box_value * 5, int_box_value * 6), '')
    lbl_report.setTextColor('green')
    lbl_report.draw(win)

    # Create a raw list and a master data list of sublists
    lst_master = []
    lst_raw = []

    import_success = -1

    while 1:
        click_xy = win.getMouse()

        int_button_num = get_clicked(int_box_value, click_xy, win)

        # No button was clicked
        if int_button_num == -1:
            continue

        # Check for report 1 button
        elif int_button_num == 1:
            if import_success == 0:
                generate_report_1(lst_master, lbl_header, lbl_report, win)

            # Check for report 2 button
        elif int_button_num == 2:
            if import_success == 0:
                generate_report_2(int_box_value, lst_master, lbl_header,
                                  lbl_report, win)

            # Check for report 3 button
        elif int_button_num == 3:
            if import_success == 0:
                generate_report_3(int_box_value, lst_master, lbl_header,
                                  lbl_report, win)

            # Check for report 4 button
        elif int_button_num == 4:
            if import_success == 0:
                generate_report_4(lst_master, lbl_header, lbl_report, win)

            # Check for exit button
        elif int_button_num == 5:
            break

            # Check for import button
        elif int_button_num == 6:

            # Sanitize the raw list
            sanitize_list(lst_raw)

            # Sanitize the master list
            # This provides support for a user loading other data files
            # without having to restart the program. If the master list
            # isn't sanitized it would contain previous family data that
            # would corrupt report results
            for i in range(len(lst_master)):
                # Always extract 0th index. As the family lists are removed from
                # the master list, the len() of master list decreases, so this
                # prevents stepping of the edge of the array
                lst_family = lst_master[0]
                sanitize_list(lst_family)
                lst_master.remove(lst_family)

            # Set import success value, this will dictate whether the program
            # will allow reports to be generated. ie No file data - no reports
            import_success = import_data_file(int_box_value, input_entry,
                                              lst_raw, lbl_header, win)


            #print('main: import_success = ', import_success)
            if import_success == 0:
                # Given successful file import
                # create master list of sublists
                for i in range(len(lst_raw)):
                    lst_master.append(lst_raw[i].split())

    # Program ended, close window
    win.close()


main()
