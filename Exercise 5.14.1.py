import time

def print_days():
    days = int((time.time()) // 60 // 60 // 24)
    print(f'It has been {days} days since the epoch')

def hours_time():
    hours_since_epoch = ((time.time()) // 60 // 60)
    hours_today_mil = int(hours_since_epoch % 24)
    hours_today_stand = hours_today_mil - 12
    return hours_today_stand


def minutes_time():    # put in code for minutes
    minutes_since_epoch = ((time.time()) // 60)
    minutes_today = int(minutes_since_epoch % 60)
    return minutes_today


def seconds_time():    # put in code for seconds
    seconds_today = int(time.time() % 60)
    return seconds_today


def time_today_gmt():
    hours = hours_time()
    minutes = minutes_time()
    seconds = seconds_time()
    print(f'The current Greenwich Mean Time is {hours}:{minutes}:{seconds}')

def time_today_cst():
    hours = hours_time() - 6
    minutes = minutes_time()
    seconds = seconds_time()
    print(f'The current Central Standard Time is {hours}:{minutes}:{seconds}')

time_today_gmt()
time_today_cst()
print_days()