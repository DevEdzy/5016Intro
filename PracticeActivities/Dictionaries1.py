# Dictionaries1.py
#
# author: Michael Edwards
# date: 19/11/2022

cities = {
    "Auckland": "AKL",
    "Wellington": "WLG",
    "Christchurch": "CHC",
    "Dunedin": "DND"
}

more_cities = {
    "Rotorua": "ROT",
    "Invercargill": "INV",
    "Napier": "NPR"
}

print(cities)
cities.update(more_cities)
print(cities)

del(cities["Dunedin"])
print(cities)
