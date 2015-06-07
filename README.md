# Udacity FSND Project 2 #

This README would normally document whatever steps are necessary to get your application up and running.

### What is this repository for? ###

* This is the basic version of the final assignment for the Introduction to Relational Databases Udacity course. No extra credit criterias have been met in this version.
* Version 1.0.

### How do I get set up? ###

#### Dependencies: ####
* Vagrant. Please follow the [Vagrant installation guide](https://docs.vagrantup.com/v2/installation/) before proceeding.
* PostgreSQL (with psycopg2). Please see configuration & execution steps below for instructions.

#### Configuration & Execution####
In the reporistory folder, run **chmod a+x pg_script.sh && sudo ./pg_script.sh**.
This will:
- Update or install postgresql, python-psycopg2 and python-pip depending on if you have them installed already or not.
- Create a postgres user amd the tournament database.
- Run all unit tests.

#### How to run unit tests manually ####
In this repository folder, run: **python vagrant/tournament/tournament_test.py**.
