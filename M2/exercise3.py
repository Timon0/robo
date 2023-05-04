defaultSpeed = 200
started = False

error = 0
prev_error = 0

error_sum = 0

c_p = 10
c_d = 5
c_i = 5

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
    global motor_right_target, motor_left_target, defaultSpeed, started, error_sum
    started = False
    error_sum = 0
    drive_straigth(0)
    


@onevent
def prox():
    global motor_right_target, motor_left_target, defaultSpeed, started, error, prev_error, error_sum, mid, c_p, c_i, c_d
    if started:
        p_right = prox_ground_delta[1]
        p_left = prox_ground_delta[0]
        
        p_mean = (p_right + p_left) // 2
        error = mid - p_left
        
        error_sum += error

        P = (c_p * (error)) // 100
        I = (c_i * error_sum) // 400
        D = (c_d * (error - prev_error)) // 400
        change = P + I + D
        
        if  error_sum == 0:
            updated_ground_speed = defaultSpeed
            print('no error')
        
        if  abs(error_sum // 100) == 0:
            updated_ground_speed = defaultSpeed
            print('no error')
        else:
            speed = (1000 * defaultSpeed)
            abs_error = (abs(error_sum) // 100)
            updated_ground_speed = speed // abs_error
        
        motor_left_target = updated_ground_speed - change
        motor_right_target = updated_ground_speed + change

        prev_error = error

        

