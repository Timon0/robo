speed = 500
in_dark_zone = False
measuring = False
started = False
measured_time = 0
measure_distance = 10

@onevent
def buttons():
    global motor_right_target, motor_left_target, speed, started
    if button_forward:
        motor_right_target = speed
        motor_left_target = speed
        started = True
        
@onevent
def prox():
    global timer_period, measuring, in_dark_zone, motor_right_target, motor_left_target, started, measure_distance
    if started:
        if in_dark_zone and prox_ground_delta[0] > 700 and not measuring:
            timer_period[0] = measure_distance
            in_dark_zone = False
            measuring = True
        elif in_dark_zone and measuring and prox_ground_delta[0] < 700:
            motor_right_target = 0
            motor_left_target = 0
        if not in_dark_zone and prox_ground_delta[0] < 700:
            in_dark_zone = True
            timer_period[0] = 0
    
@onevent
def timer0():
    global measured_time, measure_distance
    measured_time = measured_time + measure_distance
    print(measured_time)