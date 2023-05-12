default_speed = 200
started = False

error = 0
prev_error = 0

error_sum = 0

c_p = 20
c_d = 5
c_i = 5

black = 800

def drive_straigth(speed):
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = speed

@onevent
def button_forward():
    global defaultSpeed, started
    drive_straigth(default_speed)
    started = True
    
@onevent
def button_backward():
    global motor_right_target, motor_left_target, defaultSpeed, started, error_sum
    started = False
    error_sum = 0
    drive_straigth(0)

@onevent
def prox():
    global motor_right_target, motor_left_target, default_speed, started, error, prev_error, error_sum, black, c_p, c_i, c_d
    if started:
        p_right = prox_ground_delta[1]
        p_left = prox_ground_delta[0]
        
        position = black
        if p_right < black:
            position = p_right + black
        elif p_left < black:
            position = p_left
        
        error = black - position
        
        error_sum += error

        P = (c_p * (error)) // 100
        I = (c_i * error_sum) // 300
        D = (c_d * (error - prev_error)) // 300
        change = P + I + D
        
        if  error_sum == 0:
            updated_ground_speed = default_speed
        
        if  abs(error_sum // 100) == 0:
            updated_ground_speed = default_speed
        else:
            speed = (1000 * default_speed)
            abs_error = (abs(error_sum) // 100)
            updated_ground_speed = speed // abs_error
        
        motor_left_target = default_speed - change
        motor_right_target = default_speed + change

        prev_error = error