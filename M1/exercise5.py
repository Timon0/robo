duration_90_degree = 1200
duration_45_degree = duration_90_degree // 2
drive_duration = 1500
drive_short = 1060
drive_long = 2121

default_speed = 250
default_turn_speed = 200

turn_left = 1
turn_right = 2

current_position = 0

turn_directions = [1, 1, 2, 2, 2, 2, 2]
turn_radius = [duration_90_degree,duration_90_degree,3*duration_45_degree,duration_90_degree,duration_90_degree-100,3*duration_45_degree,3*duration_45_degree-150]
drive_durations = [drive_duration,drive_duration,drive_duration,drive_short,drive_short,drive_long,drive_duration,drive_long]

def turn_left(turn_duration):
    global motor_left_target, motor_right_target, default_turn_speed, timer_period,duration_45_degree
    motor_left_target = -default_turn_speed
    motor_right_target = default_turn_speed
    timer_period[1] = turn_duration
    timer_period[0] = 32000
    
def turn_right(turn_duration):
    global motor_left_target, motor_right_target, default_turn_speed, timer_period
    motor_left_target = default_turn_speed
    motor_right_target = -default_turn_speed
    timer_period[1] = turn_duration
    timer_period[0] = 32000

def start():
    global motor_left_target, motor_right_target, default_speed, timer_period, drive_durations
    motor_left_target = default_speed
    motor_right_target = default_speed
    timer_period[0] = drive_durations[0]
    
def stop():
    global motor_left_target, motor_right_target
    motor_target_left = 0
    motor_target_right = 0

@onevent
def rc5():
    if rc5_command == 53:
        start()
        
@onevent
def buttons():
    if button_forward:
        start()
        
@onevent
def timer0():
    global turn_directions, turn_radius, current_position, timer_period, motor_right_target, motor_left_target
    if current_position <= 7:
        if motor_right_target == 0 and motor_left_target == 0:
            motor_right_target = default_speed
            motor_left_target = default_speed
            timer_period[0] = drive_durations[current_position]
            
            if current_position == 7:
                current_position = current_position + 1
        else:
            if turn_directions[current_position] == 1:
                turn_left(turn_radius[current_position])
            else:
                turn_right(turn_radius[current_position])
            current_position = current_position + 1
    else:
        stop()
        
@onevent
def timer1():
    global motor_left_target, motor_right_target, timer_period
    motor_left_target = 0
    motor_right_target = 0
    timer_period[0] = 500
    timer_period[1] = 32000
