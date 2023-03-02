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
turn_radius = [duration_90_degree,duration_90_degree,3*duration_45_degree,duration_90_degree,duration_90_degree,3*duration_45_degree,3*duration_45_degree]
drive_durations = [drive_duration,drive_duration,drive_duration,drive_short,drive_short,drive_long,drive_duration,drive_long]

def turn_left(turn_duration):
    global motor_left_target, motor_right_target, default_turn_speed, timer_period,duration_45_degree
    motor_left_target = -default_turn_speed
    motor_right_target = default_turn_speed
    timer_period[0] = turn_duration
    print(turn_duration)
    
def turn_right(turn_duration):
    global motor_left_target, motor_right_target, default_turn_speed, timer_period
    motor_left_target = default_turn_speed
    motor_right_target = -default_turn_speed
    timer_period[0] = turn_duration

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
        if motor_right_target != motor_left_target:
            motor_right_target = default_speed
            motor_left_target = default_speed
            timer_period[0] = drive_durations[current_position]
        else:
            if turn_directions[current_position] == 1:
                print('left')
                turn_left(turn_radius[current_position])
            else:
                print('right')
                turn_right(turn_radius[current_position])
            current_position = current_position + 1
    else:
        stop()
