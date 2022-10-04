#Contain's the insert statements to be used in OTS.db
insert_City_records         = "INSERT INTO CITY         (City_id, City_name) VALUES(?,?);"
insert_Cinema_records       = "INSERT INTO CINEMA       (Cinema_id, City_id, Cinema_name) VALUES(?,?,?);"
insert_BookTicket_records   = "INSERT INTO BOOKTICKET   (BT_ID, Movie_id, Cinema_id, Screen_id, SeatNum) VALUES(?,?,?,?,?);"
insert_Movies_records       = "INSERT INTO MOVIES       (Movie_id, Movie_title, Movie_Duration) VALUES(?,?,?);"
insert_Screening_records    = "INSERT INTO SCREENING    (Movie_id, Cinema_id, Screen_id, Screen_time) VALUES(?,?);"
