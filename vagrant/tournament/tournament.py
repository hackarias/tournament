#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect(database_name="tournament"):
    """
    Connect to the PostgreSQL database.  Returns a database connection.
    :param database_name: name of the database.
    """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except Exception, e:
        raise e


def delete_matches():
    """
    Remove all the match records from the database.
    """
    db, cursor = connect()
    try:
        cursor.execute("TRUNCATE Matches")
        db.commit()
    except Exception, e:
        raise e
    finally:
        db.close()


def delete_players():
    """
    Remove all the player records from the database.
    TODO: delete one or more players exclusively
    """
    db, cursor = connect()
    try:
        cursor.execute("DELETE FROM Players")
        db.commit()
    except Exception, e:
        raise e
    finally:
        db.close()


def count_players():
    """
    Returns the number of players currently registered.
    """
    global row
    db, cursor = connect()
    try:
        cursor.execute("SELECT COUNT(id) FROM Players")
        row = cursor.fetchone()
    except Exception, e:
        raise e
    finally:
        db.close()
    return row[0]


def register_player(name):
    """
    Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      :param name: the player's full name (need not be unique).
    """
    db, cursor = connect()
    try:
        query = "INSERT INTO Players(name) VALUES (%s)"
        parameter = (name,)
        cursor.execute(query, parameter)
        db.commit()
    except Exception, e:
        raise e
    finally:
        db.close()


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
    global standings
    db, cursor = connect()
    try:
        cursor.execute("SELECT * FROM v_player_summary")
        standings = cursor.fetchall()
    except Exception, e:
        raise e
    finally:
        db.close()
    return standings


def report_match(winner, loser):
    """
    Records the outcome of a single match between two players.

    Args:
      :param winner:  the id number of the player who won
      :param loser:  the id number of the player who lost
    """
    db, cursor = connect()
    try:
        query = "SELECT report_match(%s, %s)"
        parameter = (winner, loser,)
        cursor.execute(query, parameter)
        db.commit()
    except Exception, e:
        raise e
    finally:
        db.close()
    return winner, loser


def swiss_pairings():
    """
    Returns a list of tuples of players and their ID.

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
    db, cursor = connect()
    try:
        cursor.execute("SELECT id,name from v_player_summary")
        players = cursor.fetchall()
    except Exception, e:
        raise e
    finally:
        pairings = []
        while players:
            pairings.append(players[0] + players[1])
            del players[0:2]
        db.close()
    return pairings
