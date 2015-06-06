-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE Players(
  id      SERIAL PRIMARY KEY DELETE ,
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
  SELECT * FROM Players
  GROUP BY id;

CREATE FUNCTION report_match(INTEGER, INTEGER) RETURNS VOID AS $$
  INSERT INTO Matches(winner, loser) VALUES($1, $2);
  UPDATE Players SET wins = wins + 1 WHERE id = $1;
  UPDATE Players SET matches = matches + 1 WHERE id = $1;
  UPDATE Players SET matches = matches +1 WHERE id = $2;
$$ LANGUAGE SQL;

