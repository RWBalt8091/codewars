import math

def what_is_the_time(time_in_mirror):
    time_split = time_in_mirror.split(':')
    
    hours = time_split[0]
    minutes = time_split[1]
    hours = int(hours)
    minutes = int(minutes)
    
    if hours == 12:
        hours = 0
    
    total_minutes = (hours * 60) + minutes
    mirrored_total_minutes = 720 - total_minutes
    mirrored_hours = str(math.trunc(mirrored_total_minutes/60))
    mirrored_minutes = str(mirrored_total_minutes%60)
    
    if mirrored_hours == '0':
        mirrored_hours = '12'
    
    if len(mirrored_hours) < 2:
        mirrored_hours = '0' + mirrored_hours
    
    if len(mirrored_minutes) < 2:
        mirrored_minutes = '0' + mirrored_minutes
    
    mirrored_time = mirrored_hours + ':' + mirrored_minutes
    return mirrored_time