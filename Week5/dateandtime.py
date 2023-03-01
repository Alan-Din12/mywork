#Author : Alan Dineen
#This program is geared towards the weekly task

#set your lists
a = ["Sat", "Sun"]
b = ["Mon","Tue","Wed","Thur","Fri"]



import datetime

x = datetime.datetime.now()
#get only the day in short form eg 'Mon'
y = (x.strftime("%a"))

#Create your if statement: 
if (y != a): 
    print ("Unfortunately it is not the weekend")
else :
    print ("It is the weekend! Woohoo!!!")





