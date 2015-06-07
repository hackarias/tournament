# Udacity FSND Project 2 #

### What is this repository for? ###

This project contains an applications that runs a swiss style tournament. 

This is the basic version of the final assignment for the Introduction to Relational Databases Udacity course. No extra credit criterias have been met in this version.
**Version 1.0.**

| File | Description |
|------|-------------|
|t**ournament.sql**| This is the database where matches and players are recorded and stored.|
|**tournament.py**| This file is the Python file containing the functions that executes the tournament.|
|**tournament_test.py**| This file contains the unit_tests provided by Udacity|


### Dependencies: ###
**Vagrant**. Please follow the [Vagrant installation guide](https://docs.vagrantup.com/v2/installation/) before proceeding.

### How do I get set up? ###
Paste the following in your terminal(make sure to have navigated to where you want to clone the repository): 
~~~~
git clone https://github.com/zackgus/fsnd--tournament.git
cd fsnd--tournament/vagrant/
vagrant up
~~~~

### Execute the application ###
How to create the database:
~~~~
psql -f tournament.sql
~~~~
This will drop the existing database and create a new, empty database.

### Example code ###
Here are some example code. The exmple below is run in the Python shell in this projects Vagrant folder:
```
>>> import tournament
>>> tournament.register_player('player_one')
>>> tournament.register_player('player_two')
>>> tournament.swiss_pairings()
[(2, 'player_two', 1, 'player_one')]
```

### How to run unit tests manually ###
To run the unit tests manually, simply log in to the Vagrant VM by typing the following in your terminal.
Make sure you're in the correct folder:
~~~~
cd fsnd--tournament/vagrant/
~~~~
Then sign in to the Vagrant VM:
~~~~
vagrant ssh
~~~~
Then navigate to the this projects folder:
~~~~
cd /vagrant/tournament
python tournament_test.py
~~~~

### Sources ###
SQL functions: http://www.postgresql.org/docs/9.4/static/xfunc-sql.html
