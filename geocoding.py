import geopy
from geopy.geocoders import ArcGIS
import pandas
arc = ArcGIS()
import difflib
from difflib import get_close_matches


cx = 0

data = {"yes":1,"no":1}
Saved_Address_Geocoding_ = pandas.DataFrame([["None","None","None"]], 
columns = ["Address","Latitude","Longitude"],
 index = ["1."])


#used to turn a string into lowercase and with no spaces
def lower(a):
    if isinstance(a, str):
        pass
    else:
        print("Enter a proper answer.")
    a = a.strip()
    a = a.lower()
    return a
def low(a,b):
    if isinstance(a, str) and isinstance(b,str):
        pass
    else:
        return "Please enter a proper address."
    a = a.strip()
    b = b.strip()
    a = a.lower()
    b = b.lower()
    a = a.title()
    b = b.title()
    return a, b

#Used to find the latitudes of the address
def latitudes(a,b):
    d = arc.geocode(a + ", " + b, timeout = 10000)
    return d.latitude

#Used to find the longitudes of the address
def longitudes(a,b):
    c = arc.geocode(a + ", " + b, timeout = 10000)
    return c.longitude

#Creates the Pandas Dataframe to store the address
def cc(a,b,c):
    #Gathers addresses
    x = arc.geocode(a + ", " + b)
    x = x.address
    x1 = latitudes(a,b)
    x2 = longitudes(a,b)
    #Prints Addresses
    print("")
    print("The Address is: {}".format(x))
    print("")
    print("Latitude is {} and the Longitude is {}".format(x1, x2))
    #Creates the Dataframe if this is the first address
    if cx == 1:
        c["Address"] = c["Address"].replace(["None"], "{}".format(x))
        c["Latitude"] = c["Latitude"].replace(["None"], "{}".format(x1))
        c["Longitude"] = c["Longitude"].replace(["None"], "{}".format(x2))
        return c
    #Adds on to the dataframe is this is the second address+
    elif cx > 1: 
        new_row = {"Address": x, "Latitude": x1, "Longitude": x2}
        c = c.append(new_row, ignore_index = True)
        #Creates the index
        n = []
        for z in range(1,cx + 1):
            n.append("{}.".format(z))
        c.index = n
        return c
    else:
        print("Error")
        exit()

#Part of code which takes the address
print("")
ss = str(input("Do you want to store an address? "))
ss = lower(ss)
if ss == "yes":
    pass
elif get_close_matches(ss,data.keys(),cutoff = 0.8) != []:
    if get_close_matches(ss, data.keys(), cutoff = 0.8) == ["yes"]:
        pass
    else:
        exit()
#ends code if no
elif ss == "no":
    exit()
else:
    exit()

#A loop that checks with the user if they wish to continue storing address
#It will ask again until user says no
while ss == "yes" or get_close_matches(ss, data.keys(), cutoff = 0.8) == ["yes"]:
    cx += 1
    
    #Gets the input for address
    geo = str(input("Enter an Address: "))
    geog = str(input("Enter the State: "))
    
    #Creates and displays the dataframe
    Saved_Address_Geocoding_ = cc(geo,geog, Saved_Address_Geocoding_)
    print('______________________________________________________________________________________')
    print(Saved_Address_Geocoding_)
    print('______________________________________________________________________________________')

    print(" ")
    ss = str(input("Do you want to enter another address? "))
    ss = lower(ss)
    if ss == "yes":
        continue
    elif get_close_matches(ss,data.keys(),cutoff = 0.8) != []:
        if get_close_matches(ss, data.keys(), cutoff = 0.8) == ["yes"]:
            continue
        else:
            break
    elif ss == "no":
        break
    else:
        break

    
#Stores the dataframe in another file, so the user can see the addresses stored
with open("saved.txt", "w", encoding='utf-8') as save:
    save.seek(0)
    Saved_Address_Geocoding_= str(Saved_Address_Geocoding_)
    saved = save.write(Saved_Address_Geocoding_)

