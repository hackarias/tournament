# Udacity FSND Project 2 #

### What is this repository for? ###

* This is the basic version of the final assignment for the Introduction to Relational Databases Udacity course. No extra credit criterias have been met in this version.
* Version 1.0.

#### Dependencies: ####
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

#### Example code ####
Here are some example code. The exmple below is execute in the vagrant Python interpreter:
```
>>> import tournament
>>> tournament.register_player('player_one')
>>> tournament.register_player('player_two')
>>> tournament.swiss_pairings()
[(2, 'player_two', 1, 'player_one')]
```

#### How to run unit tests manually ####
In your terminal:
~~~~
cd fsnd--tournament/vagrant/
vagrant ssh
cd /vagrant/
python tournament/tournament_test.py
~~~~

#### Sources ####
SQL functions: http://www.postgresql.org/docs/9.4/static/xfunc-sql.html
