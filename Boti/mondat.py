mondat = input("Írd be a mondatot: ")
irasjelek = [".", ",", "?", "!"]
kiszurendo = '.,?! '

def betuk_db(mondat):
    for karakter in mondat:
        if karakter not in kiszurendo:
            betuk = [karakter]

betuk_db(mondat)

print(f'A mondatban ' len(betuk) ' db betű van.')
input("Enter")
