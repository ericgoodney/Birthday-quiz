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

spring = ["march" , "March" , "april" , "April" , "may" , "May" ]
summer =["june" , "June", "july" , "July" , "august" , "August" , "september" , "September"]
fall = ["october" , "October" , "november" , "November" , "december" , "December"]
winter = [ "january" , "January" , "february" , "February" , "march" , "March"]

if month in ["october" , "October"] and day == "31" :
    print("You were born on Halloween!")
    
elif year in ["2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018", "2019"] and month in ["march" , "March" , "april" , "April" , "may" , "May" ] : 
    print("You are a spring baby of the two thousands!")
elif year in ["2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018", "2019"] and month in ["june" , "June", "july" , "July" , "august" , "August" , "september" , "September"] :
    print("You are a summer baby of the two thousands!")
elif year in ["2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018", "2019"] and month in ["october" , "October" , "november" , "November" , "december" , "December"] : 
    print("You are a fall baby of the two thousands!")
elif year in ["2000" , "2001" , "2002" , "2003" , "2004" , "2005" , "2006" , "2007" , "2008" , "2009" , "2010" , "2011" , "2012" , "2013" , "2014" , "2015" , "2016" , "2017" , "2018", "2019"] and month in [ "january" , "January" , "february" , "February" , "march" , "March"] :
    print("You are a winter baby of the two thousands!")
    
elif year in ["1990", "1991" , "1993" , "1994" , "1995" , "1996" , "1997" , "1998" , "1999"] and month in ["march" , "March" , "april" , "April" , "may" , "May" ] :
    print("You are a spring baby of the nineties")
elif year in ["1990", "1991" , "1993" , "1994" , "1995" , "1996" , "1997" , "1998" , "1999"] and month in ["june" , "June", "july" , "July" , "august" , "August" , "september" , "September"] :
    print("You are a summer baby of the nineties")
elif year in ["1990", "1991" , "1993" , "1994" , "1995" , "1996" , "1997" , "1998" , "1999"] and month in ["october" , "October" , "november" , "November" , "december" , "December"] :
    print("You are a fall baby of the nienties")
elif year in ["1990", "1991" , "1993" , "1994" , "1995" , "1996" , "1997" , "1998" , "1999"] and month in [ "january" , "January" , "february" , "February" , "march" , "March"] :
    print("you are a winter baby of the nienties")
    
elif year in ["1980" , "1981", "1982" , "1983" , "1984" , "1985" , "1986" , "1987" , "1988" , "1989"] and month in ["march" , "March" , "april" , "April" , "may" , "May" ] :
    print("You are a spring baby of the eighties")
elif year in ["1980" , "1981", "1982" , "1983" , "1984" , "1985" , "1986" , "1987" , "1988" , "1989"] and month in ["june" , "June", "july" , "July" , "august" , "August" , "september" , "September"] :
    print("You are a summer baby of the eighties")
elif year in ["1980" , "1981", "1982" , "1983" , "1984" , "1985" , "1986" , "1987" , "1988" , "1989"] and month in ["october" , "October" , "november" , "November" , "december" , "December"] :
    print("You are a fall baby of the eighties")
elif year in ["1980" , "1981", "1982" , "1983" , "1984" , "1985" , "1986" , "1987" , "1988" , "1989"] and month in [ "january" , "January" , "february" , "February" , "march" , "March"] :
    print("You are a winter baby of the eighties")

elif year in range(1000, 1980) and month in ["march" , "March" , "april" , "April" , "may" , "May" ] :
    print("You are a spring baby of the stone age")
elif year in range(1000, 1980) and month in ["june" , "June", "july" , "July" , "august" , "August" , "september" , "September"] :
    print("You are a summer baby of the stone age")
elif year in range(1000, 1980) and month in ["october" , "October" , "november" , "November" , "december" , "December"] :
    print("You are a fall baby of the stone age")
elif year in range([1000], 1980,[1]) and month in [ "january" , "January" , "february" , "February" , "march" , "March"] :
    print("You are a winter baby of the stone age")











