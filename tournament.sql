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
  id          SERIAL PRIMARY KEY AUTOINCREMENT,
  name        TEXT,
  games_won   INT,
  games_lost  INT
);

CREATE TABLE Matches(
  match_id      SERIAL PRIMARY KEY
);

CREATE VIEW v_leaderboard AS
  SELECT * FROM Players
  ORDER BY games_won DESC;


INSERT INTO Players(name, games_won, games_lost) VALUES ('Frank', 1, 2);
INSERT INTO Players(name, games_won, games_lost) VALUES ('Hank', 1, 3);
INSERT INTO Players(name, games_won, games_lost) VALUES ('Shank', 1, 1);
INSERT INTO Players(name, games_won, games_lost) VALUES ('Krank', 3, 0);
INSERT INTO Players(name, games_won, games_lost) VALUES ('Lank', 0, 3);
INSERT INTO Players(name, games_won, games_lost) VALUES ('Tank', 2, 1);

INSERT INTO Matches VALUES (1)