planet = 'Pluto'
print(planet[0])

print(planet[-3:])

print(len(planet))

print([char+'! ' for char in planet])

planet[0] = 'B'
# planet.append doesn't work either

print(planet)