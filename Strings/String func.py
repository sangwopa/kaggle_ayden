claim = "Pluto is a planet!"
planet = 'Pluto'

words = claim.split()

print(words)

datestr = '1956-01-31'
year, month, day = datestr.split('-')

print('/'.join([month, day, year]))

print(' 👏 '.join([word.upper() for word in words]))

print(planet + ', we miss you.')

position = 9

print(planet + ", you'll always be the " + str(position) + "th planet to me.")

print("{}, you'll always be the {}th planet to me.".format(planet, position))

pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390

print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(planet, pluto_mass, pluto_mass / earth_mass, population,))

# Referring to format() arguments by index, starting from 0
s = """Pluto's a {0}.
No, it's a {1}.
{0}!
{1}!""".format('planet', 'dwarf planet')
print(s)