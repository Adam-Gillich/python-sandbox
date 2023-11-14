import time
text = input("Adj meg egy szöveget: ")
liszt = []

for i in text:
    liszt.append(i)
    print("\r", "".join(liszt), end= "")
    time.sleep(1)
