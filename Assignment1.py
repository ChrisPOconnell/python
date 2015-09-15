__author__ = 'ChrisP'
print("Welcome to the catalog prep program!")
print("This program will be used to correct the catalog spread sheets")
print()
provnum=0
provlist=list()
while provnum < 3 or provnum >10:
    provnum=eval(input("How many Provinces are in this year's catalog?  "))
    if provnum < 3 or provnum > 10:
        print("Please enter a single digit number between 3 and 10  ")
        #Unfortunately if someone enters a letter here the program crashes.
        #to be fixed in a later version

print("Great, you have",provnum,"Provinces to work with this year.  That should be easy :)")
print()
print("Next let's collect the 3 letter Province abbreviations.")

indx=0
while (indx< provnum):
    prov=input("Please enter the three digit Province abbreviation, then press ENTER:  ")
    if len(prov)!=3:
        print("Sorry, the Province abbreviation must be 3 letters!")
    elif len(prov)==3:
        provlist.append(prov)
        indx= indx+1

print("You have",provnum,"Provinces this year.  They are:")
print(provlist)


