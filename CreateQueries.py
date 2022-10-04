#STATEMENTS TO CREATE THE TABLES (Typically only ran as first time schema setup)
createCityTable = '''CREATE TABLE CITY (
    City_id INT PRIMARY KEY,
    City_name varchar(100)
);
'''
createScreeningTable = '''CREATE TABLE SCREENING(
    Screen_id INT PRIMARY KEY,
    Movie_id INT REFERENCES MOVIES.movie_id, 
    Cinema_id INT,  
    Screen_time varchar(250)
);'''

createMoviesTable = '''CREATE TABLE MOVIES(
    movie_id INT PRIMARY KEY,
    movie_title varchar(200),
    movie_duration int
);'''

createCinemaTable ='''CREATE TABLE CINEMA(
    Cinema_id PRIMARY KEY, 
    City_id  int REFERENCES CITY.city_id, 
    Cinema_name varchar(200)
);
'''
createBookTicketTable = '''CREATE TABLE BOOKTICKET(
    BT_ID INT PRIMARY KEY, 
    Movie_id INT REFERENCES MOVIES.movie_id, 
    Cinema_id INT REFERENCES CINEMA.Cinema_id, 
    Screen_id INT REFERENCES SCREENING.Screen_id, 
    SeatNum INT
    )'''