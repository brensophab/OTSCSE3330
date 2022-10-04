import sqlite3
from tkinter import *
import csv


root =Tk()
con = sqlite3.connect("OTS.db")
cur=con.cursor()
createCityTable = '''CREATE TABLE CITY (
    City_id INT PRIMARY KEY,
    City_name varchar(100)
);
'''
# cur.execute(createCityTable)
file = open('OTSCSE3330\City.csv')
contents = csv.reader(file)

insert_records = "INSERT INTO CITY(City_id, City_name) VALUES(?,?)"
# cur.executemany(insert_records,contents)

cur.execute(insert_records)
select_all = "SELECT * FROM CITY"

#DEBUG TO CMDLINE 23-25
def debugCitiesTable():
    rows = cur.execute(select_all).fetchall()
    for r in rows: #PRINT OUT CI
        print(r)

con.commit()
con.close() 

city = Entry(root, width = 30)
city.grid(row = 3, column = 1)

#LABELS
city_label = Label(root, text = 'City: ')
city_label.grid(row =0, column = 0)

def getMoviesFromCity():        # Create SQL query such that when you
                                #Enter a city name and retrieve all the movies that are released within that particular city.
    print("Placeholder")

def listAllCinemasWithMovies(): #List all cinemas that are showing a particular movie.
    print("Placeholder")

def listBookedSeats():          #List the seats that are booked in all cinemas for a particular movie.
    print("Placeholder")

def displayShowingTimes():      #Given a specific cinema and movie list the showing times for that movie.
    print("Placeholder")

def listAvailableSeats():       #Given a movie and session time how many seats are available.
    print("Placeholder")
    
def listReservationInfo():      #Given a reservation# list the cinema, movie session, and time where seats were booked.
    print("PH")

def listMovieInfo():            #Given a reservation# list the cinema, movie session, and time where seats were booked.
    print("PH")

def listUnavailable():          #Given a session time list movie title and session times that do not have any seats available.
    print("PH")

root.mainloop()