import sqlalchemy
from sqlalchemy import create_engine

engine = create_engine('postgresql://rachelfishkin:160998@localhost:5432/artists_2')

engine.connect
print(engine.table_names())

joinedString = ",".join(engine.table_names())

engine.execute('TRUNCATE TABLE ' + joinedString + ' RESTART IDENTITY CASCADE')

engine.execute('''INSERT INTO genre(genre_name)
VALUES
('Russian granny core'),
('Soviet glam rock'),
('Post hardcore'),
('Middle eastern shit'),
('Industrial metal');''')

engine.execute('''INSERT INTO artist(name) VALUES
('Full trank'),
('Rammstein'),
('Árchitects'),
('Omer Adam'),
('Nirvana'),
('Metallica'),
('Nadezhda Babkina'),
('Phillip Kirkorov');''')

engine.execute('''INSERT INTO album(album_name, year) VALUES
('DEUTSCHLAND', 2019),
('Prince of pension', 1800),
('For those that wish to exist', 2021),
('Israeli shit: The 8', 2021),
('Collaboration with Dava', 2020),
('Sleepwalking', 2019),
('Nevermind', 1991),
('Metallica', 1991);''')

engine.execute(
    '''
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Rammstein'), (SELECT album_id FROM album WHERE album_name = 'DEUTSCHLAND');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Nirvana'), (SELECT album_id FROM album WHERE album_name = 'Nevermind');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Full trank'), (SELECT album_id FROM album WHERE album_name = 'Israeli shit: The 8');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Árchitects'), (SELECT album_id FROM album WHERE album_name = 'For those that wish to exist');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Metallica'), (SELECT album_id FROM album WHERE album_name = 'Metallica');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Nadezhda Babkina'), (SELECT album_id FROM album WHERE album_name = 'Prince of pension');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Phillip Kirkorov'), (SELECT album_id FROM album WHERE album_name = 'Collaboration with Dava');
    INSERT INTO artist_album 
    SELECT (SELECT artist_id FROM artist WHERE name = 'Omer Adam'), (SELECT album_id FROM album WHERE album_name = 'Israeli shit: The 8');

    '''
)

engine.execute(
    '''
    INSERT INTO artist_genre
    SELECT (SELECT artist_id FROM artist WHERE name = 'Rammstein'), (SELECT genre_id FROM genre WHERE genre_name = 'Industrial metal');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Full trank'), (SELECT genre_id FROM genre WHERE genre_name = 'Middle eastern shit');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Árchitects'), (SELECT genre_id FROM genre WHERE genre_name = 'Post hardcore');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Omer Adam'), (SELECT genre_id FROM genre WHERE genre_name = 'Middle eastern shit');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Nirvana'), (SELECT genre_id FROM genre WHERE genre_name = 'Industrial metal');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Metallica'), (SELECT genre_id FROM genre WHERE genre_name = 'Industrial metal');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Nadezhda Babkina'), (SELECT genre_id FROM genre WHERE genre_name = 'Russian granny core');
    SELECT (SELECT artist_id FROM artist WHERE name = 'Phillip Kirkorov'), (SELECT genre_id FROM genre WHERE genre_name = 'Soviet glam rock');
    '''
)

engine.execute('''INSERT INTO playlist(title, year) VALUES
('Russian hangcore', 2020),
('Sport', 2021),
('Crying men', 2019),
('Hype', 2017),
('Phc', 2018),
('Gold classic', 2020),
('Bald classic', 2016),
('Best gigs', 2021);''')

engine.execute('''INSERT INTO tracks(title, duration, album_id) VALUES
('Moskva', 4, (SELECT album_id FROM album WHERE album_name = 'DEUTSCHLAND')),
('Sleepwalking', 3.28, (SELECT album_id FROM album WHERE album_name = 'Sleepwalking')),
('1x1', 4.00, (SELECT album_id FROM album WHERE album_name = 'Sleepwalking')),
('Animals', 4, (SELECT album_id FROM album WHERE album_name = 'For those that wish to exist')),
('Mood color - Blue', 3.50, (SELECT album_id FROM album WHERE album_name = 'Collaboration with Dava')),
('Sex', 6.00, (SELECT album_id FROM album WHERE album_name = 'DEUTSCHLAND')),
('Guitar', 2.55, (SELECT album_id FROM album WHERE album_name = 'Israeli shit: The 8')),
('Come as you are', 3.15, (SELECT album_id FROM album WHERE album_name = 'Nevermind')),
('Throne', 4.01, (SELECT album_id FROM album WHERE album_name = 'Sleepwalking')),
('Smells like teen spirit',  4.20, (SELECT album_id FROM album WHERE album_name = 'Nevermind')),
('2 insane ppl',  2.40, (SELECT album_id FROM album WHERE album_name = 'Israeli shit: The 8')),
('Enter Sadman', 5.00, (SELECT album_id FROM album WHERE album_name = 'Metallica')),
('Sleep while staying',  2.46, (SELECT album_id FROM album WHERE album_name = 'Israeli shit: The 8')),
('An Ordinary Extinction', 4.10, (SELECT album_id FROM album WHERE album_name = 'For those that wish to exist')),
('Am I guilty', 10.00, (SELECT album_id FROM album WHERE album_name = 'Prince of pension')) ;''')
