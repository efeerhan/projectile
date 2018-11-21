import math
import cmath
import turtle

def options():
    print('''
    initial angle                   -ia
    final angle                     -fa
    initial velocity                -iv
    final velocity                  -fv
    vertical change in distance     -vcd
    horizontal change in distance   -hcd
    acceleration due to gravity     -adg
    time interval                   -ti
    ''')


def eq_select_adg():
    print("which value is missing?")
    print('''
    final velocity                -fv
    time interval                 -ti
    vertical change in distance   -vcd
    ''')


def eq_select_fv():
    print("which value is missing?")
    print('''
    time interval                 -ti
    vertical change in distance   -vcd
    ''')


def eq_select_ti():
    print("which value is missing?")
    print('''
    final velocity                -fv
    vertical change in distance   -vcd
    ''')


def eq_select_iv():
    print("which value is missing?")
    print('''
    time interval                 -ti
    vertical change in distance   -vcd
    none                          -na''')


def eq_select_fa():
    print("which value is missing?")
    print('''
    time interval                 -ti
    vertical change in distance   -vcd''')


def eq_select_ia():
    print("which value is missing?")
    print('''
    time interval                 -ti
    vertical change in distance   -vcd
    none                          -na''')


def eq_select_vcd():
    print("which value is missing?")
    print('''
    time interval                 -ti
    final velocity                -fv''')


def eq_select_hcd():
    print("which value is missing?")
    print('''
    time interval                 -ti
    final velocity                -fv''')


rad_deg = str()
init_angle_rad_flt = float()
final_angle_rad_flt = float()


def rad_deg_initial_input():
    global init_angle_rad_flt
    print('initial angle units: (radians or degrees?)')
    try:
        rad_deg = input()
        while (rad_deg != 'radians' and
               rad_deg != 'degrees'):
            rad_deg = input('illegal input, try again: ')
    except (SyntaxError, ValueError) as err:
        rad_deg = input('illegal input, try again: ')
    while rad_deg == 'radians':
        try:
            init_angle_rad_flt = eval(input('initial angle (ratio without pi): '))
            init_angle_rad_str = str(init_angle_rad_flt)
            if init_angle_rad_flt * math.pi <= math.pi / 2:
                init_angle_rad_flt = init_angle_rad_flt * math.pi
                break
            elif len(init_angle_rad_str) == '1' and init_angle_rad_str != '1':
                init_angle_rad_flt = float(init_angle_rad_str)
                pass
            else:
                print('input too large (> pi/2)')
        except (SyntaxError, ValueError) as err:
            print('incorrect value, try again: ')
    while rad_deg == 'degrees':
        try:
            init_angle_flt = float(input('initial angle: '))
            if init_angle_flt <= 90:
                init_angle_rad_flt = math.radians(init_angle_flt)
                break
            else:
                print('input too large (> 90 degrees)')
        except (SyntaxError, ValueError) as err:
            print('incorrect value, try again: ')


def rad_deg_final_input():
    global final_angle_rad_flt
    print('final angle units: (radians or degrees?)')
    try:
        rad_deg = input()
        while (rad_deg != 'radians' and
               rad_deg != 'degrees'):
            rad_deg = input('illegal input, try again: ')
    except (SyntaxError, ValueError) as err:
        rad_deg = input('illegal input, try again: ')
    while rad_deg == 'radians':
        try:
            final_angle_rad_flt = eval(input('final angle (ratio without pi): '))
            final_angle_rad_str = str(final_angle_rad_flt)
            if final_angle_rad_flt * math.pi <= math.pi / 2:
                final_angle_rad_flt = final_angle_rad_flt * math.pi
                break
            elif len(final_angle_rad_str) == '1' and final_angle_rad_str != '1':
                final_angle_rad_flt = float(final_angle_rad_str)
                pass
            else:
                print('input too large (> pi/2)')
        except (SyntaxError, ValueError) as err:
            print('incorrect value, try again: ')
    while rad_deg == 'degrees':
        try:
            final_angle = float(input('final angle: '))
            if final_angle <= 90:
                final_angle_rad_flt = math.radians(final_angle)
                break
            else:
                print('input too large (> 90 degrees)')
        except (SyntaxError, ValueError) as err:
            print('incorrect value, try again: ')


def sf_vcd():
    eq_select_vcd()
    missing_param = input()
    while (missing_param != 'ti' and
           missing_param != 'fv'):
        print('invalid entry, what are you solving for?')
        eq_select_adg()
        missing_param = input()
    if missing_param == 'fv':  # FINAL VELOCITY MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True: # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial*math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # INTERVAL_TIME
            try:
                interval_time_str = input('time interval: ')
                illegal_char = '-'
                while illegal_char in interval_time_str:
                    print('time cannot be negative, try again: ')
                    interval_time_str = input('time interval: ')
                else:
                    interval_time_flt = float(interval_time_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        vcd = velocity_initial_vertical * interval_time_flt + (0.5 * adg_flt * (interval_time_flt ** 2))
        print(vcd, "meters")
    elif missing_param == 'ti': # TIME INTERVAL MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True: # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial*math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # VELOCITY_FINAL_VERTICAL
            try:
                velocity_final = float(input('final velocity vector: '))
                velocity_final_vertical = velocity_final * math.sin(final_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        vcd = (velocity_final_vertical ** 2 - velocity_initial_vertical ** 2)/(2 * adg_flt)
        print(vcd, "meters")


def sf_hcd():
    while True:  # ANGLE_INIT
        rad_deg_initial_input()
        break
    while True: # VELOCITY_INITIAL_VERTICAL
        try:
            velocity_initial = float(input('initial velocity vector: '))
            velocity_initial_vertical = velocity_initial*math.cos(init_angle_rad_flt)
            break
        except (SyntaxError, ValueError) as err:
            print('incorrect value, try again: ')
    while True: # INTERVAL_TIME
        try:
            interval_time_str = input('time interval: ')
            illegal_char = '-'
            while illegal_char in interval_time_str:
                print('time cannot be negative, try again: ')
                interval_time_str = input('time interval: ')
            else:
                interval_time_flt = float(interval_time_str)
                break
        except (SyntaxError, ValueError) as err:
            print('incorrect value, try again: ')
    hcd = velocity_initial_vertical * interval_time_flt
    print(hcd, "meters")


def sf_adg():
    eq_select_adg()
    missing_param = input()
    while (missing_param != 'fv' and
           missing_param != 'ti' and
           missing_param != 'vcd'):
        print('invalid entry, what are you solving for?')
        eq_select_adg()
        missing_param = input()
    if missing_param == 'fv':  # FINAL VELOCITY MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # VERTICAL DISTANCE
            try:
                distance_vertical = float(input('vertical distance: '))
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # INTERVAL_TIME
            try:
                interval_time_str = input('time interval: ')
                illegal_char = '-'
                while illegal_char in interval_time_str:
                    print('time cannot be negative, try again: ')
                    interval_time_str = input('time interval: ')
                else:
                    interval_time_flt = float(interval_time_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        adg = (2*distance_vertical - 2*velocity_initial_vertical*interval_time_flt)/(interval_time_flt**2)
        print('your acceleration due to gravity is', adg, 'm/s^2')
    elif missing_param == 'ti':  # TIME INTERVAL MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # VELOCITY_FINAL_VERTICAL
            try:
                velocity_final = float(input('final velocity vector: '))
                velocity_final_vertical = velocity_final * math.sin(final_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # VERTICAL DISTANCE
            try:
                distance_vertical = float(input('vertical distance: '))
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        adg = (velocity_final_vertical**2 - velocity_initial_vertical**2)/(2 * distance_vertical)
        print('your acceleration due to gravity is', adg, 'm/s^2')
    elif missing_param == 'vcd':  # VERTICAL CHANGE IN DISTANCE MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # VELOCITY_FINAL_VERTICAL
            try:
                velocity_final = float(input('final velocity vector: '))
                velocity_final_vertical = velocity_final * math.sin(final_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # INTERVAL_TIME
            try:
                interval_time_str = input('time interval: ')
                illegal_char = '-'
                while illegal_char in interval_time_str:
                    print('time cannot be negative, try again: ')
                    interval_time_str = input('time interval: ')
                else:
                    interval_time_flt = float(interval_time_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        adg = (velocity_final_vertical - velocity_initial_vertical)/interval_time_flt
        print('your acceleration due to gravity is', adg, 'm/s^2')


def sf_ti():
    eq_select_ti()
    missing_param = input()
    while (missing_param != 'fv' and
           missing_param != 'vcd'):
        print('invalid entry, what are you solving for?')
        eq_select_ti()
        missing_param = input()
    if missing_param == 'vcd': # VERTICAL DISTANCE MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # VELOCITY_FINAL_VERTICAL
            try:
                velocity_final = float(input('final velocity vector: '))
                velocity_final_vertical = velocity_final * math.sin(final_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        interval_time_flt = (velocity_final_vertical - velocity_initial_vertical)/adg_flt
        print(interval_time_flt, 'seconds')
    elif missing_param == 'fv': # FINAL VELOCITY MISSING
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # VERTICAL DISTANCE
            try:
                distance_vertical = float(input('vertical distance: '))
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        discrim_time = (velocity_initial_vertical ** 2) - (4 * (adg_flt/2) * (distance_vertical * -1))
        sol_time_1 = ((-1 * velocity_initial_vertical) - math.sqrt(discrim_time)) / (2 * (adg_flt/2))
        sol_time_2 = ((-1 * velocity_initial_vertical) + math.sqrt(discrim_time)) / (2 * (adg_flt/2))
        print('the solutions to the quadratic are:', sol_time_1, 'seconds', 'and', sol_time_2, 'seconds')


def sf_fv():
    eq_select_fv()
    missing_param = input()
    while (missing_param != 'ti' and
           missing_param != 'vcd'):
        print('invalid entry, what are you solving for?')
        eq_select_fv()
        missing_param = input()
    if missing_param == 'ti':
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL_HORIZONTAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                velocity_initial_horizontal = velocity_initial * math.cos(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # VERTICAL DISTANCE
            try:
                distance_vertical = float(input('vertical distance: '))
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        print(init_angle_rad_flt)
        velocity_final_vertical = math.sqrt(velocity_initial_vertical**2 + (2 * adg_flt * distance_vertical))
        velocity_final = math.sqrt(velocity_final_vertical**2 + velocity_initial_horizontal**2)
        print(velocity_final, 'm/s')
    elif missing_param == 'vcd':
        while True:  # ANGLE_INIT
            rad_deg_initial_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL_HORIZONTAL
            try:
                velocity_initial = float(input('initial velocity vector: '))
                velocity_initial_vertical = velocity_initial * math.sin(init_angle_rad_flt)
                velocity_initial_horizontal = velocity_initial * math.cos(init_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # INTERVAL_TIME
            try:
                interval_time_str = input('time interval: ')
                illegal_char = '-'
                while illegal_char in interval_time_str:
                    print('time cannot be negative, try again: ')
                    interval_time_str = input('time interval: ')
                else:
                    interval_time_flt = float(interval_time_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        velocity_final_vertical = velocity_initial_vertical + (adg_flt * interval_time_flt)
        velocity_final = math.sqrt(velocity_initial_horizontal**2 + velocity_final_vertical**2)
        print(velocity_final, 'm/s')


def sf_iv():
    eq_select_iv()
    missing_param = input()
    while (missing_param != 'ti' and
           missing_param != 'na' and
           missing_param != 'vcd'):
        print('invalid entry, what are you solving for?')
        eq_select_iv()
        missing_param = input()
    if missing_param == 'ti':
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # VELOCITY_FINAL_VERTICAL_HORIZONTAL
            try:
                velocity_final = float(input('final velocity vector: '))
                velocity_final_vertical = velocity_final * math.sin(final_angle_rad_flt)
                velocity_final_horizontal = velocity_final * math.cos(final_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # VERTICAL DISTANCE
            try:
                distance_vertical = float(input('vertical distance: '))
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        velocity_initial_vertical = math.sqrt(velocity_final_vertical**2 - (2 * adg_flt * distance_vertical))
        velocity_initial = math.sqrt(velocity_initial_vertical**2 + velocity_final_horizontal**2)
        print(velocity_initial, 'm/s')
    elif missing_param == 'vcd':
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # VELOCITY_INITIAL_VERTICAL_HORIZONTAL
            try:
                velocity_final = float(input('final velocity vector: '))
                velocity_final_vertical = velocity_final * math.sin(final_angle_rad_flt)
                velocity_final_horizontal = velocity_final * math.cos(final_angle_rad_flt)
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # INTERVAL_TIME
            try:
                interval_time_str = input('time interval: ')
                illegal_char = '-'
                while illegal_char in interval_time_str:
                    print('time cannot be negative, try again: ')
                    interval_time_str = input('time interval: ')
                else:
                    interval_time_flt = float(interval_time_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        velocity_initial_vertical = velocity_final_vertical - (adg_flt * interval_time_flt)
        velocity_initial = math.sqrt(velocity_initial_vertical**2 + velocity_final_horizontal**2)
        print(velocity_initial, 'm/s')
    elif missing_param == 'na':
        while True:  # ANGLE_FINAL
            rad_deg_final_input()
            break
        while True:  # ACCELERATION DUE TO GRAVITY
            try:
                adg_str = input('acceleration due to gravity: ')
                illegal_char = '-'
                while illegal_char in adg_str:
                    print('enter acceleration due to gravity as positive: ')
                    adg_str = input('acceleration due to gravity: ')
                else:
                    adg_flt = float(adg_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True:  # INTERVAL_TIME
            try:
                interval_time_str = input('time interval: ')
                illegal_char = '-'
                while illegal_char in interval_time_str:
                    print('time cannot be negative, try again: ')
                    interval_time_str = input('time interval: ')
                else:
                    interval_time_flt = float(interval_time_str)
                    break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        while True: # VERTICAL DISTANCE
            try:
                distance_vertical = float(input('vertical distance: '))
                break
            except (SyntaxError, ValueError) as err:
                print('incorrect value, try again: ')
        velocity_initial_vertical = (distance_vertical/interval_time_flt) - ((adg_flt * interval_time_flt)/2)
        if velocity_initial_vertical < 0:
            velocity_initial_vertical = velocity_initial_vertical * -1
        else:
            pass
        velocity_initial = velocity_initial_vertical/(math.sin(final_angle_rad_flt))
        print(velocity_initial)

