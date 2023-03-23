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

    result = np.array([[1,0,0,0],[0,1,0,0], [0,0,1,0], [0,0,0,1]])
    for i, joint in enumerate(joints):
        trans = translation(translationen[i])
        rot = rotate_z(90 - joint)
        if i > 0 and i < 5:
            rot = rotate_y(90 -joint)
        result = result @ trans @ rot

    return result

def translation(trans):
    return np.array([[1,0,0,trans[0]], [0,1,0,trans[1]],[0,0,1,trans[2]], [0,0,0,1]])

def rotate_z(theta):
    rad = radians(theta)
    return np.array([[cos(rad), -sin(rad), 0, 0], [sin(rad), cos(rad), 0, 0],[0,0,1,0], [0,0,0,1]])

def rotate_y(theta):
    rad = radians(theta)
    return np.array([[cos(rad),0, sin(rad), 0],[0,1,0,0], [-sin(rad),0, cos(rad), 0], [0,0,0,1]])
