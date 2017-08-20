addressbook = []
with open('cities.txt', 'r') as f:
    for line in f:
        city = line[:]
        addressbook.append(city)

print(addressbook)