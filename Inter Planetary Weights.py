#Make a program to calculate a person's weight on the different planets in our solar system

#Write out the named constants for each planet's surface gravity factor
nMercury = 0.38
nVenus = 0.91
nMoon = 0.165
nMars = 0.38
nJupiter = 2.34
nSaturn = 0.93
nUranus = 0.92
nNeptune = 1.12
nPluto = 0.066

#Get the user's name and weight on earth and convert the entered weight to a numeric data that can store decimal points
sName = input("What is your name?")

fWeight = float(input("Please enter your weight:"))

#Multiple the earth weight by each planet's surface gravity factor
fMercuryWeight = fWeight * nMercury
fVenusWeight = fWeight * nVenus
fMoonWeight = fWeight * nMoon
fMarsWeight = fWeight * nMars
fJupiterWeight = fWeight * nJupiter
fSaturnWeight = fWeight * nSaturn
fUranusWeight = fWeight * nUranus
fNeptuneWeight = fWeight * nNeptune
fPlutoWeight = fWeight * nPluto

#Print out the weight of the user on each planet
print(sName, "here are your weights on our Solar System's planets:")
print('{:25}'.format("Weight on Mercury is:") , '{:10,.2f}'.format(fMercuryWeight))
print('{:25}'.format("Weight on Venus is:") , '{:10,.2f}'.format(fVenusWeight))
print('{:25}'.format("Weight on Moon is:") , '{:10,.2f}'.format(fMoonWeight))
print('{:25}'.format("Weight on Mars is:") , '{:10,.2f}'.format(fMarsWeight))
print('{:25}'.format("Weight on Jupiter is:") , '{:10,.2f}'.format(fJupiterWeight))
print('{:25}'.format("Weight on Saturn is:") , '{:10,.2f}'.format(fSaturnWeight))
print('{:25}'.format("Weight on Uranus is:") , '{:10,.2f}'.format(fUranusWeight))
print('{:25}'.format("Weight on Neptune is:") , '{:10,.2f}'.format(fNeptuneWeight))
print('{:25}'.format("Weight on Pluto is:") , '{:10,.2f}'.format(fPlutoWeight))