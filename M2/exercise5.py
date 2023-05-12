default_speed = 400
started = False

error = 0
prev_error = 0

error_sum = 0

prev_error_size = 10
prev_errors = [0,0,0,0,0,0,0,0,0,0]
current_pos = 0

c_p = 35
c_d = 5
c_i = 15

def drive_straigth(speed):
    global motor_left_target, motor_right_target
    motor_left_target = speed
    motor_right_target = speed
    
def fill_errors(error_size):
    pass

def update_errors(current_error):
    prev_errors[current_pos] = current_error
    current_pos += 1
    if current_pos == 10:
        current_pos = 0

@onevent
def button_forward():
    global defaultSpeed, started, prev_error_size
    drive_straigth(default_speed)
    #prev_errors = fill_errors(prev_error_size)
    started = True
    
@onevent
def button_backward():
    global motor_right_target, motor_left_target, defaultSpeed, started, error_sum
    started = False
    error_sum = 0
    drive_straigth(0)

@onevent
def prox():
    global motor_right_target, motor_left_target, default_speed, started, error, prev_error, black, c_p, c_i, c_d, prev_errors, prev_error_size
    if started:
        p_right = prox_ground_delta[1]
        p_left = prox_ground_delta[0]
        
        error = p_right - p_left
        
        update_errors(error)
        summe = 0
        print(len(prev_errors))
        for i in range(len(prev_errors)):
            summe += prev_errors[i]
            print(prev_errors[i])
        error_sum = summe // prev_error_size
        
        P = (c_p * (error)) // 100
        I = (c_i * error_sum) // 400
        D = (c_d * (error - prev_error)) // 300
        change = P + I + D
        
        motor_left_target = default_speed - change
        motor_right_target = default_speed + change

        prev_error = error