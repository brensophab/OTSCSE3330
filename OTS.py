import sqlite3
from tkinter import *
import csv
from CreateQueries import *
from InsertQueries import *


root = Tk()
con = sqlite3.connect("OTS.db")
cur=con.cursor()
# cur.execute(createBookTicketTable)
cur.execute(createCinemaTable)
# cur.execute(createCityTable)
# cur.execute(createScreeningTable)
# cur.execute(createBookTicketTable)

BookTicketFile  = open('CSVDATA\BookTicket.csv')
CinemaFile      = open('CSVDATA\Cinema.csv')
CityFile        = open('CSVDATA\City.csv')
MoviesFile      = open('CSVDATA\Movies.csv')
ScreeningFile   = open('CSVDATA\Screening.csv')

bookTicketContents = csv.reader(BookTicketFile)
cinemaContents     = csv.reader(CinemaFile) 
cityContents       = csv.reader(CityFile)
moviesContents     = csv.reader(MoviesFile)
screeningContents  = csv.reader(ScreeningFile)

# cur.executemany(insert_BookTicket_records, bookTicketContents)
cur.executemany(insert_Cinema_records,cinemaContents)
# cur.executemany(insert_city_records,cityContents) Uncomment to insert values from city db
# cur.executemany(insert_Movies_records,moviesContents)
# cur.executemany(insert_Screening_records,screeningContents)

#RUN INSERT COMANDS FOR ONLY FIRST TIME SETUP
select_all_cities = "SELECT * FROM CITY"
select_all_BookTickets = "SELECT * FROM BOOKTICKET"
#DEBUG TO CMDLINE 23-25
def debugCitiesTable():
    rows = cur.execute(select_all_cities).fetchall()
    for r in rows: #PRINT OUT CI
        print(r)
def debugBOOKTICKETTables():
    rows = cur.execute(select_all_BookTickets).fetchAll()
    for r in rows:
        print(r)
# debugCitiesTable()
debugBOOKTICKETTables()

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