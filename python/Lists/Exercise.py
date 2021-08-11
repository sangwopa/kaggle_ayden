def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) == 1 or len (L) == 0:
        return None
    else:
        return(L[1])

L = []

print(len(L))
print(select_second(L))

def losing_team_captain(teams):
    """Given a list of teams, where each team is a list of names, return the 2nd player (captain)
    from the last listed team
    """
    return teams[-1][1]

teams = [['Paul', 'John', 'Ringo', 'George']]

print(losing_team_captain(teams))

def purple_shell(racers):
    """Given a list of racers, set the first place racer (at the front of the list) to last
    place and vice versa.
    
    >>> r = ["Mario", "Bowser", "Luigi"]
    >>> purple_shell(r)
    >>> r
    ["Luigi", "Bowser", "Mario"]
    """
    racers[0], racers[-1] = racers[-1], racers[0]
    return racers

r = ["Mario", "Bowser", "Luigi"]
purple_shell(r)
print(r)

a = [1, 2, 3]
b = [1, [2, 3]]
c = []
d = [1, 2, 3][1:]

print(len(a), len(b), len(c), len(d),)

print(d)

def fashionably_late(arrivals, name):
    """Given an ordered list of arrivals to the party and a name, return whether the guest with that
    name was fashionably late.
    """
    if name in arrivals[(round(len(arrivals)/2)):-1]:
        return True
    else:
        return False

party_attendees = ['Adela', 'Fleda', 'Owen', 'May', 'Mona', 'Gilbert', 'Ford']

print(party_attendees[(round(len(party_attendees)/2)):-1])

print(fashionably_late(party_attendees, 'Mona'))
