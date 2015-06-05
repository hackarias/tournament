#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """
    Connect to the PostgreSQL database.  Returns a database connection.
    """
    conn_string = "dbname=tournament"
    return psycopg2.connect(conn_string)


def delete_matches():
    """
    Remove all the match records from the database.
    """
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM Matches"
    cursor.execute(query)
    conn.commit()
    conn.close()


def delete_players():
    """
    Remove all the player records from the database.
    TODO: delete one or more players exclusively
    """
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM Players"
    cursor.execute(query)
    conn.commit()
    conn.close()


def count_players():
    """
    Returns the number of players currently registered.
    """
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT COUNT(id) FROM Players"
    cursor.execute(query)
    row = cursor.fetchone()
    conn.close()
    return row[0]  # NO. This is a very ugly hack. TODO


def register_player(name):
    """
    Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      :param name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO Players(name) VALUES (%s)"
    cursor.execute(query, (name,))
    conn.commit()
    conn.close()


def player_standings():
    """
    Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    cursor = conn.cursor()
    query = "SELECT * FROM v_player_summary"
    cursor.execute(query)
    standings = cursor.fetchall()
    conn.close()
    return standings


def report_match(winner, loser):
    """
    Records the outcome of a single match between two players.

    Args:
      :param winner:  the id number of the player who won
      :param loser:  the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()

    # create a match
    query = "INSERT INTO Matches(winner, loser) VALUES(%s, %s)"
    cursor.execute(query, (winner, loser))
    conn.commit()

    # Add 1 to matches and 1 to wins for the winning player.
    cursor.execute("UPDATE Players SET wins=wins + 1 WHERE id = %s",
                   (winner,))
    cursor.execute("UPDATE Players SET matches=matches + 1 WHERE id = %s",
                   (winner,))
    conn.commit()
    # Add 1 to matches and leave wins for the losing player.
    cursor.execute("UPDATE Players SET matches=matches + 1 WHERE id = %s",
                   (loser,))
    conn.commit()
    conn.close()


def swiss_pairings():
    """
    Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    cursor = conn.cursor()
    query = ""
    cursor.execute(query)
    conn.close()