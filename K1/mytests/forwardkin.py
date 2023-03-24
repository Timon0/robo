import numpy as np
from math import pi, cos, sin, radians

measurements = {
    'j0z': 3,
    'j1z': 71,
    'j2z': 126,
    'j3z': 124,
    'j4z': 60,
    'j5z': 134
}

translationen = [
    [281, 0, measurements['j0z']],
    [0,0, measurements['j1z']],
    [0,0, measurements['j2z']],
    [0,0, measurements['j3z']],
    [0,0, measurements['j4z']],
    [0,0, measurements['j5z']],
]

def forward_kinematic_braccio(joints):
    ''' param: joints: current position of all the joints of the braccio '''
    ''' return: current position'''

    result = np.eye(4)
    
    ## initial translation
    result = result @ translation([281, 0, 3])
    
    ## Joint 0
    result = result @ rotate_z(90 - joints[0]) @ translation([0, 0, 71]) 
    
    ## Joint 1
    result = result @ rotate_y(90 - joints[1]) @ translation([0, 0, 126]) 
    
    ## Joint 2
    result = result @ rotate_y(90 - joints[2]) @ translation([0, 0, 124]) 
    
    ## Joint 3
    result = result @ rotate_y(90 - joints[3]) @ translation([0, 0, 60])

    ## Joint 4
    result = result @ rotate_z(90 - joints[4]) @ translation([0, 0, 134]) 
    
    return result

def translation(trans):
    return np.array([
        [1,0,0,trans[0]],
        [0,1,0,trans[1]],
        [0,0,1,trans[2]],
        [0,0,0,1]
    ])

def rotate_z(theta):
    rad = radians(theta)
    return np.array([
        [cos(rad), -sin(rad), 0, 0],
        [sin(rad), cos(rad), 0, 0],
        [0,0,1,0],
        [0,0,0,1]
    ])

def rotate_y(theta):
    rad = radians(theta)
    return np.array([
        [cos(rad),0, sin(rad), 0],
        [0,1,0,0],
        [-sin(rad),0, cos(rad), 0],
        [0,0,0,1]
    ])
