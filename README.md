# RiskyBank - Springboard Data Engineering OOP Project

[![Build Status][travis-image]][travis-url]
[![Downloads Stats][npm-downloads]][npm-url]

RiskyBank is a simple mock ATM/Banking application run via the command line. 
The program takes members personal info and adds them to a PostgreSQL database. 
Members can open accounts and make various transactions such as deposits, withdrawals, balance inquiries, as well as submit applications for financial products such as  loans and credit cards. Members, Account, and Products database tables are all linked via SQLAlchemy Object Relational Mapping (ORM).

- `raw.githubusercontent.com/jwittbold/riskybank/master/screenshots/riskybank_banner.png?sanitize=true&raw=true`

## Installation Requirements

RiskyBank is written in Python 3.8 and utilizes SQLAlchemy and a PostgreSQL database. To run RiskyBank on your machine you will first need to have the following software installed:

Python 3
https://www.python.org/downloads/

PostgreSQL
https://www.postgresql.org/download/

SQLAlchemy
```
pip install SQLAlchemy
```
psycopg2 
```
pip install psycopg2
```

Once the requisite software is installed, you can proceed to download the RiskyBank GitHub repository.

Upon download, locate the file 'config.toml', which you must modify to match your  own PostgreSQL login credentials.

- `raw.githubusercontent.com/jwittbold/riskybank/master/screenshots/database_settings_example.png?sanitize=true&raw=true`


To run RiskyBank, open a new terminal window and navigate to the downloaded folder titled 'riskybank' containing all of the application module files. 

Launch Python
```
python3
```
Launch RiskyBank by typing 'main.py' followed by <kbd>Enter</kbd. 
```
main.py
```

You should now be at the entrance of the program.


## Usage

RiskyBank takes users input to operate the program. Users are prompted with common questions regarding personal details for the purpose of opening a new account. 

- `raw.githubusercontent.com/jwittbold/riskybank/master/screenshots/jeffrey_lebowski.png?sanitize=true&raw=true`

New users are also required to open an account in order for their member info to be saved to the database.

- `raw.githubusercontent.com/jwittbold/riskybank/master/screenshots/larry_sellers.png?sanitize=true&raw=true`



## Release History

* 0.1.0
    * Initial release.


## Meta

Jack Wittbold / jwittbold@gmail.com

Distributed under the MIT License. See ``LICENSE`` for more information.
