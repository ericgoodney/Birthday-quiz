"""
birthday.py
Author: <your name here>
Credit: <list sources used, if any>
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""

name = str(input("Hello, what is your name? "))
month = str(input("Hi " + name + ", what was the name of the month you were born in? "))
year = str(input("And what year were you born in, " + name + "? "))
day = str(input("And the day? "))

a = ["january" , "January"]
b = ["february" , "February"]
c = ["march" , "March"]
d = ["april" , "April"]
e = ["may" , "May"]
f = ["june"  , "June"]
g = ["july" , "July"]
h = ["august" , "August"]
i = ["september" , "September"]
j = ["october" , "October"]
k = ["november" , "November"]
l = ["december" , "December"]






if month in ["october" , "October"] and day == "31" :
    print("You were born on Halloween!")
    
elif year in ["2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018", "2019"]
    print("You are a baby of the two thousands!")
else:
    print("" + name + ", hope your next birthday is the best birthday ever!")










