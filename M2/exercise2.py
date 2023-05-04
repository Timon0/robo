defaultSpeed = 200
started = False

mid = 512
left = mid + mid // 2
right = mid - mid // 2

last_direction = 0

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
    global motor_right_target, motor_left_target, defaultSpeed, started, last_direction
    if started:
        p_right = prox_ground_delta[1]
        p_left = prox_ground_delta[0]
        
        if p_left > mid and p_right > mid:
            if last_direction == 0:
                pass
                #drive_straigth(0)
            elif last_direction == 1:
                motor_right_target = 75
                motor_left_target = 300
            elif last_direction == 2:
                motor_right_target = 300
                motor_left_target = 75
        elif p_left > mid:
            motor_right_target = 150
            motor_left_target = 250
            last_direction = 1
        elif p_right > mid:
            motor_left_target = 150
            motor_right_target = 250
            last_direction = 2
        else:
            drive_straigth(defaultSpeed)
            last_direction = 0
        
