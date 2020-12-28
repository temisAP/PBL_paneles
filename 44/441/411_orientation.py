from scipy import optimize
import math

L_spring = 20
d = L_spring/10
H = L_spring-d
estado = 'cerrado'

def F(pitch):
    t = (2*math.pi)/pitch * H
    if pitch<=(d):
        return 9999
        print(pitch)
    elif pitch > d:
        return math.cos(t)-math.cos(theta)

if estado == 'abierto':
    theta = 0
    pitch = optimize.newton(F,H/10*1.25)
elif estado == 'cerrado':
    theta = math.pi
    pitch = optimize.newton(F,H/10*1.2)

print(pitch)
