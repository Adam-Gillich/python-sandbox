def time_converter(time_in):
    seconds = time_in % 60
    minutes = int(time_in / 60) % 60
    hours = int(time_in / 3600) % 24
    days = int(time_in / (3600 * 24))
    time = [days, hours, minutes, seconds]
    return time


t = 12*3600 + 18317
time = time_converter(t)

print(f"{time[0]}d:{time[1]}h:{time[2]}m:{time[3]}s")
