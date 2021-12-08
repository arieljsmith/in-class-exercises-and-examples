# try to represent a musician with a dictionary

musicians = [{
    "name": "Andrew Bird",
    "instrument": ["violin", "whistle"],
    "record label": "Merge",
    "bands": ["Band 1", "Band 2", "Band 3"]
    },
    {

    }]

# as we reach the limitations of dictionaries to represent data, we
# can move to classes


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    # The __str__ defines what's shown when you try to print an instance
    # of this class (as further below--otherwise trying to print it will
    # just show where in memory it can be found.
    def __str__(self):
        return f"{self.name}: {self.instrument}"


# when I create an object that's an element of a class, it's called an instance
# let's create a musician and store that instance in a variable
# writing the name of the class with () causes the __init__ method to be called
snoop = Musician("Snoop Dogg", "MC")
print(snoop)

jewel = Musician("Jewel", "guitar")
print(jewel)


class Band:
    def __init__(self, name):
        self.name = name
        self.members = []

    def __str__(self):
        return self.name
    # ***IF YOU WERE TO MAKE THE BELOW A @Property, THEN...
    def show_members(self):
        print(f"The members of {mouse_rat.name} are: ", [f"{member}" for member in mouse_rat.members])

mouse_rat = Band("Mouse Rat")
print(f"The members of {mouse_rat.name} are {mouse_rat.members}")

mouse_rat.members.extend([snoop, jewel]) # Extend is used in place of append when you want to add multiples at one time

print(f"The members of {mouse_rat.name} are: ", [f"{member}" for member in mouse_rat.members])
# create a new musician instances
andy = Musician("Andy Dwyer", "guitar")
duke = Musician("Duke Silver", "saxophone")
# add those musicians to the members of the band

new_members = [andy, duke]

mouse_rat.members.extend(new_members)
# ***...YOU'D CALL THE BELOW WITHOUT () (so mouse_rat.show_members())
mouse_rat.show_members()

avril = Musician("Avril Lavigne", "vocals")

mouse_rat.members.append(avril)
mouse_rat.show_members()
