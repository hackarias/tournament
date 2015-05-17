-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE tournament;
CREATE DATABASE tournament;
\c tournament;


CREATE TABLE Players(
  id          SERIAL PRIMARY KEY,
  name        TEXT,
  games_won   INT,
  games_lost  INT
);

CREATE TABLE Matches(
  match_id      SERIAL PRIMARY KEY,
  winner_name   TEXT REFERENCES Players(name),
  winner_id     INT REFERENCES Players(id),
  loser_name    TEXT REFERENCES Players(name),
  loser_id      INT REFERENCES Players(id)
);


CREATE VIEW v_leaderboard AS
  SELECT * FROM Players
  ORDER BY games_won DESC;


INSERT INTO Players(name) VALUES ('Frank');
INSERT INTO Players(name) VALUES ('Jonas');
INSERT INTO Players(name) VALUES ('Martin');
INSERT INTO Players(name) VALUES ('Froudymus Benedictalia');
INSERT INTO Players(name) VALUES ('Dropbox Ferrari');
INSERT INTO Players(name) VALUES ('Rhino Gucci');