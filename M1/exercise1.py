motor_left_target = 250
motor_right_target = 250
timer_period[0] = 10000
                 
@onevent
def timer0():
    global motor_left_target, motor_right_target
    motor_left_target = 0
    motor_right_target = 0
