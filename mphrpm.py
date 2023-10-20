#!/usr/bin/python3

def mph(dx,dy,dz,frames,framerate):
    d = ((dx**2)+(dy**2)+(dz**2))**.5
    print(f'Pythagorean distance = {d}')
    t = frames/framerate
    print(f'Elapsed time = {t} seconds')
    fps = d/t
    [print(f'Converting {fps} feet per second yields:')]
    mph = fps*3600/5280
    print(f'\t\tSPEED = {round(mph,2)} MPH\n')

def rpm(f,fr):
    rpm = fr*60/f
    print(f'\n\t\tspin rate = {round(rpm,2)} RPM')

def prompt_calc():
    while True:
        metric = input('Are you calculating RPM or [MPH]?"\n\t')
        if (str.upper(metric) == 'MPH') or (metric == ''):
            x = float(input('\nDistance (ft) traveled along the baseline axis = '))
            y = float(input('Distance (ft) traveled along the sideline axis = '))
            z = float(input('Distance (ft) traveled vertically = '))
            f = float(input('Elapsed frames = '))
            fr = float(input('Frame rate = '))
            mph(x,y,z,f,fr)
            break
        elif str.upper(metric) == 'RPM':
            f = float(input('\nElapsed frames for 1 revolution = '))
            fr = float(input('Frame rate = '))
            rpm(f,fr)
            break
        else:
            print("\nInput not recognized.  Let's try that again, shall we?\n\n")    

prompt_calc()
