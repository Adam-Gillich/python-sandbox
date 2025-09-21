import math
import yaml


def input_float(text):
    while True:
        try:
            value = float(input(text).replace(',', '.', ).replace(' ', '').strip("meters"))
        except ValueError:
            print("\nSomething's wrong! You can only input numbers!\n   Try again!\n")
            continue
        return value


def input_whole(text):
    while True:
        try:
            value = int(input(text).replace(',', '.', ).replace(' ', '').strip())
        except ValueError:
            print("\nSomething's wrong! You can only input WHOLE numbers!\n   Try again!\n")
            continue
        if value < 0:
            print("\nYou can only input WHOLE numbers!\n    Try again!\n")
            continue
        return value


def satellite_number(n):
    while True:
        if n < 3:
            print("\nUnable to configure a system with less than 3 satellites! \n   Try again!\n")
            n = input_whole("Please enter at least 3! ")
            continue
        return (n - 1) / n, n


def orbit_calculator(R, h0, mu, x):
    r0 = R + h0
    T = 2 * math.pi * math.sqrt(r0 ** 3 / mu)
    T23 = (x) * T
    a = (x ** (2 / 3)) * r0
    rp = 2 * a - r0
    if rp < R or rp < ra:
        x = x ** -1
        a = (x ** (2 / 3)) * r0
        rp = 2 * a - r0
    hp = rp - R
    return round(hp), round(T), round(T23)


def time_converter(time_in):
    seconds = time_in % 60
    minutes = int(time_in / 60) % 60
    hours = int(time_in / 3600) % 24
    days = int(time_in / (3600 * 24))
    time = [days, hours, minutes, seconds]
    return time


choose_txt = "Choose the body where you want your Relay Network to be:\n" \
             "Kerbol   ->(ker)\n" \
             " Moho    ->(mo)\n" \
             " Eve     ->(e)\n" \
             "   Gilly ->(g)\n" \
             " Kerbin  ->(k)\n" \
             "   Mun   ->(mu)\n" \
             "   Minmus->(mi)\n" \
             " Duna    ->(d)\n" \
             "   Ike   ->(i)\n" \
             " Dres    ->(dr)\n" \
             " Jool    ->(j)\n" \
             "   Laythe->(l)\n" \
             "   Vall  ->(v)\n" \
             "   Tylo  ->(t)\n" \
             "   Bop   ->(b)\n" \
             "   Pol   ->(p)\n" \
             " Eeloo   ->(ee)\n" \
             "\nEnter either the name or the letter(s) in brackets! "


def choose_body():
    try:
        key = input(choose_txt)
        name = config[key]
        return name
    except KeyError:
        for i in config.keys():
            if config[i]["alt_name"] == key:
                name = i
                return name
        while True:
            try:
                key = input("\nSomething went wrong! The names are case sensitive!\n  Try again!\n")
                name = config[key]
                return name
            except KeyError:
                for i in config.keys():
                    if config[i]["alt_name"] == key:
                        name = i
                        return name
                continue


Configfile = "C:\\Users\\Admin\\Documents\\VSC-Projects\\python-sandbox\\Adam\\relay_network_calculator_config.yaml"

with open(Configfile, "r") as file:
    config = yaml.safe_load(file)

'''
for k in list(config.keys()):
    if "alt_name" in config[k]:
        ak = config[k]["alt_name"]
        config[ak] = config[k]
'''


name = choose_body()

cfg = config[name]
R = float(cfg["R"])
std_grav_para = float(cfg["std_grav_para"])

if name == "Kerbol":
    soi = "infinite"
else:
    soi = float(cfg["SOI"])

try:
    atmosphere = float(cfg["Atmosphere"])
    ra_alt = atmosphere
    ra = R + atmosphere
except KeyError:
    ra = 0
    ra_alt = 0



requested_height = input_float("\nDefine the desired END HEIGHT (from the surface) of the Relay Network in meters! ")

while True:
    if requested_height < ra_alt:
        print(f"\nIt seems like the END HEIGHT is LOWER than the atmosphere of {name}!\n    Try again! The atmosphere of {name} is {ra_alt} meters!\n")
        requested_height = input_float("\nDefine the desired END HEIGHT (from the surface) of the Relay Network in meters! ")
        continue
    try:
        if requested_height > soi:
            print(f"\n it seems like the END HEIGHT is HIGHER than the Sphere of influence of {name}!\n    Try again! The SOI of {name} is {soi} meters!\n")
            requested_height = input_float("\nDefine the desired END HEIGHT (from the surface) of the Relay Network in meters! ")
            continue
    except TypeError:
        pass
    break


SatNumVar, SatNum = satellite_number(input_whole("\nDefine the desired number of Satellites of the Relay Network! "))


hp, T, T23 = orbit_calculator(R, requested_height, std_grav_para, SatNumVar)
end_period = time_converter(T)
phasing_period = time_converter(T23)

print(f"\n\n\n"
      f"You requested a satellite network around: {name}, with {SatNum} satellites!\n"
      f"You set the height of the network to {requested_height} meters!\n"
      f"\n"
      f"So at the end your satellite network should be on a circular orbit of {requested_height} meters.\n"
      f"It's period should be {f'{end_period[0]}d:' if end_period[0] > 0 else ''}{end_period[1]}h:{end_period[2]}m:{end_period[3]}s.\n"
      f"\n"
      f"To achieve that, your phasing orbit's\n"
      f"Apoapsis should be: {requested_height} meters\n"
      f"Periapsis should be: {hp} meters\n"
      f"With a period of {f'{phasing_period[0]}d:' if phasing_period[0] > 0 else ''}{phasing_period[1]}h:{phasing_period[2]}m:{phasing_period[3]}s\n"
      f"\n"
      f"Try to match these values as close as you can!\nGood Luck!")


