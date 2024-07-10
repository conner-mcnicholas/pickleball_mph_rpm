#!/usr/bin/python3

import sys

def mph(dx,dy,dz,frames,framerate):
    d = ((dx**2)+(dy**2)+(dz**2))**.5
    print(f'Pythagorean distance = {round(d,2)} feet')
    t = frames/framerate
    print(f'Elapsed time = {round(t,2)} seconds')
    fps = d/t
    print(f'Converting {round(fps,2)} feet per second yields:')
    mph = fps*3600/5280
    print(f'\t\tSPEED = {round(mph,2)} MPH\n')

def rpm(f,fr):
    rpm = fr*60/f
    print(f'\n\t\tspin rate = {round(rpm,2)} RPM')

def prompt_calc():
    while True:
        if len(sys.argv) > 1:
            if str.upper(sys.argv[1]) == "MPH":
                metric = "MPH"
            elif str.upper(sys.argv[1]) == "RPM":
                metric = "RPM"
            else:
                print('First command line argument not recognized, assuming MPH')
                metric = "MPH"
        else:
            metric = input('Are you calculating RPM or [MPH]?"\n\t')
        if len(sys.argv) > 2:
            fr = float(str.upper(sys.argv[2]))  
        else:
            fr = input('\nFrame rate [30 fps] = ')
            print(f"fr = {fr}")
            if fr == "":
                fr = 30.0
            else:
                fr = float(fr)
        if (str.upper(metric) == 'MPH') or (metric == ''):
            d = {}
            d['x'] = input('\nDistance (0 ft) traveled along the baseline axis = ')
            d['y'] = input('Distance (0 ft) traveled along the sideline axis = ')
            d['z'] = input('Distance (0 ft) traveled vertically = ')
            f = float(input('Elapsed frames = '))
            for i in d.keys():
                if d[i] == "":
                    d[i] = 0.0
                else:
                    d[i] = float(d[i])
            x,y,z = list(d.values())
            mph(x,y,z,f,fr)
            break
        elif str.upper(metric) == 'RPM':
            f = float(input('\nElapsed frames for 1 revolution = '))
            rpm(f,fr)
            break
        else:
            print("\nInput not recognized.  Let's try that again, shall we?\n\n")    

prompt_calc()
