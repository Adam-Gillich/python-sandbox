mondat = input("Írd be a mondatot ")
irasjelek = [".", ",", "?", "!"]

for i in irasjelek:
    betuk = mondat.replace(i, '')
print(betuk)