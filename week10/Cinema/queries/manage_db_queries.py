INSERT_INTO_USER = '''
    INSERT INTO USER (USERNAME, PASSWORD) VALUES (?, ?)
'''

INSERT_INTO_PROJECTION = '''
    INSERT INTO PROJECTION (MOVIE_ID, TYPE, DATE, TIME)
    VALUES (?, ?, ?, ?)
'''

INSERT_INTO_MOVIE = '''
    INSERT INTO MOVIE (NAME, RATING)
    VALUES (?, ?)
'''

INSERT_INTO_RESERVATION = '''
    INSERT INTO RESERVATION (USER_ID, PROJECTION_ID, ROW, COL)
    VALUES (?, ?, ?, ?)
'''

REMOVE_RESERVATION = '''
    DELETE
    FROM RESERVATION
    JOIN USER ON USER.ID = RESERVATION.USER_ID
    WHERE USERNAME = ?
'''

SELECT_MOVIE_BY_ID = '''
    SELECT NAME
    FROM MOVIE
    WHERE ID = ?
'''

SELECT_USER = '''
    SELECT *
    FROM USER
    WHERE USERNAME = ? AND PASSWORD = ?
'''

LOGIN_USER = '''
    UPDATE USER
    SET IS_LOGGED = 1
    WHERE USERNAME = ? AND PASSWORD = ?
'''

LOGOUT_USER = '''
    UPDATE USER
    SET IS_LOGGED = 0
    WHERE USERNAME = ?
'''

MOVIES_ORDERED_BY_RATING = '''
    SELECT ID, NAME, RATING
    FROM MOVIE
    ORDER BY RATING ASC
'''

ALL_PROJECTIONS_FOR_MOVIE = '''
    SELECT ID, TYPE, DATE
    FROM PROJECTION
    WHERE MOVIE_ID = ?
'''

ALL_PROJECTIONS_FOR_MOVIE_BY_DATE = '''
    SELECT ID, TYPE, TIME
    FROM PROJECTION
    WHERE MOVIE_ID = ? AND DATE = ?
'''
