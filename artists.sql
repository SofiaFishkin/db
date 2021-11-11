CREATE DATABASE artists_2;

\c artists_2;

CREATE TABLE IF NOT EXISTS playlist (
	playlist_id serial not null,
	title varchar(100) not null,
	year smallint not null,
	PRIMARY KEY (playlist_id)
);

CREATE TABLE IF NOT EXISTS artist (
	artist_id serial,
	name varchar(100) not null,
	PRIMARY KEY (artist_id)
);

CREATE TABLE IF NOT EXISTS album (
	album_id serial,
	album_name varchar(150) not null,
	year smallint not null,
	PRIMARY KEY (album_id)
);

CREATE TABLE IF NOT EXISTS tracks (
	track_id serial,
	duration int not null default 0,
	title varchar(100) not null,	
	album_id serial references album(album_id),
	PRIMARY KEY (track_id)
);

CREATE TABLE IF NOT EXISTS genre (
	genre_id serial not null,
	genre_name varchar(50) not null,
	PRIMARY KEY (genre_id)
);

CREATE TABLE IF NOT EXISTS artist_genre (
  artist_id serial NOT NULL,
  genre_id serial NOT NULL,
  PRIMARY KEY (artist_id, genre_id),
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
  FOREIGN KEY (genre_id) REFERENCES genre(genre_id)
);

CREATE TABLE IF NOT EXISTS artist_album (
  artist_id serial NOT NULL,
  album_id serial NOT NULL,
  PRIMARY KEY (artist_id, album_id),
  FOREIGN KEY (artist_id) REFERENCES artist(artist_id),
  FOREIGN KEY (album_id) REFERENCES album(album_id)
);

CREATE TABLE IF NOT EXISTS tracks_playlist (
  track_id serial NOT NULL,
  playlist_id serial NOT NULL,
  PRIMARY KEY (track_id, playlist_id),
  FOREIGN KEY (track_id) REFERENCES tracks(track_id),
  FOREIGN KEY (playlist_id) REFERENCES playlist(playlist_id)
);











