#Author : Alan Dineen
#This program is about dictionaries

car = {
    "Make" : "Volkswagen",
    "Model" : "Golf 1.4 TSI",
    "Year" : 2011,
    "Colour" : "Silver",
    "Owner" : {
    "name" : "Alan D",
    "Driver ID" : 123
        
    }
}

print (car ["Make"])
print(car ["Model"])
print (car ["Year"]) 
print (car ["Owner"] ["name"])
print (type(car["Owner"].get("names")))