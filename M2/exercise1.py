defaultSpeed = 150
started = False

mid = 512
left = mid + mid // 2
right = mid - mid // 2



def drive_straigth(speed):
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = speed

@onevent
def button_forward():
    global defaultSpeed, started
    drive_straigth(defaultSpeed)
    started = True
    
@onevent
def button_backward():
    global motor_right_target, motor_left_target, defaultSpeed, started
    started = False
    drive_straigth(0)
    
@onevent
def prox():
    global motor_right_target, motor_left_target, defaultSpeed, started
    if started:
        p_right = prox_ground_delta[1]
        p_left = prox_ground_delta[0]
        
        if p_left > mid:
            motor_right_target = 100
            motor_left_target = 200
        elif p_right > mid:
            motor_left_target = 100
            motor_right_target = 200
        else:
            drive_straigth(defaultSpeed)
        