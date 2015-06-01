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
  id      SERIAL PRIMARY KEY,
  name    TEXT,
  wins    INT DEFAULT 0,
  matches INT DEFAULT 0
);

CREATE TABLE Matches(
  match_id  SERIAL PRIMARY KEY,
  winner    INT REFERENCES Players(id),
  loser     INT REFERENCES Players(id)
);

CREATE VIEW v_player_summary AS
  SELECT id, name, wins, matches FROM Players;