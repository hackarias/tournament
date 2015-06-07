-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

/*
  Drops the database if it already exists, and thereafter creates a new
  one and connect to it.
 */
DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

/*
  Creating the table containing the players.
  Each player has an id, name and wins/matches.
 */
CREATE TABLE Players(
  id      SERIAL PRIMARY KEY,
  name    TEXT,
  wins    INT DEFAULT 0,
  matches INT DEFAULT 0
);

/*
 Creating the table containing the matches. Each match has an id, a
  winner and a loser.
  */
CREATE TABLE Matches(
  match_id  SERIAL PRIMARY KEY,
  winner    INT REFERENCES Players(id),
  loser     INT REFERENCES Players(id)
);

/*
 Creating view for summary of players. It lists all content from the Players table, for each player.
  */
CREATE VIEW v_player_summary AS
  SELECT * FROM Players
  GROUP BY id
  order by wins desc;

/*
Creating a function for reporting matches. It takes two player IDs and updates the players table with results. The first value passed in is the winner, and the second the loser.
 */
CREATE FUNCTION report_match(winner INTEGER, loser INTEGER) RETURNS VOID AS $$
  INSERT INTO Matches(winner, loser) VALUES(winner, loser);
  UPDATE Players SET wins = wins + 1 WHERE id = winner;
  UPDATE Players SET matches = matches + 1 WHERE id = winner;
  UPDATE Players SET matches = matches +1 WHERE id = loser;
$$ LANGUAGE SQL;

